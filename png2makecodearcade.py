from PIL import Image
import argparse
import numpy as np
import json
import re

# finds color from palette closest to color argument and returns its index in the palette


def palette_loader(filename: str):
    with open(filename) as file:
        data = json.load(file)
    palette=[]
    for el in data:
        if not re.match( r"^#[0-9a-f]{6}$", el):
            raise Exception("invalid palette entry:", el)
        palette.append(list(bytearray.fromhex(el[1:])))
    return palette
        

def find_palette_index(palette, color):
    colors = np.array(palette)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2, axis=1))
    index_of_smallest = np.where(distances == np.amin(distances))
    return index_of_smallest[0][0]  # extract value encapsuled in tuple


def convert_image(palette, filename):
    image = Image.open(filename)
    image = image.convert("RGBA")
    outImage = Image.new("RGBA", (image.width, image.height))

    for y in range(image.height):
        for x in range(image.width):
            pix = image.getpixel((x, y))
            rgb = list(pix[:3])
            alpha = pix[3]
            if(alpha == 0):
                pass
                print('.', end='')
                outImage.putpixel((x, y), (0, 0, 0, 0))
            else:
                pal_index = find_palette_index(palette, rgb)
                # print(pal_index)
                # indexes in makecode starts from 1
                print(format(pal_index+1, 'x'), end='')
                outImage.putpixel((x, y), tuple(palette[pal_index]))
        print()
    outImage.save('out.png')

def converter():
  
        parser = argparse.ArgumentParser()
        parser.add_argument('--pal', help='palette file')
        parser.add_argument('image', help='image to convert')
        args = parser.parse_args()

        if args.pal: palfile=args.pal
        palette = palette_loader("default.pal.json")
        convert_image(palette, args.image)
   

converter()
