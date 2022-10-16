from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from datetime import datetime

def prepare_string():
    res=""
    cur_datetime=datetime.now()
    res+=str(cur_datetime.day)+"."+str(cur_datetime.month)+"."+str(cur_datetime.year)+" "+str(cur_datetime.hour)+"-"+str(cur_datetime.minute)
    return res

def prepare_image(path):
    image=Image.open(path)
    drawer=ImageDraw.Draw(image)
    font=ImageFont.truetype("arial.ttf", 25)
    drawer.text((200, 200), prepare_string(), font=font, fill=('#FF0000'))
    return image
    
def prepare_data_for_send(path):
    bio=BytesIO()
    bio.name='cat.jpeg'
    image=prepare_image(path)
    image.save(bio, 'JPEG')
    bio.seek(0)
    return bio