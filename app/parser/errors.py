class NotValidLogin(Exception):
    def __str__(self):
        return "Incorrect username or password."


class UnexpectedLoginStructure(Exception):
    def __str__(self):
        return "Unexpected login source code structure"


class UnexpectedCustomerStructure(Exception):
    def __str__(self):
        return "Unexpected customer source code structure"


class UnexpectedAccountStructure(Exception):
    def __str__(self):
        return "Unexpected account source code structure"


class UnexpectedStatementStructure(Exception):
    def __str__(self):
        return "Unexpected statement source code structure"
