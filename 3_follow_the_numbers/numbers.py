import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 500
space = 20 #* related to the size of the dot

dots = []
lines = []

next_dot = 0

for cir in range(0, 10):
    actor = Actor("dot.png")

    actor.pos = randint(space, (WIDTH-space)),\
        randint(space, (HEIGHT-space))
    
    dots.append(actor)
    
print(len(dots))

def draw():
    screen.fill("black")
    number = 1

    for cir in dots:
        screen.draw.text(str(number), \
                         (cir.pos[0], cir.pos[1]+12))
        
        cir.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (0, 0, 100))

pgzrun.go()