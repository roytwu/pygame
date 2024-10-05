"""
Author:      Roy Wu, Summer Wu
Description: Draw a line between two dots/stars
History:     10/01/2024, initial version
             10/05/2024, add a stopwatch to the game, 
                         it times how long does a player connect all the dots
"""
import pgzrun
import time
from random import randint

WIDTH  = 500
HEIGHT = 300
space  = 25 #* related to the size of the dot
game_over = False

dots  = []
lines = []

next_dot   = 0
total_dot  = 6  #* total dot/star in the game
final_time = 0
start_time = time.time()
stopwatch = False


for cir in range(0, total_dot):
    #* draw dot and star alternatively
    if cir%2 == 0:
        actor = Actor("dot.png")
    else:
        actor = Actor("star.png")

    actor.pos = randint(space, (WIDTH-space)),\
        randint(space, (HEIGHT-space))
    dots.append(actor)
    
# print(len(dots))

def draw():
    global final_time
    global stopwatch
    screen.fill("black")
    number = 1

    for cir in dots:
        screen.draw.text(str(number), \
                         (cir.pos[0], cir.pos[1]+18))
        cir.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (200, 200, 200))

    if game_over:
        screen.fill("linen")
        end_time = time.time()
        total_time = end_time-start_time

        #* record the final time and stop the stopwatch
        if stopwatch == False:
            final_time = total_time
            final_time = round(final_time, 5)
            stopwatch = True
        
        string = "Time is... " + str(final_time) + " seconds."
        screen.draw.text(string, color = "black", topleft = (10, 10))
    
def update():
    pass    
    
def on_mouse_down(pos):
    global next_dot
    global lines
    global game_over

    if dots[next_dot].collidepoint(pos):
        print("Ouch!")
        print(next_dot)

        #* if the dot being clicked is not the 0-th dot
        if bool(next_dot):
            previous = dots[next_dot - 1].pos
            current  = dots[next_dot].pos
            lines.append((previous, current))
        next_dot = next_dot + 1

        if next_dot == total_dot:
            game_over= True
            
    else:
        lines = []
        next_dot = 0
pgzrun.go()