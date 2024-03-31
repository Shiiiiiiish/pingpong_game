from pygame import *
win = display.set_mode((1000, 500))
bg = transform.scale(image.load("bg.jpg"), (1000, 500))





game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(bg, (0, 0))
    display.update()


