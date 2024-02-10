import unittest

from api_requests.simple_books_api import submit_order, get_order


class TestSubmitOrder(unittest.TestCase):

    def test_submit_valid_order(self):
        book_id = 1
        customer_name = "PYTA10"
        response = submit_order(book_id, customer_name)

        self.assertEqual(response.status_code, 201, "Unexpected status code")
        # print(response.json()['created'])
        self.assertTrue(response.json()['created'], "'created' property is not true")

        order_id = response.json()['orderId']

        get_order_response = get_order(order_id)

        expected_order_id = get_order_response.json()['id']
        expected_book_id = get_order_response.json()['bookId']
        expected_customer_name = get_order_response.json()['customerName']

        self.assertEqual(expected_order_id, order_id)
        self.assertEqual(expected_book_id, book_id)
        self.assertEqual(expected_customer_name, customer_name)


    def test_submit_order_with_invalid_book_id(self):
        response = submit_order(20, "PYTA10")

        expected_error_message = "Invalid or missing bookId."
        actual_error_message = response.json()['error']

        self.assertEqual(expected_error_message, actual_error_message, "Unexpected error message")
