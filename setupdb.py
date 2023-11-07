import models
import os

def main():
    """
    Comment out the fuction you are not using and run the file.
    """
    populate_test_database()
    # delete_database()

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
        ["Saskia Smit", "Kastanjelaan 42, 1080 AB, Amsterdam", "NLINGB000123456"],
        ["James de Jong", "Acacialaan 3, 1075 CD, Amsterdam", "NLASN000456789"]
    ]

    product_data = [
        ["Tote bag", "Tote bag with cat illustration", 8.99, 10],
        ["Knitted sweater", "Striped knitted sweater with black and white", 33.99, 5]
    ]

    transaction_data = [
        [0, 1, 1],
        [1, 0, 2]

    ]

    for user in user_data:
        models.User.create(
            name=user[0],
            address=user[1],
            billing=user[2]
        )

    for product in product_data:
        models.Product.create(
            name=product[0],
            description=product[1],
            price_per_unit=product[2],
            stock_quantity=product[3]       
        )
    
    for transaction in transaction_data:
        models.Transaction.create(
            buyer=transaction[0],
            product=transaction[1],
            quantity=transaction[2]
        )

    models.db.close()


def delete_database():
    """
    Delete the database.
    """
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


if __name__ == "__main__":
    main()
