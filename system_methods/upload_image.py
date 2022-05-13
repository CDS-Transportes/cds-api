import base64
import io
import requests
from PIL import Image
import json

KEY_IMGBB = '778bac42ccd8e15deb9d9a2efc81e188'

def upload(file):
    try:
        file = Image.open(file.stream).convert('RGB')
        buf = io.BytesIO()
        im_resize = file.resize((500, 500))
        im_resize.save(buf, format='JPEG')
        byte_im = buf.getvalue()

        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": KEY_IMGBB,
            "image": base64.b64encode(byte_im),
        }

        res = requests.post(url, payload)

        if(int(res.status_code) == 200):
            return True, (json.loads(res.text)['data']['url'])
        else:
            return False, ''
    except:
        return False, ''