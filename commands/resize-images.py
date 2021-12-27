import os
from PIL import Image

images_path = 'assets/media/book_images/'
requested_dimensions = {
    'width': 1280,
    'height': 720
}

fixturesNames = os.listdir(images_path)
fixturesNames.sort()

for name in fixturesNames:
    image = Image.open(images_path + name)
    image.thumbnail(size=(requested_dimensions['width'], requested_dimensions['height']))
    image.save(images_path + name)
    print('resized ' + name + ' to:')
    print(image.size)


