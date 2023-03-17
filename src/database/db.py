from peewee import PostgresqlDatabase
import os
import boto3
from botocore.exceptions import ClientError
import json


def db_credentials():

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
    to_dict = json.loads(secret)
    return to_dict

credentials = db_credentials()

db_name = os.environ.get("DB_NAME")

db_params = {
    "name": db_name,
    "host": credentials["host"],
    "user": credentials["username"],
    "password": credentials["password"]
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
