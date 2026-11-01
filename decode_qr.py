from PIL import Image 
from pyzbar.pyzbar import decode
img = Image.open('generated_qrcodes/python_01.png')
decoded_objects = decode(img)
for obj in decoded_objects:
    print(f'Type: {obj.type}')
    print(f'Data: {obj.data.decode("utf-8")}')