import json
import time
from datetime import datetime

from db import users as users_db


# TODO 1: Don't store the plain text password.

def register(firstname: str, lastname: str, email: str, password: str):
    """This function registers a User.

    - firstname (string): First Name of the user
    - lastname (string): Last Name of the user
    - email (string) (used for login): Email of the user
    - password (string) (used for login): Password of the user
    """
    user = {
        "firstname": firstname,
        "lastname": lastname,
        "email": email,
        "password": password,
        "created_at": datetime.now(),
        "last_login": None
    }
    users_db.append(user)


def login(email: str, password: str):
    """This function is intended for user login.

    - email: Email of the user
    - password: Password of the user.
    """

    """
    if user(email, password) is in the users_db:
        print("ao g yema dalta")
    else: 
        print("na g nema")
    """


register(firstname="kami", lastname="khatak", email="kami@gmail.com", password="123")
login(email="kami@gmail.com", password="123")
print(json.dumps(users_db, indent=4, default=str))

time.sleep(20)
