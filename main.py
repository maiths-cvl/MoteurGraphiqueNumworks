from kandinsky import *

for i in range(100):
  set_pixel(i,i,color(0,0,255))
  set_pixel(i+100,100,color(255,0,0))
  set_pixel(i+200,i+100,color(0,255,0))


def rectangle(x=10, y=10, width=10, height=10, fill=True):
    for i in range(width):
        set_pixel(x+i, y, color(0,0,255))
    for i in range(height):
        set_pixel(x, y+i, color(0,0,255))
    w = width
    for w in range(width):
        set_pixel(x+w, y+height, color(0,0,255))
        w-=1
    h = height
    for h in range(height):
        set_pixel(x+width, y+h, color(0,0,255))
        h-=1

    if fill == True:
        for i in range(height):
            for o in range(width):
                set_pixel(x+o, y+i, color(0,0,255))

  