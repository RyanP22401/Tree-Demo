import turtle
import random
import numpy as np

# Variables to change
# Starting width
wid = 20

# Max number of steps
steps = 9

# Leaf variance
lsigma = 0.25

# Branch length variance
bsigma = 0.3

# Number of branches
segments = 40

# Bias to grow upwards
biasMult = .3



# Setting up the screen
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

# Setting up the turtle
skk = turtle.Turtle()
skk.speed(20)
skk.hideturtle()

def resetTurtle(skk):
    skk.speed(100)
    skk.pu()
    skk.width(12)
    skk.setheading(90)
    skk.setx(0)
    skk.sety(-150)
    skk.pd()
    skk.speed(20)

# Movement
for x in range(segments):
    cs = 0
    cw = wid
    resetTurtle(skk)

    while cs < steps:
        cw -= int(wid/steps) * random.randrange(1,2)
        if cw < 1: break
        skk.width(cw)
        bias = int(-1*(skk.heading()-90)*biasMult)
        skk.left(np.random.normal(0, lsigma, 1) * 90 + bias)
        cs += 1
        skk.forward(abs(int(np.random.normal(0, bsigma, 1)[0] * 100)+50))

turtle.done()