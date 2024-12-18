from Settings import *
from Audio import *
from Graphics import *
def avg(y1, y2):
    return (y1 + y2) / 2

def leftScreenCollide(leftBallCoord):
    return leftBallCoord >= 1000

def rightScreenCollide(rightBallCoord):
    return rightBallCoord <= 0

def plyrBarDivider(plyrBarCoords, portion = 'full'):
    sectSize = (plyrBarCoords[3] - plyrBarCoords[1]) / 3
    if portion == 'u':
        return [int(plyrBarCoords[1]), int(sectSize + plyrBarCoords[1])]
    elif portion == 'm':
        return [int(plyrBarCoords[1] + sectSize), int(plyrBarCoords[3] - sectSize)]
    elif portion == 'l':
        return [int(plyrBarCoords[3] - sectSize), int(plyrBarCoords[3])]
    else:
        return [plyrBarCoords[1], plyrBarCoords[3]]

def botBarDivider(botBarCoords, portion = 'full'):
    sectSize = (botBarCoords[3] - botBarCoords[1]) / 3
    if portion == 'u':
        return [int(botBarCoords[1]), int(botBarCoords[1] + sectSize)]
    elif portion == 'm':
        return [int(botBarCoords[1] + sectSize), int(botBarCoords[3] - sectSize)]
    elif portion == 'l':
        return int(botBarCoords[3] - sectSize), int(botBarCoords[3])
    else:
        return [botBarCoords[1], botBarCoords[3]]
    
def plyrCollideUpper(plyrUpperBottom, plyrUpperTop, ballCoords):
    if ballCoords[0] <= S.plyr1BallCollide:
        S.incrementor()
        return avg(ballCoords[1], ballCoords[3]) in range(plyrUpperBottom, plyrUpperTop)

def plyrCollideMid(plyrMidBottom, plyrMidTop, ballCoords):
    if ballCoords[0] <= S.plyr1BallCollide:
        S.incrementor()
        return avg(ballCoords[1], ballCoords[3]) in range(plyrMidBottom, plyrMidTop)

def plyrCollideLower(plyrLowerBottom, plyrLowerTop, ballCoords):
    if ballCoords[0] <= S.plyr1BallCollide:
        S.incrementor()
        return avg(ballCoords[1], ballCoords[3]) in range(plyrLowerBottom, plyrLowerTop)

def botCollideUpper(botUpperBottom, botUpperTop, ballCoords):
    if ballCoords[2] >= S.plyr2BallCollide:
        S.incrementor()
        return avg(ballCoords[1], ballCoords[3]) in range(botUpperBottom, botUpperTop)

def botCollideMid(botMidBottom, botMidTop, ballCoords):
    if ballCoords[2] >= S.plyr2BallCollide:
        S.incrementor()
        return avg(ballCoords[1], ballCoords[3]) in range(botMidBottom, botMidTop)

def botCollideLower(botLowerBottom, botLowerTop, ballCoords):
    if ballCoords[2] >= S.plyr2BallCollide:
        S.incrementor()
        return avg(ballCoords[1], ballCoords[3]) in range(botLowerBottom, botLowerTop)

def plyrCollide(plyrBottom, plyrTop, ballCoords):
    if ballCoords[0] <= S.plyr1BallCollide:
        return avg(ballCoords[1], ballCoords[3]) in range(plyrBottom, plyrTop)

def botCollide(botBottom, botTop, ballCoords):
    if ballCoords[2] >= S.plyr2BallCollide:
        return avg(ballCoords[1], ballCoords[3]) in range(botBottom, botTop)

def topScreenCollide(topBallCoord):
    if topBallCoord == S.topScreenCollide:
        S.incrementor()
        return True

def bottomScreenCollide(bottomBallCoord):
    if bottomBallCoord == S.bottomScreenCollide:
        S.incrementor()
        return True