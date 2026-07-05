import os

def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    user = os.environ.get("DB_USER", "aniendcards")
    password = os.environ.get("DB_PASSWORD", "changeme")
    db = os.environ.get("DB_NAME", "aniendcards")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"

    
PASETO_KEY:str = os.environ.get("PASETO_KEY", "changeme")

ACCESS_TOKEN_EXPIRE_MINUTES: int = 15