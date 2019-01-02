#!/usr/bin/python3
from PIL import Image
import sys


class DrawConsole:
    def __init__(self, image_file, resize=(100, 100)):
        self._pixel = '\x1b[48;2;{}m\x1b[38;2;{}m\u2584\x1b[0m'
        self.image = Image.open(image_file)
        self.image = self.image.resize(resize)
        self.width, self.height = self.image.size
        self.true_color = True if len(self.image.getbands()) > 3 else False

    @property
    def pixels(self):
        lines = ''
        for h in range(0, self.height, 2):
            line = ''
            for w in range(0, self.width):
                if self.true_color:
                    r, g, b, _ = self.image.getpixel((w, h))
                    r1, g1, b1, _ = self.image.getpixel((w, h+1))
                else:
                    r, g, b = self.image.getpixel((w, h))
                    r1, g1, b1 = self.image.getpixel((w, h+1))
                line += self._pixel.format('{};{};{}'.format(r, g, b), '{};{};{}'.format(r1, g1, b1))
            lines += line + '\n\r'
        return lines


if __name__ == '__main__':
    size = (100, 100)
    if sys.argv.__len__() < 2:
        print('png file name require!')
        exit(0)
    if sys.argv.__len__() == 3:
        size = [int(x) for x in sys.argv[2].split('x')]
    pic = DrawConsole(sys.argv[1], size)
    print(pic.pixels)

