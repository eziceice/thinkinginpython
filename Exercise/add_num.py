from PIL import Image, ImageDraw, ImageFont, ImageColor

def add_num(image):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=40)
    filcolor = ImageColor.colormap.get('red')
    width, height = image.size
    draw.text((width - 30, 0), '5', font=font, fill=filcolor)
    image.convert('RGB').save('profile-generated.jpg')


if __name__ == '__main__':
    image = Image.open('profile.jpg')
    add_num(image)
