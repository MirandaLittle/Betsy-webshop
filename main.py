# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

import models
import os
from spellchecker import SpellChecker

spell = SpellChecker()

def search(term):
    """
    Search for a specific term in the product name and product description
    """
    product_list = []
    term_lowercase = term.lower()
    corrected = spell.correction(term_lowercase)
    query = (
        models.Product.select(models.Product.name, models.Product.description)
        .where(
            (models.Product.name.contains(corrected)) | 
            (models.Product.description.contains(corrected)))
    )
    for product in query:
        product_list.append(product.name)
    return product_list


def list_user_products(user_id):
    """
    list all products that a user owns using the id of the user
    """
    product_list = []
    query = (
        models.UserProduct.select()
        .join(models.Product)
        .where(models.UserProduct.user == user_id)
    )
    for user in query:
        product_list.append(user.product.name)
    return product_list
    


def list_products_per_tag(tag_id):
    """
    list all products with a specific tag using the id of the tag
    """
    product_list = []
    query = (
        models.TagProduct.select()
        .join(models.Product)
        .where(models.TagProduct.tag == tag_id)
    )
    for product in query:
        product_list.append(product.product.name)
    return product_list


def add_product_to_catalog(user_id, product_name, description, price_per_unit,stock_quantity):
    """
    add a product to the catalog of products and link it to a specific user using the id of the user
    """
    new_product = (models.Product
           .insert(name=product_name, description=description, price_per_unit=price_per_unit, stock_quantity=stock_quantity)
           .execute())
    new_user_product = (models.UserProduct
                    .insert(user=user_id, product=new_product)
                    .execute())
    

def update_stock(product_id, new_quantity):
    """
    Update the stock quantity of a product using the product id and the new quantity
    """
    new_stock = (models.Product
           .update(stock_quantity=new_quantity)
           .where(models.Product.id == product_id)
           .execute())



def purchase_product(product_id, buyer_id, quantity):
    """
    Let a buyer purchase a product from a user and update the stock quantity of the product
    """
    transaction = (models.Transaction
                .insert(buyer=buyer_id, product=product_id, quantity=quantity)
                .execute())
    original_stock = models.Product.stock_quantity

    update = (models.Product
              .update(stock_quantity=(original_stock - quantity))
              .where(models.Product.id == product_id)
              .execute())

def remove_product(product_id):
    """
    remove a product from a user
    """
    remove = models.UserProduct.delete().where(models.UserProduct.product == product_id).execute()


print(search("chrisdmas"))
print(list_user_products(1))
print(list_products_per_tag(2))
print(add_product_to_catalog(2, "Christmas ornament", "Christmas ornament silver angel", 3.58 , 5))
print(update_stock(1, 8))
print(purchase_product(3, 2, 1))
print(remove_product(3))