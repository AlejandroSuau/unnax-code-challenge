import mock

from django.test import SimpleTestCase

from parser.account_parser import AccountParser


class TestParser(SimpleTestCase):

    @mock.patch("parser.account_parser.AccountParser")
    def _test_parser_result(self, mock_class):
        pass
