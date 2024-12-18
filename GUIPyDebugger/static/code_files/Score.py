from Colliders import leftScreenCollide, rightScreenCollide
from Graphics import *
import time as t

score = [0, 0]
def updateScore():
    if leftScreenCollide(G.ballCoords[0]):
        score[0] += 1
    elif rightScreenCollide(G.ballCoords[2]):
        score[1] += 1

def pointScored():
    if (leftScreenCollide(G.ballCoords[0])) or (rightScreenCollide(G.ballCoords[2])):
        return True

def resetGame():
    t.sleep(1.5)
    S.currentSpeed = S.startingSpeed
    G.rect1Coords = (25, 150, 60, 351)
    G.rect2Coords = (940, 150, 975, 351)
    G.ballCoords = (485, 235, 515, 265)

def gameOver(win_msg):
    G.clearScreen()
    colors = ['red', 'orange', 'green', 'blue', 'purple', 'red', 'orange', 'green', 'blue', 'purple']
    for i in range(10):
        G.canvas.create_text((500, 250), text = win_msg, fill = colors[i], font=('Roboto','50','bold'))
        G.root.update()
        G.canvas.pack()
        t.sleep(.5)

    G.root.destroy()