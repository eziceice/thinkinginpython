import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def generate_letters():
    code = random.choices(string.ascii_letters, k=4)
    img = Image.new('RGB', (240, 60), 'Black')
    font = ImageFont.truetype('resources/arial.ttf', size=40)
    d = ImageDraw.Draw(img)
    for s in range(4):
        d.text((60*s + 10, 0), code[s], font=font, fill='White')
    img = img.filter(ImageFilter.BLUR)
    img.save('resources/letters.jpeg')


if __name__ == '__main__':
    generate_letters()