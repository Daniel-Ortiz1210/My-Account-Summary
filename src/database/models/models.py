from src.database.models.base import BaseModel
from peewee import CharField, IntegerField, DateField, DecimalField, ForeignKeyField


class Account(BaseModel):
    account_number = CharField(unique=True, null=False, max_length=16)


class Transaction(BaseModel):
    id = CharField(primary_key=True, max_length=13)
    date = DateField(formats=["%m/%d/%Y"])
    transaction = DecimalField(decimal_places=2)
    account_number = ForeignKeyField(model=Account, field=Account.account_number, backref="transactions")
