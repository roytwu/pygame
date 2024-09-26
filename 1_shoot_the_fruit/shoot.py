"""
Author:      Roy Wu, Summer Wu
Description: Use Pygame Zero for a apple shooting/clicking game
History:     09/14/2024, initial version
"""

import pgzrun
from random import randint

apple = Actor("apple.png")
mush = Actor("mushroom.png")
ct = 0  #* counter

def draw():
    screen.clear()
    apple.draw()
    mush.draw()

def place_apple():
    apple.x = randint(10, 700)
    apple.y = randint(10, 500)

def place_mush():
    mush.x = randint(10, 500)
    mush.y = randint(10, 300)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        global ct
        ct = ct + 1
        print("Good Shot!")
        place_apple()
    elif mush.collidepoint(pos):
        print("Wrong target!")
        place_mush()
        place_apple()
    else:
        print("Game over, you PeDan!")
        print("Total number of good shots: " + str(ct))
        quit()

place_apple()
pgzrun.go()