import unittest

from api_requests.simple_books_api import get_list_of_books


class TestListOfBooks(unittest.TestCase):

    def test_get_list_of_books_status_code(self):
        response = get_list_of_books()
        self.assertEqual(200, response.status_code)

    def test_get_list_of_books_number_of_results(self):
        response = get_list_of_books()
        self.assertTrue(len(response.json()) > 5)

    def test_get_list_of_books_filter_by_type_fiction(self):
        response = get_list_of_books(book_type="fiction")
        books = response.json()

        for book in books:
            print(book['name'])
            book_type = book['type']
            self.assertEqual(book_type, "fiction")

    def test_get_list_of_books_filter_by_type_non_fiction(self):
        response = get_list_of_books(book_type="non-fiction")
        books = response.json()

        for book in books:
            print(book['name'])
            book_type = book['type']
            self.assertEqual(book_type, "non-fiction")

    def test_get_list_of_books_filter_by_invalid_type(self):
        response = get_list_of_books(book_type="invalid_type")
        expected_error_message = "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."
        actual_error_message = response.json()["error"]

        self.assertEqual(expected_error_message, actual_error_message)