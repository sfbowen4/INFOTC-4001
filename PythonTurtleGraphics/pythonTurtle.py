#Stephen Bowen 2020
#Drawing a lorenz attractor model for chaos theory using recursive functions
#Equation and original code by Ariya Shajii

import turtle
from math import atan2
import time

screen = turtle.Screen()
screen.title('Lorenz Attractor')

t = turtle.Turtle()
t.speed(10)
t.pensize(1)
t.radians()
t.pendown()

def Draw(x, y, z):
    global t
    dt = 0.01
    sigma = 10.0
    beta = 2.667
    rho = 28.0

    scale = 10
    dx, dy, dz = 0.0, 0.0, 0.0

    t.setpos(x*scale, y*scale)
    t.setheading(atan2(dy, dx))

    dx = (sigma*(y - x)) * dt
    dy = (x*(rho - z) - y) * dt
    dz = (x*y - beta*z) * dt

    x += dx
    y += dy
    z += dz

    Draw(x, y, z)

try:
    Draw(0.1, 1.0, 1.05)
except:
    #Reaches maximum recursion depth pretty quickly so this is to enjoy the beauty of the model
    print("Done")
    time.sleep(30)