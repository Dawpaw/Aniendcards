from datetime import timedelta, datetime, timezone
import json
from argon2 import PasswordHasher

import pyseto
from pyseto import Key

from src.config import PASETO_KEY

_paseto_key = Key.new(version=4, purpose="local", key=PASETO_KEY.encode(encoding="utf-8"))
default_time_delta = timedelta(minutes=15)
_ph = PasswordHasher()

def hash_password(password:str) -> str:
    return _ph.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return _ph.verify(hashed_password, plain_password)
    except Exception:
        return False

def create_access_token(data: dict, expires_delta: timedelta = default_time_delta):
    to_encode = data.copy()
    expires = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expires.isoformat()})
    token = pyseto.encode(key=_paseto_key, payload=to_encode)
    return token.decode("utf-8")

def decode_access_token(token: str):
    decoded = pyseto.decode(keys=_paseto_key, token=token)
    payload = decoded.payload
    if isinstance(payload, dict):
        return payload
    return json.loads(payload)