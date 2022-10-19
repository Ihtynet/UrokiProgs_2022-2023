from PIL import Image, ImageColor
from PIL import ImageDraw

width = 800
height = 800

image = Image.new("RGB", (width, height), color="white")

draw = ImageDraw.Draw(image)
#draw.line((0, 0, width, height))

dd=80
d=0
for i in range(10):
    draw.line((d,0,d,800), fill="black")
    draw.line((0,d,800,d), fill="black")
    d=d+dd

"""for i in range(10):
    x = int(width/10 * i)
    draw.line((x, 0, x, height), fill=ImageColor.getrgb("red"))"""

image.save("empty.png", "PNG")