from peewee import PostgresqlDatabase
import os
import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "db_credentials"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    return secret

"""
"database-1.c5niavzkvagt.us-east-1.rds.amazonaws.com"
"transactions"
"aZf5gT6f2KVb001"
"aZf5gT6f2KVb001"
"""



db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")
db_password = os.environ.get("DB_PASSWORD")
db_user = os.environ.get("DB_USER")


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
