import pgzrun
from random import randint

WIDTH = 900
HEIGHT = 600
score = 0
game_over = False

peach = Actor("princess_100.png")
mush = Actor("mushroom.png")

peach.pos = 100, 100
mush.pos = 200, 200 

def draw():
    screen.fill("black")
    peach.draw()
    mush.draw()
    screen.draw.text("Score: "+ str(score), color = "green", topleft = (10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: "+ str(score), 
                         color = "green", topleft = (10, 10), fontsize = 60)

def place_mush():
    mush.x = randint(20, (WIDTH-20))
    mush.y = randint(20, (HEIGHT-20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    step_size = 6

    if keyboard.left:
        peach.x = peach.x - step_size
        if peach.x <= 0:
            peach.x = WIDTH
    elif keyboard.right:
        peach.x = peach.x + step_size
        if peach.x >= WIDTH:
            peach.x =0
    elif keyboard.up:
        peach.y = peach.y - step_size
        if peach.y <= 0:
            peach.y = HEIGHT
    elif keyboard.down:
        peach.y = peach.y + step_size
        if peach.y >= HEIGHT:
            peach.y = 0
    
    mush_get = peach.colliderect(mush)

    if mush_get == True:
        score = score + 10
        place_mush()


clock.schedule(time_up, 20.0)
place_mush()
pgzrun.go()
