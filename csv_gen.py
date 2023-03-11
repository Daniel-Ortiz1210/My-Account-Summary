from transactions import build_transaction


def create_csv_file(func):
    def wrapper(*args, **kwargs):
        import csv
        import uuid

        result = func(*args, **kwargs)
        with open(f"csv/{uuid.uuid4().__str__()}.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)

            for row in result:
                csv_writer.writerow(row)
        return result
    return wrapper


@create_csv_file
def build_transactions_file(transaction_builder, account):
    headers = ["Id", "Date", "Transaction", "Account"]

    csv_body = [headers]

    for _ in range(30):
        csv_body.append(transaction_builder(account))

    return csv_body
