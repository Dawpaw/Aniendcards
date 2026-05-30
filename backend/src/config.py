SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# TODO make this do more
def get_sqlite_uri() -> str:
    return SQLALCHEMY_DATABASE_URL