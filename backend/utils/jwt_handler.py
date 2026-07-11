import os
from datetime import (
    datetime,
    timedelta
)

from jose import jwt
from dotenv import load_dotenv


load_dotenv()


SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY"
)

ALGORITHM = os.getenv(
    "JWT_ALGORITHM"
)


def create_access_token(data: dict):

    to_encode = data.copy()


    expire = (
        datetime.utcnow()
        + timedelta(hours=24)
    )


    to_encode.update(
        {
            "exp": expire
        }
    )


    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    return token