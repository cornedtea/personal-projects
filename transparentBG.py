""" Code to create a transparent background for an image on greyscale background
In this project, this file takes the rock image and returns a transparent background version."""

from PIL import Image
import math


def transparent(filename: str):
    img = Image.open(filename)
    img = img.convert("RGBA")
    img_data = img.getdata()
    new_img = img.copy()
    new_data = []
    for pixel in img_data:
        dist1 = math.sqrt((pixel[0] - pixel[1]) ** 2)
        dist2 = math.sqrt((pixel[1] - pixel[2]) ** 2)
        if dist1 < 10 and dist2 < 10 and pixel[0] != 0:
            new_color = (0, 0, 0, 0)
            new_data.append(new_color)
        else:
            new_data.append(pixel)
    new_img.putdata(new_data)
    return new_img


if __name__ == "__main__":
    rock_transparent = transparent("Images/lizard.png")
    rock_transparent.show()
    rock_transparent.save("Images/lizard.png")
