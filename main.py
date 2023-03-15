from src.database.db import init_db
from src.database.models.models import Account
from src.utils.csv_gen import build_transactions_file
from src.utils.account_statement import get_statement_summary

from fastapi import Query, Path, status
from fastapi.responses import JSONResponse
from fastapi import FastAPI


def get_app(debug=False):
    app = FastAPI(
        debug=debug,
        openapi_url="/api/v1/openapi.json",
        docs_url="/api/docs"
    )
    init_db(drop_all=True)
    return app


app = get_app()


@app.get(path="/my_account_statement/{email}/{account_number}", tags=["Account Balance"])
def my_account_statement(email: str = Path(), account_number: str = Path(max_length=16, min_length=16)):
    from src.email.email import send_email

    account = Account.get_or_none(Account.account_number == account_number)

    if account is None:
        try:
            account = Account(account_number=account_number)
            account.save()
        except:
            return JSONResponse({"message": "No pudimos guardar tu cuenta"}, status_code=status.HTTP_400_BAD_REQUEST)
        build_transactions_file(account_number)
        send_email = send_email(account_number, email)

        if send_email["status"] == 202:
            return JSONResponse({"message": "Email enviado con exito"}, status_code=status.HTTP_200_OK)
        return JSONResponse({"message": "No pudimos enviar el email", "info": send_email["info"]}, status_code=send_email["status"])
    
    send_email = send_email(account_number, email)

    if send_email["status"] == 202:
        return JSONResponse({"message": "Email enviado con exito"}, status_code=status.HTTP_200_OK)
    return JSONResponse({"message": "No pudimos enviar el email", "info": send_email["info"]}, status_code=send_email["status"])
