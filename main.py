from PIL import Image
import os

i = 28
for filename in os.listdir('input'):
    i = filename 
    im = Image.open(f"./input/{filename}")
    os.mkdir(f'./output/{i}')
    back = im.crop((39, 32, 433, 750))
    spine = im.crop((465, 32, 567, 750))
    front = im.crop((598, 32, 994, 750))
    top = im.crop((39, 800, 433, 897))
    bottom = im.crop((596, 800, 996, 897))
    back.save(f"./output/{i}/back.jpg")
    spine.save(f"./output/{i}/spine.jpg")
    front.save(f"./output/{i}/front.jpg")
    bottom.save(f"./output/{i}/bottom.jpg")
    top.save(f"./output/{i}/top.jpg")

