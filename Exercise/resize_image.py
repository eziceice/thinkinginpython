from PIL import Image
import glob


def resize(path):
    for filename in glob.glob(path + '/*.jpg'):
        img = Image.open(filename)
        new_size = (640, 1136)
        img = img.resize(new_size)
        img.save('{}'.format(filename.replace('jpg', 'jpeg')))


if __name__ == '__main__':
    resize('resources')