from src.database.models.models import Account
from src.utils.csv_gen import build_transactions_file
from src.utils.account_statement import get_statement_summary

from fastapi import APIRouter
from fastapi import Query, Path, status
from fastapi.responses import JSONResponse


api_router = APIRouter()


@api_router.get(path="/my_account_statement/{email}/{account_number}", tags=["Account Balance"])
def my_account_statement(email: str = Path(), account_number: str = Path(max_length=16, min_length=16)):
    from src.email.email import send_email

    account = Account.get_or_none(Account.account_number == account_number)

    if account is None:
        try:
            account = Account(account_number=account_number)
            account.save()
        except:
            return JSONResponse({"message": "No pudimos verificar tu numero cuenta"}, status_code=status.HTTP_404_NOT_FOUND)
        build_transactions_file(account_number)
        send_email = send_email(account_number, email)

        if send_email["status"] == 202:
            return JSONResponse({"message": "Email enviado con exito"}, status_code=status.HTTP_200_OK)
        return JSONResponse({"message": "No pudimos enviar el email", "info": send_email["info"]}, status_code=status.HTTP_400_BAD_REQUEST)
    
    send_email = send_email(account_number, email)

    if send_email["status"] == 202:
        return JSONResponse({"message": "Email enviado con exito"}, status_code=status.HTTP_200_OK)
    return JSONResponse({"message": "No pudimos enviar el email"}, status_code=status.HTTP_400_BAD_REQUEST)
    