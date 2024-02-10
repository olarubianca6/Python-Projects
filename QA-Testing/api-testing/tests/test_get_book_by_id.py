import unittest

from api_requests.simple_books_api import get_book_by_id


class TestGetBookById(unittest.TestCase):

    def test_get_book_by_id(self):
        response = get_book_by_id(1)
        book = response.json()

        self.assertEqual(book['id'], 1)
        self.assertEqual(len(book), 8)