import tkinter as tk
from tkinter import Canvas
from Settings import *

class Graphics:
    root = tk.Tk()
    canvas = Canvas(root, bg = S.backgroundColor, height = 500, width = 1000)
    root.title('Pong')

    def __init__(self):
        self.rect1Coords = (25, 150, 60, 351)
        self.rect2Coords = (940, 150, 975, 351)
        self.ballCoords = (485, 235, 515, 265)

    def updateSprites(self, rect1Coords, rect2Coords, ballCoords):
        from Score import score
        self.canvas.create_rectangle(self.rect1Coords, fill = S.player1BarColor)
        self.canvas.create_rectangle(self.rect2Coords, fill = S.player2BarColor)
        self.canvas.create_oval(self.ballCoords, fill = S.ballColor)
        self.canvas.create_text((500, 25), text = f'{score[0]}:{score[1]}', fill = S.textColor, font=('Roboto','30','bold'))
        self.canvas.pack()
    
    def clearScreen(self):
        self.canvas.delete('all')


G = Graphics()