import unittest

from HTMLTestRunner import HTMLTestRunner

from tests.test_api_status import TestApiStatus
from tests.test_delete_order import TestDeleteOrder
from tests.test_get_book_by_id import TestGetBookById
from tests.test_get_list_of_books import TestListOfBooks
from tests.test_submit_orders import TestSubmitOrder
from tests.test_update_order import TestUpdateOrder


class TestSuite(unittest.TestCase):

    def test_suite(self):

        # Definim un obiect care reprezinta suita de teste
        suta_de_teste = unittest.TestSuite()
        suta_de_teste.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus))
        suta_de_teste.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteOrder))
        suta_de_teste.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestGetBookById))
        suta_de_teste.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestListOfBooks))
        suta_de_teste.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder))
        suta_de_teste.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestUpdateOrder))

        runner = HTMLTestRunner()

        runner.run(suta_de_teste)