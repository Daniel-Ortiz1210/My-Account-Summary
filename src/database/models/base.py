from src.database.db import psql_db
from peewee import Model

class BaseModel(Model):
    class Meta:
        database = psql_db