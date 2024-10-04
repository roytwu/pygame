import pgzrun
from random import randint
from time   import time

WIDTH = 500
HEIGHT = 300
space = 25 #* related to the size of the dot
game_over = False

dots = []
lines = []

next_dot = 0
total_dot =5

def update():
    pass

for cir in range(0, total_dot):
    if cir%2 == 0:
        actor = Actor("dot.png")
    else:
        actor = Actor("star.png")

    actor.pos = randint(space, (WIDTH-space)),\
        randint(space, (HEIGHT-space))
    
    dots.append(actor)
    
# print(len(dots))

def draw():
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
        # screen.fill("white")
        # total_time = end_time-start_time
        string = "Time is... " + str(time())
        screen.draw.text(string, color = "red", topleft = (10, 10))
    
    
    
def on_mouse_down(pos):
    global next_dot
    global lines
    global game_over

    if dots[next_dot].collidepoint(pos):
        print("Ouch!")
        print(next_dot)
        if bool(next_dot):
            previous = dots[next_dot - 1].pos
            current = dots[next_dot].pos
            lines.append((previous, current))
        next_dot = next_dot + 1

        if next_dot == total_dot:
            game_over= True
            
    else:
        lines = []
        next_dot = 0
pgzrun.go()