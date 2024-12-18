from Settings import *
import time as t
from Movement import *
from Graphics import *
from Bot import  *
from Score import *
from Audio import *

if __name__ == '__main__':
    while True:

        t.sleep(S.currentSpeed)

        G.updateSprites(G.rect1Coords, G.rect2Coords, G.ballCoords)

        if isP1UpKey():
                G.rect1Coords = moveUp(*G.rect1Coords)
        elif isP1DownKey():
                G.rect1Coords = moveDown(*G.rect1Coords)

        ballDirection(G.rect1Coords, Bot.rect2Coords, G.ballCoords)

        if direction['right'] == True:
            G.ballCoords = moveRight(*G.ballCoords)
        elif direction['left'] == True:
            G.ballCoords = moveLeft(*G.ballCoords)
        elif direction['upRight'] == True:
            G.ballCoords = moveUpRight(*G.ballCoords)
        elif direction['downRight'] == True:
            G.ballCoords = moveDownRight(*G.ballCoords)
        elif direction['upLeft'] == True:
            G.ballCoords = moveUpLeft(*G.ballCoords)
        elif direction['downLeft'] == True:
            G.ballCoords = moveDownLeft(*G.ballCoords)


        if S.secondPlayer == False:
            if plyrCollide(G.rect1Coords[1], G.rect1Coords[3], G.ballCoords):
                Bot.chooseTargetPortion()

            if not Bot.isBallToTarget():
                if Bot.ballAboveTarget():
                    G.rect2Coords = Bot.moveUp(*G.rect2Coords)
                elif Bot.ballBelowTarget():
                    G.rect2Coords = Bot.moveDown(*G.rect2Coords)
        else:
            if isP2UpKey():
                G.rect2Coords = Bot.moveUp(*G.rect2Coords)
            elif isP2DownKey():
                G.rect2Coords = Bot.moveDown(*G.rect2Coords)

        updateScore()

        if pointScored():
            if score[0] == S.scoreLimit:
                mainGame = False
                gameOver(S.Player1WinMessage)
            elif score[1] == S.scoreLimit:
                mainGame = False
                gameOver(S.Player2WinMessage)
            
            resetGame()
        G.root.update()
        G.clearScreen()

'''
CURRENT ERROR:
Nothing:)

SOLUTION:
Don't break it
'''