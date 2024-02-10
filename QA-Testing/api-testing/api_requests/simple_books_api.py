from random import randint

import requests

from api_requests.generate_token_request import get_token

BASE_URL = "https://simple-books-api.glitch.me"
STATUS_ENDPOINT = "/status"
GET_ALL_BOOKS_ENDPOINT = "/books"
ORDERS_ENDPOINT = "/orders"

token = get_token()

def get_api_status():
    response = requests.get(BASE_URL + STATUS_ENDPOINT)
    return response

def get_list_of_books(book_type="", limit=""):

    url = BASE_URL + GET_ALL_BOOKS_ENDPOINT + f"?type={book_type}&limit={limit}"

    # if book_type != "" and limit == "":
    #     url += f"?type={book_type}"
    # elif book_type == "" and limit != "":
    #     url += f"?limit={limit}"
    # elif book_type != "" and limit != "":
    #     url += f"?limit={limit}&book_type={book_type}"

    response = requests.get(url)
    return response

def get_book_by_id(book_id):
    url = BASE_URL + GET_ALL_BOOKS_ENDPOINT + f"/{book_id}"
    return requests.get(url)


def submit_order(book_id, customer_name):
    header_params = {
        'Authorization': f"Bearer {token}"
    }

    request_body = {
        "bookId": book_id,
        "customerName": customer_name
    }

    orders_url = BASE_URL + ORDERS_ENDPOINT
    print(f"Submitting order at: {orders_url}")
    response = requests.post(orders_url, headers=header_params, json=request_body)
    return response


def update_order(order_id, new_customer_name):
    header_params = {
        'Authorization': f"Bearer {token}"
    }

    request_body = {
        "customerName": new_customer_name
    }

    order_update_url = BASE_URL + ORDERS_ENDPOINT + f"/{order_id}"
    print(f"Updating order at: {order_update_url}")

    response = requests.patch(order_update_url, headers=header_params, json=request_body)
    return response

def get_order(order_id):
    header_params = {
        'Authorization': f"Bearer {token}"
    }
    get_order_url = BASE_URL + ORDERS_ENDPOINT + f"/{order_id}"
    print(f"Getting order from: {get_order_url}")

    return requests.get(get_order_url, headers=header_params)

def delete_an_order(order_id):
    header_params = {
        'Authorization': f"Bearer {token}"
    }
    order_delete_url = BASE_URL + ORDERS_ENDPOINT + f"/{order_id}"
    print(f"Deleting order at {order_delete_url}")
    return requests.delete(order_delete_url, headers=header_params)

# print(get_token())

# print(get_list_of_books().json())

# list_of_books: list = get_list_of_books().json()
#
# for book in list_of_books:
#     print(book['name'])
#     assert book['type'] == 'fiction' or book['type'] == 'non-fiction'

# a = 5
# a = a + 4
# a += 4


# print(get_list_of_books(limit="2", book_type="fiction").json())
