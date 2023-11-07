# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

import models
import os

def search(term):
    ...


def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...

def populate_test_database():
    models.db.connect()
    models.db.create_tables(
        [
            models.User,
            models.Product,
            models.Transaction,
        ]
    )

    user_data = [
        ("Saskia Smit", "Kastanjelaan 42, 1080 AB, Amsterdam", "NLINGB000123456"),
        ("James de Jong", "Acacialaan 3, 1075 CD, Amsterdam", "NLASN000456789")
    ]

    product_data = [
        ("Tote bag", "Tote bag with cat illustration", 8.99, 10)
        ("Knitted sweater", "Striped knitted sweater with black and white", 33.99, 5)
    ]

    transaction_data = [
        (0, 1)
        (1, 0)

    ]
    models.db.close()
