class Settings:
    setup = []
    def __init__(self, scoreLimit, secondPlayer, startingSpeed, speedIncrementor, ballSpeed, barSpeed, player1BarColor, player2BarColor, ballColor, textColor, backgroundColor, Player1WinMessage, Player2WinMessage, backgroundMusic, winMusic, sfx):
        self.scoreLimit = int(scoreLimit)
        self.secondPlayer = secondPlayer
        self.startingSpeed = float(startingSpeed)
        self.currentSpeed = float(startingSpeed)
        self.speedIncrementor = float(speedIncrementor)
        self.ballSpeed = int(ballSpeed)
        self.barSpeed = int(barSpeed)
        self.stopBarTop = 0
        self.stopBarBottom = 506 if barSpeed == 5 else 501
        self.plyr1BallCollide = 60 if ballSpeed == 5 else 55
        self.plyr2BallCollide = 940 if ballSpeed == 5 else 955
        self.topScreenCollide = 0 if ballSpeed == 5 else -5
        self.bottomScreenCollide = 500 if ballSpeed == 5 else 505
        self.player1BarColor = player1BarColor
        self.player2BarColor = player2BarColor
        self.ballColor = ballColor
        self.textColor = textColor
        self.backgroundColor = backgroundColor
        self.Player1WinMessage = Player1WinMessage
        self.Player2WinMessage = Player2WinMessage
        self.backgroundMusic = backgroundMusic
        self.winMusic = winMusic
        self.sfx = sfx

        if self.secondPlayer == 'True':
            self.secondPlayer = True
        else:
            self.secondPlayer = False
        
        if self.backgroundMusic == 'False':
            self.backgroundMusic = False
        if self.winMusic == 'False':
            self.winMusic = False
        if self.sfx == 'True':
            self.sfx = False
        else:
            self.sfx = True

    @classmethod
    def setupSettings(cls):
        with open('Settings/Settings.txt') as s:
            for line in s.readlines():
                for char in line:
                    if char =='>':
                        Settings.setup.append(line[28:-1])
    
    def incrementor(self):
        if self.currentSpeed - self.speedIncrementor >= 0:
            self.currentSpeed -= self.speedIncrementor
        else:
            pass




Settings.setupSettings()
S = Settings(*Settings.setup)