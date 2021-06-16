import re
from datetime import datetime

from django.db import transaction

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By

from customer.models import Customer
from account.models import Currency, Account
from statement.models import Statement

from . import errors


class SeleniumContext:
    SELENIUM_HUB = "http://selenium:4444/wd/hub"

    def __init__(self):
        self.driver = webdriver.Remote(
            command_executor=self.SELENIUM_HUB,
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def __enter__(self):
        return self.driver

    def __exit__(self, type, value, traceback):
        self.driver.close()


class AccountParser:
    URL_ROOT = "http://test.unnax.com"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def parse(self):
        with SeleniumContext() as driver:
            self._login(driver)
            customer = self._parse_customer(driver)
            accounts = self._parse_accounts(driver, customer)
            statements = []
            for account in accounts:
                statements.append(self._parse_statements(driver, account))

        return customer, accounts, statements

    def _login(self, driver):
        try:
            url = f"{self.URL_ROOT}/login"

            driver.get(url)

            previous_url = driver.current_url

            username_input = driver.find_element(By.ID, "username")
            username_input.send_keys(self.username)

            password_input = driver.find_element(By.ID, "password")
            password_input.send_keys(self.password)

            form = driver.find_element(By.TAG_NAME, "form")
            form.submit()
        except Exception:
            raise errors.UnexpectedLoginStructure from None

        if previous_url == driver.current_url:
            raise errors.NotValidLogin

    def _parse_customer(self, driver):
        try:
            url = f"{self.URL_ROOT}/customer"
            driver.get(url)

            name = driver.find_element(By.TAG_NAME, "h4").text

            details = driver.find_elements(By.CLASS_NAME, "collection-item")
            phone, email, address = [i.text for i in details]

            return Customer(
                name=name,
                phone=phone,
                email=email,
                address=address
            )
        except Exception:
            raise errors.UnexpectedCustomerStructure from None

    def _parse_accounts(self, driver, customer):
        try:
            self._reset_driver_to_root(driver)

            accounts = []
            elements = driver.find_elements(By.CLASS_NAME, "collection-item")
            for element in elements:
                name = element.find_element(By.CLASS_NAME, "title").text

                details = element.find_element(By.TAG_NAME, "p").text
                number, balance = details.split("\n")
                currency_symbol, balance = (balance[0], balance[1:])

                statements_url = element.find_element(
                    By.TAG_NAME, "a"
                ).get_attribute("href")
                internal_identifier = re.search(
                    r"\d+$", statements_url
                ).group(0)

                currency = Currency.objects.get(symbol=currency_symbol)
                account = Account(
                    internal_identifier=internal_identifier,
                    name=name,
                    number=number,
                    balance=balance,
                    currency=currency,
                    customer=customer
                )
                accounts.append(account)

            return accounts
        except Exception:
            raise errors.UnexpectedAccountStructure from None

    def _parse_statements(self, driver, account):
        try:
            url = f"{self.URL_ROOT}/statements/{account.internal_identifier}"
            driver.get(url)

            statements = []

            elements = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")
            for element in elements:
                statement_details = element.find_elements(By.TAG_NAME, "td")
                concept, date, amount, balance = [i for i in statement_details]

                if "red-text" in amount.get_attribute("class").split():
                    statement_type = Statement.Type.WITHDRAW
                else:
                    statement_type = Statement.Type.DEPOSIT

                date = datetime.strptime(date.text, "%d/%m/%Y")

                statement = Statement(
                    concept=concept.text,
                    date=date.strftime("%Y-%m-%d"),
                    amount=amount.text[1:],
                    balance=balance.text[1:],
                    account=account,
                    type=statement_type
                )
                statements.append(statement)

            return statements
        except Exception:
            raise errors.UnexpectedStatementStructure from None

    def _reset_driver_to_root(self, driver):
        driver.get(self.URL_ROOT)


class AccountParserPrinter:
    STATEMENTS_HEADER = (
            f"{'Date':^10}|{'Amount':^10}|{'Balance':^10}| Concept"
    )

    @classmethod
    def print(cls, customer, accounts, statements):
        to_print = (
            f"\n{customer}\n"
            f"Accounts ({len(accounts)})\n"
        )
        for i, account in enumerate(accounts):
            to_print += (
                f"\t{account}\n"
                f"\tStatements ({len(statements[i])})\n"
                f"\t\t{cls.STATEMENTS_HEADER}\n"
            )
            for statement in statements[i]:
                to_print += f"\t{statement}\n"
            to_print += "\n"

        print(to_print)


class AccountStoreHelper:

    @classmethod
    @transaction.atomic()
    def store(cls, task, customer, accounts, statements):
        storing_objects = [customer] + accounts
        for statement in statements:
            storing_objects += statement

        for instance in storing_objects:
            instance.task = task
            instance.save()
