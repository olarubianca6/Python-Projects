import unittest

from api_requests.simple_books_api import get_api_status


class TestApiStatus(unittest.TestCase):

    def test_api_status(self):
        response = get_api_status()

        expected_status_code = 200
        actual_status_code = response.status_code
        self.assertEqual(expected_status_code, actual_status_code)

        expected_status = "OK"
        actual_status = response.json()['status']
        self.assertEqual(expected_status, actual_status)

