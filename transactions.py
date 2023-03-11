import datetime
import uuid
import random

def get_transaction_import(min: int, max: int) -> float:
    random_decimal = random.uniform(-60, 60)
    rounding_decimal = round(random_decimal, 2)
    return rounding_decimal


def get_transaction_date(min_montn: int, max_month: int, min_day: int, max_day: int, year=2023) -> str:
    date = datetime.date(year=year, month=random.randint(min_montn, max_month), day=random.randint(min_day, max_day))
    return date.strftime("%m/%d/%Y")
    

def build_transaction(account) -> list:
    transaction = list()

    transaction.append(uuid.uuid4().__str__()[:13])
    transaction.append(get_transaction_date(min_montn=3, max_month=6, min_day=1, max_day=30))
    transaction.append(get_transaction_import(min=-60, max=60))
    transaction.append(account)

    return transaction
