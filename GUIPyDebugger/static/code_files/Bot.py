from random import *
from Colliders import *
from Graphics import *

class Bot(Graphics):
    targetPortion = {'top':False, 'mid':False, 'low':False}
    rect2Coords = G.rect2Coords
        # self.targetPortion = {'top':False, 'mid':False, 'low':False}

    def moveUp(self, left, top, right, bottom):
        if top != S.stopBarTop:
            left = left
            top -= S.barSpeed
            right = right
            bottom -= S.barSpeed
            Bot.rect2Coords = (left, top, right, bottom)
        return (left, top, right, bottom)

    def moveDown(self, left, top, right, bottom):
        if bottom != S.stopBarBottom:
            left = left
            top += S.barSpeed
            right = right
            bottom += S.barSpeed
            Bot.rect2Coords = (left, top, right, bottom)
        return (left, top, right, bottom)
    
    def chooseTargetPortion(self):
        for portion in self.targetPortion:
            self.targetPortion[portion] = False
        targetKeys = list(self.targetPortion.keys())
        self.targetPortion[targetKeys[randint(0, 2)]] = True
        return self.targetPortion
    
    @classmethod
    def ballCenter(self, ballCoords = G.ballCoords):
        return avg(G.ballCoords[1], ballCoords[3])
    
    def isBallToTarget(self):
        ballCenter = Bot.ballCenter(self.ballCoords)
        if self.targetPortion['top']:
            barCoords = botBarDivider(self.rect2Coords, 'u')
            return ballCenter in range(barCoords[0], barCoords[1])
        elif self.targetPortion['mid']:
            barCoords = botBarDivider(self.rect2Coords, 'm')
            return ballCenter in range(barCoords[0], barCoords[1])
        elif self.targetPortion['low']:
            barCoords = botBarDivider(self.rect2Coords, 'l')
            return ballCenter in range(barCoords[0], barCoords[1])
        
    def ballAboveTarget(self):
        ballCenter = Bot.ballCenter(self.ballCoords)
        if self.targetPortion['top']:
            barCoords = botBarDivider(self.rect2Coords, 'u')
            return ballCenter < barCoords[0]
        elif self.targetPortion['mid']:
            barCoords = botBarDivider(self.rect2Coords, 'm')
            return ballCenter < barCoords[0]
        elif self.targetPortion['low']:
            barCoords = botBarDivider(self.rect2Coords, 'l')
            return ballCenter < barCoords[0]

    def ballBelowTarget(self):
        ballCenter = Bot.ballCenter(self.ballCoords)
        if self.targetPortion['top']:
            barCoords = botBarDivider(self.rect2Coords, 'u')
            return ballCenter > barCoords[1]
        elif self.targetPortion['mid']:
            barCoords = botBarDivider(self.rect2Coords, 'm')
            return ballCenter > barCoords[1]
        elif self.targetPortion['low']:
            barCoords = botBarDivider(self.rect2Coords, 'l')
            return ballCenter > barCoords[1]

Bot = Bot()