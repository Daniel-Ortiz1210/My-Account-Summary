from src.utils.account_statement import get_statement_summary

import urllib.request
import ssl
import base64
import sendgrid
from sendgrid.helpers.mail import Mail, Email, From, To, Subject, Attachment, FileContent, FileName, FileType, Disposition, TemplateId
from python_http_client.exceptions import HTTPError

def send_email(account_number, email, statement_summary=get_statement_summary):

    ssl._create_default_https_context = ssl._create_unverified_context

    client = sendgrid.SendGridAPIClient(api_key="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")
    statement_summary = statement_summary(account_number)
    transactions_by_month = ""

    for month, count in statement_summary["transactions_by_month"].items():
        transactions_by_month += f"Transacciones en {month}: {count}<br>"

    with open(file="src/templates/email.html") as template:
        template = template.read()

    with open(file=f"csv/{account_number}.csv", mode='rb') as csv_file:
        csv_file = csv_file.read()
        csv_file_encoded = base64.b64encode(csv_file).decode()

    mail = Mail(
            from_email=From("thisisdanielortiz@gmail.com"),  
            subject=Subject("Aqui está tu estado de cuenta"),
            to_emails=To(email),
            plain_text_content="Tomáte tu tiempo para revisar todo! Estamos a tus órdenes",
            html_content=template.replace(
                ":balance", str(statement_summary["balance"])).replace(
                ":avg_credit", str(statement_summary["average_credit_amount"])).replace(
                ":avg_debit", str(statement_summary["average_debit_amount"])).replace(
                ":month_transactions", transactions_by_month)
            )
    attachment = Attachment()
    attachment.file_content = FileContent(csv_file_encoded)
    attachment.file_name = FileName("estado_cuenta.csv")
    attachment.file_type = FileType("text/csv")
    attachment.disposition = Disposition("attachment")

    try:
        mail.attachment = attachment
        response = client.send(mail)
        return {"status": response.status_code}
    except HTTPError as e:
        return {"status": response.status_code, "info": e}
    