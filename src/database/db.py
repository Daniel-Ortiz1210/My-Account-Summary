from peewee import PostgresqlDatabase
import os


db_host = os.environ.get("DB_HOST", "database-1.c5niavzkvagt.us-east-1.rds.amazonaws.com")
db_name = os.environ.get("DB_NAME", "transactions")
db_password = os.environ.get("DB_PASSWORD", "aZf5gT6f2KVb001")
db_user = os.environ.get("DB_USER", "postgres")


db_params = {
    "name": db_name,
    "host": db_host,
    "user": db_user,
    "password": db_password
    }


psql_db = PostgresqlDatabase(
    db_params.get("name"), 
    user=db_params.get("user"), 
    password=db_params.get("password"), 
    host=db_params.get("host")
    )


def init_db(drop_all=False):
    from src.database.models.models import Account, Transaction
    with psql_db.connection_context():
        try:
            if drop_all:
                psql_db.drop_tables(models=[Account, Transaction])
                return
            psql_db.create_tables(models=[Account, Transaction])
        except:
            psql_db.rollback()
