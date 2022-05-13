from hashlib import md5

def get_hash(text:str):
    return md5(text.encode('utf-8')).hexdigest()
