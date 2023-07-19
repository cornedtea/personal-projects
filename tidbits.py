"""
**Miscellaneous Functions**

Scroll to bottom of document for sample function calls
"""

from imageTools import *
import math
import random
import turtle
import time


def pigLatin(stg):
    """
    Takes a single word as a string and returns the word in pig latin.
    This function was made for a homework problem.
    """
    vowels = "aeiou"
    sng = stg.lower()
    ix = -1
    found = False
    while ix < len(sng) - 1 and not found:
        ix += 1
        if sng[ix] in vowels:
            found = True
    if not found or sng[:ix] == '':
        return sng + 'way'
    else:
        return sng[ix:] + sng[:ix] + 'ay'


def average_color(pic: Picture, x0: int, y0: int, size: int) -> ImageColor:
    """
    Compute the average color for a portion of given picture specified by a
    square of a give size placed at the given location.
    Function given as part of homework.

    @param pic: a picture object
    @param x0: the x-coordinate of the upper-left corner of the square
    @param y0: the y-coordinate of the upper-left corner of the square
    @param size: the size of the square
    @return: average color of the portion of the picture specified by the square
    """
    wid = pic.getWidth()
    hgt = pic.getHeight()
    sum_r = 0
    sum_g = 0
    sum_b = 0
    pix_count = 0
    for x in range(x0, x0+size):
        for y in range(y0, y0+size):
            if (0 <= x < wid) and (0 <= y < hgt):
                (r, g, b) = pic.getColor(x, y)
                sum_r += r
                sum_g += g
                sum_b += b
                pix_count += 1
    return sum_r // pix_count, sum_g // pix_count, sum_b // pix_count


def mosaic(image: Picture, size: int) -> Picture:
    """ Takes an image and an integer size and returns a new picture representing
    a mosaic form of the given picture with squares regions, known as tiles,
    of size equal to the given size filled with a single color.
    This function was made for a homework problem."""
    mosImg = Picture(image.getWidth(), image.getHeight())
    tcd = 0  # tile count down
    tca = 0  # tile count across
    a = 0  # horizontal distance from beginning of tile
    b = 0  # vertical distance from beginning of tile
    for x in range(mosImg.getWidth()):
        if x % size == 0:
            tca += 1
            a = 0
        else:
            a += 1
        for y in range(mosImg.getHeight()):
            if y % size == 0:
                tcd += 1
                b = 0
            newCol = average_color(image, x - a, y - b, size)
            mosImg.setColor(x, y, newCol)
            b += 1
    return mosImg


def find_closest_color(color: ImageColor, color_list: list[ImageColor]) -> ImageColor:
    """
    Given a color and a list of colors, finds the closest color in the list to the given color.
    This function was made for a homework problem.
    """
    closestColor = color_list[0]
    for clr in color_list:
        if distance(color, clr) < distance(color, closestColor):
            closestColor = clr
    return closestColor


def recolor(pic: Picture, color_list: list[ImageColor]) -> Picture:
    """
    Given an image and a color list, produces a copy of the image using colors from the list.
    This function was made for a homework problem.
    """
    rePic = pic.copy()
    for (x, y) in rePic:
        oldColor = rePic.getColor(x, y)
        newColor = find_closest_color(oldColor, color_list)
        rePic.setColor(x, y, newColor)
    return rePic


def findNewCoords(xval: int, yval: int, xmid: int, ymid: int, angle) -> tuple:
    """
    Given the x- and y- values of a point in a plane, the x- and y-values of the center of the plane,
    and an angle of rotation, determines the new x- and y-values in the resulting rotated plane.
    This function was made for a homework problem.
    """
    xA = xval - xmid
    yA = yval - ymid
    xB = (xA * math.cos(angle)) - (yA * math.sin(angle))
    yB = (xA * math.sin(angle)) + (yA * math.cos(angle))
    xC = xB + xmid
    yC = yB + ymid
    return xC, yC


def rotatePic(image: Picture, angle: int) -> Picture:
    """
    Takes an image and an angle and returns a new copy of the picture object
    with the same size and shape as the original but with the content rotated
    by the given angle–positive values correspond to counter-clockwise rotation
    while negative values correspond to clockwise rotation.
    This function was made for a homework problem.
    """
    picWidth = image.getWidth()
    picHeight = image.getHeight()
    pic = Picture(picWidth, picHeight, (0, 0, 0))
    radAngle = math.radians(angle)
    midX = picWidth / 2
    midY = picHeight / 2
    for (x, y) in pic:
        newCoords = findNewCoords(x, y, midX, midY, radAngle)
        newX = newCoords[0]
        newY = newCoords[1]
        if 0 < newX < picWidth and 0 < newY < picHeight:
            clr = image.getColor(newX, newY)
            pic.setColor(x, y, clr)
    return pic


def background_substitution(oldBG: Picture, newBG: Picture, oldFG: Picture) -> Picture:
    """
    Takes an old background with no objects, a new background with no objects, and an image with objects
    in the foreground of the old background and returns a new image with the foreground objects on the new
    background.
    This function was made for an in-class actvity.
    """
    newFG = Picture(oldFG.getWidth(), oldFG.getHeight())
    for (x, y) in oldFG:
        OFGcol = oldFG.getColor(x, y)
        OBGcol = oldBG.getColor(x, y)
        NBGcol = newBG.getColor(x, y)
        if distance(OFGcol, OBGcol) < 100:
            newFG.setColor(x, y, NBGcol)
        else:
            newFG.setColor(x, y, OFGcol)
    return newFG


def chromakey(oldimg: Picture, newBG: Picture) -> Picture:
    """
    Takes an image with objects in the foreground of a greenscreen and a new background with no objects
    and returns a new image with the foreground objects on the new background.
    This function was made for an in-class activity.
    """
    newFG = Picture(oldimg.getWidth(), oldimg.getHeight())
    for (x, y) in newFG:
        (r, g, b) = oldimg.getColor(x, y)
        newCol = newBG.getColor(x, y)
        if g > r and g > b:
            newFG.setColor(x, y, newCol)
        else:
            newFG.setColor(x, y, (r, g, b))
    return newFG


def dragonOfEve(turt: turtle.Turtle, dist, reps: int) -> None:
    """
    Given a turtle, a distance, and an integer number of repetitions, draw the fractal known as
    the Dragon of Eve.
    This function was made for a homework problem.
    """
    if reps == 1:
        turt.forward(dist)
    else:
        l1 = dist / 2
        l2 = dist / math.sqrt(2)
        l3 = dist / 2
        turt.left(90)
        dragonOfEve(turt, l1, reps - 1)
        turt.right(135)
        dragonOfEve(turt, l2, reps - 1)
        turt.left(45)
        turt.up()
        turt.forward(l3)
        turt.left(180)
        turt.down()
        dragonOfEve(turt, l3, reps - 1)
        turt.up()
        turt.left(180)
        turt.forward(l3)
        turt.down()


def runDragonOfEve(startR: int, endR: int, dist: int):
    """
    Takes two inputs, the starting number of recursive levels and the ending number of recursive levels,
    and draws the Dragon of Eve fractal for each rep value, sleeping for 2 seconds between the end of one
    and the start of the next.
    This function was given as part of a homework assignment, and later modified by me.
    """
    screen = turtle.Screen()
    turt = turtle.Turtle()
    for r in range(startR, endR):
        turt.reset()
        turt.hideturtle()
        turt.speed(0)
        turt.up()
        turt.backward(dist / 2)
        turt.down()
        dragonOfEve(turt, dist, r)
        time.sleep(2.0)
    screen.exitonclick()


# =====================================================
# I recommend playing around with the functions!
# Some suggested function calls are commented out below.


if __name__ == "__main__":

    # Sample calls for pigLatin()
    # print('triple', pigLatin('triple'))
    # print('anvil', pigLatin('anvil'))

    # Sample call for mosaic()
    # This may take a bit to load
    # Change image path in quotations or number to experiment
    # mosaic(Picture("Images/astilbe.jpg"), 50).show()

    # Sample call for recolor()
    # Change image path in quotations or color list in brackets to experiment
    # recolor(Picture("Images/daylilies.jpg"), ["red", "yellow", "green", "black"]).show()

    # Sample call for rotatePic()
    # Change image path in quotations or integer angle to experiment
    # rotatePic(Picture("Images/butterfly.jpg"), 45).show()

    # Sample call for background_substitution() and chromakey()
    # Change image paths in quotations to change
    old_background = Picture("Images/green.png")  # image with just the old background
    new_background = Picture("Images/blue.png")  # image with the desired background
    foreground = Picture("Images/greenRock.png")  # image with desired foreground
    # foreground must be on greenscreen for chromakey or on old background for background sub
    # new and old backgrounds must be same size (e.g. 1000 x 1000)
    background_substitution(old_background, new_background, foreground).show()
    chromakey(foreground, new_background).show()

    input("Press any key to end: ")  # For use with all image-generating functions (i.e. mosaic)

    # Sample call for runDragonOfEve()
    # Change the 1st and 2nd integers to change start and end repetitions
    # Change the 3rd number to change line length (300 is recommended)
    # runDragonOfEve(1, 5, 300)
