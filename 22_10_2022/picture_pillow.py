from PIL import Image, ImageColor
from PIL import ImageDraw

width = 400
height = 300

image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)
draw.line((0, 0, width, height))

for i in range(10):
    x = int(width/10 * i)
    draw.line((x, 0, x, height), fill=ImageColor.getrgb("red"))

image.save("empty.png", "PNG")