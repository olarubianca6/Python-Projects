import unittest

from api_requests.simple_books_api import submit_order, update_order, get_order


class TestUpdateOrder(unittest.TestCase):

    def test_update_order(self):
        book_id = 1
        customer_name = "PYTA10"

        # PLASAM COMANDA
        submit_order_response = submit_order(book_id, customer_name)
        order_id = submit_order_response.json()['orderId']

        new_customer_name = "TestAutomation10"

        # UPDATAM COMANDA PLASATA
        update_order_response = update_order(order_id, new_customer_name)
        self.assertEqual(update_order_response.status_code, 204)

        # VERIFICAM CA S-A UPDATAT COMANDA IN MOD CORECT
        get_order_response = get_order(order_id)
        expected_order_id = get_order_response.json()['id']
        expected_book_id = get_order_response.json()['bookId']
        expected_customer_name = get_order_response.json()['customerName']

        self.assertEqual(expected_order_id, order_id)
        self.assertEqual(expected_book_id, book_id)
        self.assertEqual(expected_customer_name, new_customer_name)