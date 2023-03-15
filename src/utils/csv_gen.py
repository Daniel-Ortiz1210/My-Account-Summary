from src.utils.transactions_builders import build_transaction
from src.schemas.schemas import TransactionsSchema
from src.database.models.models import Transaction

import csv


def insert_transactions_to_db(account):
    
    with open(f"csv/{account}.csv", newline="") as csv_file:
        csv_file = list(csv.DictReader(csv_file))
        for row in list(csv_file):
            row["account_number"] = account
        transactions_list = TransactionsSchema(transactions=list(csv_file))

    Transaction.insert_many(transactions_list.dict()["transactions"]).execute()
    return
        

def create_csv_file(func):
    
    def wrapper(*args, **kwargs):
        import uuid

        result = func(*args, **kwargs)
        account = args[0]
        with open(f"csv/{account}.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)

            for row in result:
                csv_writer.writerow(row)
        
        insert_transactions_to_db(account)

        return csv_file

    return wrapper


@create_csv_file
def build_transactions_file(account, transaction_builder=build_transaction):
    headers = ["Id", "Date", "Transaction"]

    csv_body = [headers]

    for _ in range(30):
        csv_body.append(transaction_builder())

    return csv_body
