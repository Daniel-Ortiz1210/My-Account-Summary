import datetime
import uuid
import random

def get_transaction_import(min: int, max: int) -> float:
    random_decimal = random.uniform(-60, 60)
    rounding_decimal = round(random_decimal, 2)
    return rounding_decimal

