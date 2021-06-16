import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django
django.setup()

import argparse

from parser.account_parser import AccountParser, AccountParserPrinter


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", help="expected login username")
    parser.add_argument("--password", help="expected login password")
    args = parser.parse_args()
    if args.username and args.password:
        try:
            account_parser = AccountParser(args.username, args.password)
            customer, accounts, statements = account_parser.parse()
            AccountParserPrinter.print(customer, accounts, statements)
        except Exception as e:
            print(
                "An exception occurred: {0} {1}".format(
                    str(e.__class__), e
                )
            )
    else:
        parser.error("expected --username and --password arguments")
