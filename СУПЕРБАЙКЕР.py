
from tkinter import *

import time
import random

tk = Tk()
tk.title('$уперБАЙКЕР 3Д БЕсплатно')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400, highlightthickness=0)
# every elements has own coordinates
canvas.pack()
# just an update of pole
tk.update()

class Ball:
    def __init__(self, canvas, paddle, score, color):

        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        # create circle in command line r=15, color = needed color
        self.id = canvas.create_oval(10,10, 25, 25, fill=color)
        # start of dot
        self.canvas.move(self.id, 245, 100)
        # every available directions
        starts = [-2, -1, 1, 2]
        # randomize
        random.shuffle(starts)
        # choose 1st of randomized spots
        self.x = starts[0]
        # firstly ball falls down, so we decrease value on axis oY
        self.y = -2
        # ball finds out his scales
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # checking for touching the bottom. While no, value = false
        self.hit_bottom = False
    # proceses touching plat(platform, yea, im just a little bit stupid)
    def hit_paddle(self, pos):
        # get coordinates
        paddle_pos = self.canvas.coords(self.paddle.id)
        # if coords of touching are same as coords of plat
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                # increase score
                self.score.hit()
                # return  mark that we successful touched
                return True
        # if there was no touching return false
        return False
    # moving of ball
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        # write in memory new coords of ball
        pos = self.canvas.coords(self.id)
        # if ball falls from above
        if pos[1] <= 0:
            # stamping falling in the next step = 2
            self.y = 2
        # if ball touching bottom with R Low angle(lol, angle)
        if pos[3] >= self.canvas_height:
            # marks it with separate variable
            self.hit_bottom = True
            # writing out message and number of score
            canvas.create_text(250, 120, text='Ну ты не байкер ни разу', font=('Courier', 12), fill='red')
        # if there was touching
        if self.hit_paddle(pos) == True:
            # move ball at the top
            self.y = -2
        # if touched left wall
        if pos[0] <= 0:
            # moving right
            self.x = 2
        # if touched right wall
        if pos[2] >= self.canvas_width:
            # moving left
            self.x = -2

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # list of possible plot's locations
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(start_1)
        self.starting_point_x = start_1[0]
        # moving plat to the staring point
        self.canvas.move(self.id, self.starting_point_x, 300)
        # while plat is not moving
        self.x = 0
        # plat finds out it width
        self.canvas_width = self.canvas.winfo_width()
        # creating obrabptchik najatiy
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        # while game is not started we are waiting
        self.started = False
        # when player push Enter - it get started
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
    def turn_right(self, event):
        # move in 2 pixels by oX right
        self.x = 2
    def turn_left(self, event):
        # left
        self.x = -2
    def start_game(self, event):
        self.started = True
    def draw(self):
        # move plat on definite amount of pixels
        self.canvas.move(self.id, self.x, 0)
        # gets coords of pole
        pos = self.canvas.coords(self.id)
        # if we stuck in left wall
        if pos[0] <= 0:
            # stop
            self.x = 0
        # if stuck in right wall
        elif pos[2] >= self.canvas_width:
            # stop
            self.x = 0

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)
score = Score(canvas, 'green')
paddle = Paddle(canvas, 'White')
ball = Ball(canvas, paddle, score, 'red')
while not ball.hit_bottom:
    if paddle.started == True:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
time.sleep(3)
