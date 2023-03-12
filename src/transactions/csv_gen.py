from src.transactions.transactions_builders import build_transaction


def create_csv_file(func):
    def wrapper(*args, **kwargs):
        import csv
        import uuid

        result = func(*args, **kwargs)
        account = args[0]
        with open(f"csv/{account}.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)

            for row in result:
                csv_writer.writerow(row)
        return csv_file
    return wrapper


@create_csv_file
def build_transactions_file(account, transaction_builder=build_transaction):
    headers = ["Id", "Date", "Transaction"]

    csv_body = [headers]

    for _ in range(30):
        csv_body.append(transaction_builder(account))

    return csv_body
