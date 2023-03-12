from peewee import PostgresqlDatabase


db_params = {
    "name": "transactions",
    "host": "database-1.c5niavzkvagt.us-east-1.rds.amazonaws.com",
    "user": "postgres",
    "password": "aZf5gT6f2KVb001"
    }

psql_db = PostgresqlDatabase(
    db_params.get("name"), 
    user=db_params.get("user"), 
    password=db_params.get("password"), 
    host=db_params.get("host")
    )

def init_db():
    from src.database.models.models import Account, Transaction
    psql_db.connect()
    psql_db.create_tables(models=[Account, Transaction])
    psql_db.close()
    