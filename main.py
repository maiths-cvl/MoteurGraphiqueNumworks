from kandinsky import *
from math import *

def rectangle(x=10, y=10, width=10, height=10, coloration=(0, 255, 0), fill=True):
    for i in range(width):
        set_pixel(x+i, y, color(coloration))
    for i in range(height):
        set_pixel(x, y+i, color(coloration))
    w = width
    for w in range(width):
        set_pixel(x+w, y+height, color(coloration))
        w-=1
    h = height
    for h in range(height):
        set_pixel(x+width, y+h, color(coloration))
        h-=1

    if fill == True:
        for i in range(height):
            for o in range(width):
                set_pixel(x+o, y+i, color(coloration))

def circle(x=50, y=50, r=50, coloration=(0, 255, 0), fill=True):
    if fill == False:
        for angle in range(0, 360):
            xa = x + int(r * cos(angle * pi / 180))
            ya = y + int(r * sin(angle * pi / 180))
            set_pixel(xa, ya, color(coloration))
    if fill == True:
        for xa in range(x - r, x + r + 1):
            for ya in range(y - r, y + r + 1):
                if (xa - x) ** 2 + (ya - y) ** 2 <= r ** 2:
                    set_pixel(xa, ya, color(0, 255, 0))

def drawLine(xa=10, ya=10, xb=50, yb=50, coloration=(0, 255, 0)):
    ydiff = abs(yb-ya)
    xl = abs(xb-xa)
    freq = int(xl/ydiff)
    c = 0
    for i in range(xl):
        if c >= freq:
            ya+=1
            c = 0
        set_pixel(xa+i, ya, color(coloration))
        c+=1


drawLine()