from PIL import Image
from pytesseract import image_to_string


entire_text=image_to_string(Image.open('D:\kludge19\linear_algebra.PNG'),lang='eng')
with open("Output.txt", "w") as text_file:
    text_file.write(entire_text)

import ttos    
