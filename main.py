from src.database.db import init_db
from src.endpoints.endpoints import api_router

from fastapi import FastAPI


def get_app(drop_all_tables=False):
    app = FastAPI(
        openapi_url="/api/v1/openapi.json",
        docs_url="/api/docs"
    )
    init_db(drop_all=drop_all_tables)
    return app


app = get_app()
app.include_router(router=api_router)