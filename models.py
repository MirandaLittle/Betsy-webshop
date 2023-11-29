import peewee

db = peewee.SqliteDatabase("database.db")

class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    name = peewee.CharField()
    address = peewee.CharField()
    billing = peewee.CharField()


class Product(BaseModel):
    name = peewee.CharField()
    description = peewee.CharField()
    price_per_unit = peewee.DecimalField(decimal_places=2, auto_round=True)
    stock_quantity = peewee.IntegerField()

# tussentabel one to many
class UserProduct(BaseModel):
    user = peewee.ForeignKeyField(User)
    product = peewee.ForeignKeyField(Product)

# tussentabel met many to many relatie
class Transaction(BaseModel):
    buyer = peewee.ForeignKeyField(User)
    product = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()

class Tag(BaseModel):
    tag = peewee.CharField(unique=True)

# tussentabel met many to many relatie
class TagProduct(BaseModel):
    product = peewee.ForeignKeyField(Product)
    tag = peewee.ForeignKeyField(Tag)

