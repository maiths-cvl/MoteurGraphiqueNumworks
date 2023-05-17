from ge import *
import time

cir = shape((125, 125, 125), xa= 50, ya= 50, r=25).circle()
cirf = shape((255, 32, 152), xa=100, yb=50, r=25, fill=False)
cirf.circle()

linee = shape(xa= 24, ya= 10, xb = 124, yb= 35, coloration = (0, 255, 0)).line()

rect = shape()

for i in range(10):
    rect.coloration = (255, 255, 255)
    rect.xa = i*20
    rect.coloration = (0, 125, 255)
    rect.rectangle()