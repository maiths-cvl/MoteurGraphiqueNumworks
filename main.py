from kandinsky import *
from math import *


class shape:
    def __init__(self, coloration=(125, 125, 125), xa=10, ya=10, xb=20, yb=20, width=10, height=10, r=50, fill=True):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.width = width
        self.height = height
        self.r = r
        self.fill = fill
        self.coloration = coloration

    def rectangle(self):
        for i in range(self.width):
            set_pixel(self.xa+i, self.ya, color(self.coloration))
        for i in range(self.height):
            set_pixel(self.xa, self.ya+i, color(self.coloration))
        w = self.width
        for w in range(self.width):
            set_pixel(self.xa+w, self.ya+self.height, color(self.coloration))
            w-=1
        h = self.height
        for h in range(self.height):
            set_pixel(self.xa+self.width, self.ya+h, color(self.coloration))
            h-=1

        if self.fill == True:
            for i in range(self.height):
                for o in range(self.width):
                    set_pixel(self.xa+o, self.ya+i, color(self.coloration))

    def circle(self):
        if self.fill == False:
            for angle in range(0, 360):
                x = self.xa + int(self.r * cos(angle * pi / 180))
                y = self.ya + int(self.r * sin(angle * pi / 180))
                set_pixel(x, y, color(self.coloration))
        if self.fill == True:
            for xd in range(self.xa - self.r, self.xa + self.r + 1):
                for yd in range(self.ya - self.r, self.ya + self.r + 1):
                    if (xd - self.xa) ** 2 + (yd - self.ya) ** 2 <= self.r ** 2:
                        set_pixel(xd, yd, color(self.coloration))

    def line(self):
        ydiff = abs(self.yb-self.ya)
        xl = abs(self.xb-self.xa)
        if(ydiff>0):
            freq = int(xl/ydiff)
        else:
            freq = 0
        c = 0
        for i in range(xl):
            if c >= freq and not freq == 0:
                self.ya+=1
                c = 0
            set_pixel(self.xa+i, self.ya, color(self.coloration))
            c+=1

        if xl==0:
            for i in range(ydiff):
                set_pixel(self.xa, self.ya+i, color(self.coloration))