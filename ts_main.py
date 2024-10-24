from graphics import *
# from drawsvg import *
import drawsvg as draw

import chess
# import taiwan.svg


class Ts:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def main(self):
        win = GraphWin('Face', 800, 600) # give title and dimensions
        #win.yUp() # make right side up coordinates!

        head = Circle(Point(40,100), 25) # set center and radius
        head.setFill("yellow")
        head.draw(win)

        eye1 = Circle(Point(30, 105), 5)
        eye1.setFill('blue')
        eye1.draw(win)

        eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
        eye2.setWidth(3)
        eye2.draw(win)

        mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
        mouth.setFill("red")
        mouth.draw(win)

        label = Text(Point(100, 120), 'A face')
        label.draw(win)

        message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
        message.draw(win)

        d = draw.Drawing(200, 100, origin='center')
        d.append(draw.Lines(-80, 45,
                            70, 49,
                            95, -49,
                            -90, -40,
                            close=False,
                            fill='#eeee00',
                            stroke='black'))



        win.getMouse()
        win.close()


if __name__ == '__main__':
    my_Ts = Ts()
    my_Ts.main()
    print("I'm a Ts")
    while True:
        action = input("Q").upper()
        if action not in "ABOS" or len(action) != 1:
            print("error")
            continue
        if action == 'A':
            my_Ts.accelerate()
            print("Accerlate...")
        my_Ts.step()
