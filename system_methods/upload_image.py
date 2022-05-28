import time
from PIL import Image
import json
from system_methods.hash_string import get_hash

def upload(file):
    try:
        file = Image.open(file.stream)

        im_resize = file.resize((100, 100))

        newname = get_hash(str(time.time() * 1000))

        im_resize.save((f'public_resources/img/perfil/{newname}.webp'), format="WEBP")

        return True, (f"http://127.0.0.1:5000/public/perfil/{newname}.webp")
 
    except Exception as e:
        return False, ''