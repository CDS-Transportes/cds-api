import jwt

def valid(token):
    try:
        decoded = jwt.decode(token, "Zh!vwNCHJfGx", algorithms=["HS256"])
        return True, decoded
    except jwt.ExpiredSignatureError:
        return False, ''
