import keyboard as key
from Colliders import *
from Graphics import *
from Settings import *

direction = {'right':True, 'left':False, 'upRight':False, 'downRight':False, 'upLeft':False, 'downLeft':False}

#Players bar movement
def isP1UpKey():
    return key.is_pressed('w')

def isP1DownKey():
    return key.is_pressed('s')

def isP2UpKey():
    return key.is_pressed('up')

def isP2DownKey():
    return key.is_pressed('down')

def moveUp(left, top, right, bottom):
    if top != S.stopBarTop:
        left = left
        top -= S.barSpeed
        right = right
        bottom -= S.barSpeed
    return (left, top, right, bottom)

def moveDown(left, top, right, bottom):
    if bottom != S.stopBarBottom:
        left = left
        top += S.barSpeed
        right = right
        bottom += S.barSpeed
    return (left, top, right, bottom)

#Ball movement
def directionReset(direction, newDirection):
    for i in direction:
        direction[i] = False
    direction[newDirection] = True

def moveRight(left, top, right, bottom):
    left += S.ballSpeed
    top = top
    right += S.ballSpeed
    bottom = bottom
    return (left, top, right, bottom)

def moveLeft(left, top, right, bottom):
    left -= S.ballSpeed
    top = top
    right -= S.ballSpeed
    bottom = bottom
    return (left, top, right, bottom)

def moveUpRight(left, top, right, bottom):
    left += S.ballSpeed
    top -= S.ballSpeed
    right += S.ballSpeed
    bottom -= S.ballSpeed
    return (left, top, right, bottom)

def moveDownRight(left, top, right, bottom):
    left += S.ballSpeed
    top += S.ballSpeed
    right += S.ballSpeed
    bottom += S.ballSpeed
    return (left, top, right, bottom)

def moveUpLeft(left, top, right, bottom):
    left -= S.ballSpeed
    top -= S.ballSpeed
    right -= S.ballSpeed
    bottom -= S.ballSpeed
    return (left, top, right, bottom)

def moveDownLeft(left, top, right, bottom):
    left -= S.ballSpeed
    top += S.ballSpeed
    right -= S.ballSpeed
    bottom += S.ballSpeed
    return (left, top, right, bottom)

def ballDirection(plyrBarCoords, botBarCoords, ballCoords):
    plyrUpper = plyrBarDivider(plyrBarCoords, 'u')
    plyrMid = plyrBarDivider(plyrBarCoords, 'm')
    plyrLower = plyrBarDivider(plyrBarCoords, 'l')
    botUpper = botBarDivider(botBarCoords, 'u')
    botMid = botBarDivider(botBarCoords, 'm')
    botLower = botBarDivider(botBarCoords, 'l')

    if botCollideUpper(*botUpper, ballCoords):
        directionReset(direction, 'upLeft')
    elif botCollideMid(*botMid, ballCoords):
        directionReset(direction, 'left')
    elif botCollideLower(*botLower, ballCoords):
        directionReset(direction, 'downLeft')
    elif plyrCollideUpper(*plyrUpper, ballCoords):
        directionReset(direction, 'upRight')
    elif plyrCollideMid(*plyrMid, ballCoords):
        directionReset(direction, 'right')
    elif plyrCollideLower(*plyrLower, ballCoords):
        directionReset(direction, 'downRight')
    elif topScreenCollide(ballCoords[1]):
        if direction['upRight'] == True:
            directionReset(direction, 'downRight')
        elif direction['upLeft'] == True:
            directionReset(direction, 'downLeft')
    elif bottomScreenCollide(ballCoords[3]):
        if direction['downRight'] == True:
            directionReset(direction, 'upRight')
        elif direction['downLeft'] == True:
            directionReset(direction, 'upLeft')
'''
Debugging lol:
    print('player Upper', plyrUpper)
    print('player Middle', plyrMid)
    print('player Lower', plyrLower)
    print('bot Upper', botUpper)
    print('bot Mid', botMid)
    print('bot Lower', botLower)
    print('ball coordinates', ballCoords[0], ballCoords[1], ballCoords[2], ballCoords[3])
    print('bot upper collider', botCollideUpper(botUpper[0], botUpper[1], ballCoords))
    print('bot mid collider', botCollideMid(botMid[0], botMid[1], ballCoords))
    print('bot lower collider', botCollideLower(botLower[0], botLower[1], ballCoords))
    print('player upper collider', plyrCollideUpper(plyrUpper[0], plyrUpper[1], ballCoords))
    print('player mid collider', plyrCollideMid(plyrMid[0], plyrMid[1], ballCoords))
    print('player lower collider', plyrCollideLower(plyrLower[0], plyrLower[1], ballCoords))
    print('bot bar collider', botCollide(bot[0], bot[1], ballCoords))
    print('player bar collider', plyrCollide(plyr[0], plyr[1], ballCoords))
    print('top screen collider', topScreenCollide(ballCoords[1]))
    print('bottom screen collider', bottomScreenCollide(ballCoords[3]))
'''