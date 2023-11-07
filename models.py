import peewee

db = peewee.SqliteDatabase("database.db")

class BaseModel():
    class Meta:
        database = db

class User(BaseModel):
    name = peewee.CharField()
    address = peewee.CharField()
    billing = peewee.CharField()


class Product(BaseModel):
    name = peewee.CharField()
    description = peewee.CharField()
    price_per_unit = peewee.FloatField()
    stock_quantity = peewee.IntegerField()

# tussentabel met many to many relatie
class Transaction(BaseModel):
    buyer = peewee.ForeignKeyField(User)
    product = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()
