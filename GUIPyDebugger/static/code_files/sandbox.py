from tkinter import *
import time as t
import random

root = Tk()
canvas = Canvas(root, bg = 'black', height = 500, width = 1000)

ballCoords = (485, 235, 515, 265)


def makeBall():
    canvas.create_oval(ballCoords, fill = 'green')
makeBall()
canvas.pack()

def moveRight(ballCoords, left, right):
    left += 5
    top = ballCoords[1]
    right += 5
    bottom = ballCoords[3]
    return (left, top, right, bottom)

def moveLeft(ballCoords, left, right):
    left -= 5
    top = ballCoords[1]
    right -= 5
    bottom = ballCoords[3]
    return (left, top, right, bottom)

def moveUpRight(ballCoords, left, top, right, bottom):
    left += 5
    top -= 5
    right += 5
    bottom -= 5
    return (left, top, right, bottom)

def moveDownRight(ballCoords, left, top, right, bottom):
    left += 5
    top += 5
    right += 5
    bottom += 5
    return (left, top, right, bottom)

def moveUpLeft(ballCoords, left, top, right, bottom):
    left -= 5
    top -= 5
    right -= 5
    bottom -= 5
    return (left, top, right, bottom)

def moveDownLeft(ballCoords, left, top, right, bottom):
    left -= 5
    top += 5
    right -= 5
    bottom += 5
    return (left, top, right, bottom)

right = True
'''
while True:
    print(ballCoords)
    if right:
        ballCoords = moveRight(ballCoords, ballCoords[0], ballCoords[2])
        if ballCoords[2] == 1000:
            right = False
    elif right == False:
        ballCoords = moveLeft(ballCoords, ballCoords[0], ballCoords[2])
        if ballCoords[0] == 0:
            right = None
            upright = True
    elif upright:
        ballCoords = moveUpRight(ballCoords, ballCoords[0], ballCoords[1], ballCoords[2], ballCoords[3])
        if ballCoords[1] == 0:
            upright = False
    elif upright == False:
        ballCoords = moveDownRight(ballCoords, ballCoords[0], ballCoords[1], ballCoords[2], ballCoords[3])
        if (ballCoords[2] == 1000) or (ballCoords[3] == 500):
            upright = None
            upleft = True
    elif upleft == True:
        ballCoords = moveUpLeft(ballCoords, ballCoords[0], ballCoords[1], ballCoords[2], ballCoords[3])
        if ballCoords[1] <= 0:
            upleft = False
    elif upleft == False:
        ballCoords = moveDownLeft(ballCoords, ballCoords[0], ballCoords[1], ballCoords[2], ballCoords[3])
        if ballCoords[0] == 0:
            break

    makeBall()
    print(ballCoords)
    t.sleep(0.01)
    root.update()
    canvas.delete('all')

'''
#left top right bottom

#ball should move right, left, upright, downright, upleft, downleft
