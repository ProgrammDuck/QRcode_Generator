import qrcode
from qrcode.main import QRCode
import re
from colour import Color
import tkinter



def is_hex_color(hexcolor):
    hex_color_pattern = r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$'
    return bool(re.match(hex_color_pattern, hexcolor))

def is_name_color(color):
    try:
        color = color.replace(" ", "")
        Color(color)
        return True
    except ValueError:
        return False

def is_correct_colors(bg, fg):
    if not (is_hex_color(bg) or is_name_color(bg)):
        print('Background color incorrect!')
        exit(1)
    elif not (is_hex_color(fg) or is_name_color(fg)):
        print('Qr color incorrect!')
        exit(1)

qr = QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.data = str(input("Enter qr data: "))
backgroundcolor = str(input("Enter background color: "))
color = str(input("Enter qr color: "))
img_name = str(input("Enter image name: ") + ".png")

is_correct_colors(backgroundcolor, color)

img = qr.make_image(
    fill_color=color,
    back_color=backgroundcolor
)

print("Trying to save image...")
img.save(img_name)
print("Success")
