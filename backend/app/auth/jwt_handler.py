from jose import jwt

from backend.app.services.user_service import (
    get_user
)

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"


def create_token(
    username
):

    payload = {

        "sub": username
    }

    token = jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM
    )

    return token

def verify_token(
    token
):

    payload = jwt.decode(

        token,

        SECRET_KEY,

        algorithms=[ALGORITHM]
    )

    return payload

def get_current_user(
    token
):

    payload = verify_token(
        token
    )

    username = payload[
        "sub"
    ]

    user = get_user(
        username
    )

    return user