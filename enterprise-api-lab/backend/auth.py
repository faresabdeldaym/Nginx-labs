import jwt
import datetime

SECRET_KEY = "my-secret-key-change-this"

def generate_token(username):
    return jwt.encode({
        "user": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }, SECRET_KEY, algorithm="HS256")


def verify_token(token):
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True
    except:
        return False