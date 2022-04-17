import datetime
from datetime import timezone
import jwt

def create(id, email, usuario):
    encoded_jwt = jwt.encode({"ID": id, 'EMAIL': email, 'USER': usuario, 'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(hours=5)}, "Zh!vwNCHJfGx", algorithm="HS256")
    return encoded_jwt

