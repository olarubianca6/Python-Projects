import unittest

from api_requests.simple_books_api import submit_order, delete_an_order, get_order


class TestDeleteOrder(unittest.TestCase):

    def test_delete_order(self):
        book_id = 3
        customer_name = "PYTA10"
        response = submit_order(book_id, customer_name)

        self.assertEqual(response.status_code, 201, "Unexpected status code")
        # print(response.json()['created'])
        self.assertTrue(response.json()['created'], "'created' property is not true")

        order_id = response.json()['orderId']

        delete_order_response = delete_an_order(order_id)

        self.assertEqual(delete_order_response.status_code, 204)

        get_order_response = get_order(order_id)

        expected_error_message = f"No order with id {order_id}."
        print(expected_error_message)
        actual_error_message = get_order_response.json()['error']
        self.assertEqual(expected_error_message, actual_error_message)