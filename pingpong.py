from pygame import *
from random import randint
from time import sleep
win = display.set_mode((1000, 500))
bg = transform.scale(image.load("bg.jpg"), (1000, 500))
clock = time.Clock()
font.init()
font = font.SysFont('Arial', 52)


directionx = randint(1, 2)
directiony = randint(1, 2)

text_win1 = font.render('PLAYER 1 WIN!', 3, (255, 255, 255))
text_win2 = font.render("PLAYER 2 WIN!", 3, (255, 255, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed, s_w, s_h, score):
        super().__init__()
        self.score = score
        self.s_w = s_w
        self.s_h = s_h
        self.image = transform.scale(image.load(player_image), (s_w, s_h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self, p):
        k_p = key.get_pressed()
        if p == 'p1':
            if k_p[K_UP] and self.rect.y > 0:
                self.rect.y -= self.speed
            if k_p[K_DOWN] and self.rect.y < 310:
                self.rect.y += self.speed


        if p == 'p2':
            if k_p[K_w] and self.rect.y > 0:
                self.rect.y -= self.speed
            if k_p[K_s] and self.rect.y < 440:
                self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        if directionx == 1:
            self.rect.x += self.speed
        if directionx == 2:
            self.rect.x -= self.speed
        if directiony == 1:
            self.rect.y += self.speed
        if directiony == 2:
            self.rect.y -= self.speed





#экземпляры
p1 = Player('platform.png', 900, 250, 1, 20, 190, 0)
p2 = Player('platform.png', 100, 250, 1, 20, 190, 0)
ball = Ball('ball.png', 250, 250, 1, 30, 30, 0)

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        win.blit(bg, (0, 0))
        p1.reset()
        p1.update('p1')
        p2.reset()
        p2.update('p2')
        ball.reset()
        ball.update()
        if ball.rect.y <= 0 or ball.rect.y >= 470:
            if directiony == 1:
                directiony = 2
            else:
                directiony = 1

        if sprite.collide_rect(p1, ball):
            directionx = 2

        if sprite.collide_rect(p2, ball):
            directionx = 1

        if ball.rect.x - p2.rect.x <= -50:
            p1.score += 1
            sleep(1)
            ball.rect.x = 500
            ball.rect.y = 250
            directionx = randint(1, 2)
            directiony = randint(1, 2)


        if ball.rect.x - p1.rect.x >= 50:
            p2.score += 1
            sleep(1)
            ball.rect.x = 500
            ball.rect.y = 250
            directionx = randint(1, 2)
            directiony = randint(1, 2)

        score_2 = font.render(f"{p2.score}", 1, (255, 255, 255))
        score_1 = font.render(f'{p1.score}', 1, (255, 255, 255))
        win.blit(score_1, (970, 10))
        win.blit(score_2, (10, 10))

        if p1.score >= 5:
            finish = True
            win.blit(text_win1, (500, 250))


        if p2.score >= 5:
            finish = True
            win.blit(text_win2, (500, 250))


        display.update()
clock.tick(15)


