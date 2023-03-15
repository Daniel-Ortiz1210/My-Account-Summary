from src.database.models.models import Transaction, Account
from peewee import fn
import boto3
import datetime

aws_translate = boto3.client("translate")

def get_balance(account_number):
    query = Transaction.select(
        fn.SUM(Transaction.transaction).alias("balance")).where(
            account_number==account_number).dicts(
                as_dict=True
                )
    balance = list(query)[0]["balance"]
    return float(balance)


def count_transactions_by_month(account_number):
    query = Transaction.select(
        Transaction.date.month, fn.COUNT(Transaction.id).alias("count")).where(
            Transaction.account_number==account_number).order_by(
                Transaction.date.month).group_by(
                Transaction.date.month).dicts(
                    as_dict=True
                )
    
    transactions_by_month = {}

    for column in list(query):
        month = datetime.datetime(2020, int(column["extract"]), 1).strftime("%B")
        response = aws_translate.translate_text(
            Text=month,
            SourceLanguageCode="en",
            TargetLanguageCode="es-MX",
        )
        
        transactions_by_month[response["TranslatedText"].title()] = column["count"]
    
    return transactions_by_month


def average_credit_amount(account_number):
    query = Transaction.select(
        fn.AVG(Transaction.transaction).alias("credit_average")).where(
            Transaction.account_number==account_number).where(
                Transaction.transaction >= 0).dicts(as_dict=True
                )
    average = round(query[0]["credit_average"], 2)
    return float(average)


def average_debit_amount(account_number):
    query = Transaction.select(
        fn.AVG(Transaction.transaction).alias("debit_average")).where(
            Transaction.account_number==account_number).where(
                Transaction.transaction < 0).dicts(as_dict=True
                )
    average = round(query[0]["debit_average"], 2)
    return float(average)


def get_statement_summary(account_number):
    statement_summary = {
        "balance": get_balance(account_number),
        "transactions_by_month": count_transactions_by_month(account_number),
        "average_credit_amount": average_credit_amount(account_number),
        "average_debit_amount": average_debit_amount(account_number)
        }

    return statement_summary
