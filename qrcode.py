#!/usr/bin/python3
from PIL import Image
import sys
char_list = [['\x1b[30m\u2588\x1b[0m', '\x1b[37m\u2588\x1b[0m'], ['\x1b[30m\u2588\x1b[0m', '\x1b[37m\u2588\x1b[0m']]
count = len(char_list)


def to_text(image_file):
    asd = ''
    h_size = image_file.size[1] -1  if image_file.size[1] % 2 else image_file.size[1]
    for h in range(0,  h_size, 2):
        for w in range(0, image_file.size[0]):
            try:
                r, g, b, a = image_file.getpixel((w, h))
                gray = int(r*0.2 + g*0.3 + b*0.1 + a*0.2)
                r1, g1, b1, a1 = image_file.getpixel((w, h+1))
                gray1 = int(r1*0.2 + g1*0.3 + b1*0.1 + a*0.2)
                asd += char_list[int(gray / 200)][int(gray1 / 200)]
            except TypeError:
                c = image_file.getpixel((w, h))
                c1 = image_file.getpixel((w, h+1))
                asd += char_list[1 if c else 0][1 if c1 else 0]
        asd += '\r\n'
    return asd


def main():
    size = []
    if sys.argv.__len__() < 2:
        print("Usage:{0} ImageName size\n\tExample: {1} exa.png 100x100".format(sys.argv[0],sys.argv[0]))
        return 0
    if sys.argv.__len__() == 3:
        size = sys.argv[2].split('x')
        size = [int(i) for i in size]
    image_file = Image.open(sys.argv[1])
    if not size:
        size = (100, 100)
    image_file = image_file.resize(size)
    print(to_text(image_file))


if __name__ == '__main__':
        main()
