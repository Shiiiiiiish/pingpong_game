from pygame import *
win = display.set_mode((1000, 500))
bg = transform.scale(image.load("bg.jpg"), (1000, 500))
clock = time.Clock()




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





#экземпляры
p1 = Player('platform.png', 900, 250, 1, 20, 190, 0)
p2 = Player('platform.png', 100, 250, 1, 20, 190, 0)


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    win.blit(bg, (0, 0))
    p1.reset()
    p1.update('p1')
    p2.reset()
    p2.update('p2')
    display.update()
clock.tick(244)


