from typing import Any
from pygame import *



# Налаштування ігрової сцени
wmd_width = 1200
wnd_height = 800
wnd = display.set_mode((wmd_width, wnd_height))
display.set_caption('Доганялки')

background = transform.scale(
    image.load('hg.png'), 
    (wmd_width, wnd_height))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load('images1.png'), size)
        self.image1 = transform.scale(image.load('gh .png'), size)
        self.image2 = transform.scale(image.load('jk.png'), size)
        self.image3 = transform.scale(image.load('gey.png'), size)
        self.image4 = transform.scale(image.load('tf.png'), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        wnd.blit(self.image, (self.rect.x, self.rect.y))
    def reset1(self):
        wnd.blit(self.image1, (self.rect.x, self.rect.y))
    def reset2(self):
        wnd.blit(self.image2, (self.rect.x, self.rect.y))
    def reset3(self):
        wnd.blit(self.image3, (self.rect.x, self.rect.y))
    def reset4(self):
        wnd.blit(self.image4, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 1100:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
class Enamy(GameSprite):
    def update(self):
        if self.rect.x <= 30:
            self.directhion = "right"

        if self.rect.x >= 1100 :
            self.directhion = "left"

        if self.directhion == "left":
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_haight):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.haight = wall_haight
        self.image = Surface((self.width, self.haight))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    
    def reset(self):
        wnd.blit(self.image, (self.rect.x, self.rect.y))



mixer.init()
mixer.music.load("satyr.mp3")
mixer.music.play()

finish = False


sprite1 = Player('images.jfif', 400, 700, 20, (100, 100))
sprite2 = Enamy('gh .png', 1100, 700, 10, (100, 100))
sprite3 = GameSprite('jk.png', 30, 30, 400, (100, 100))
win = GameSprite('gey.png', 600, 350, 400, (400, 400))
lose = GameSprite('tf.png', 600, 350, 400, (400, 400))

Wall =   [Wall(12, 23, 34, 130, 200, 30, 500),
    Wall(12, 23, 34, 600, 100, 30, 500),
    Wall(12, 23, 34, 1000, 40, 30, 500),
    Wall(12, 23, 34, 800, 40, 500, 30),
    Wall(12, 23, 34, 280, 200, 600, 30),
    Wall(12, 23, 34, 100, 400, 350, 30)]
# Основний цикл гри
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    wnd.blit(background, (0, 0))

    if finish != True:
        sprite1.reset()
        sprite2.reset2()
        sprite3.reset2()
        for wall in Wall:
            wall.reset()

        

    sprite1.reset()
    sprite1.update()
    sprite2.reset1()
    sprite2.update()
    sprite3.reset2()

        
    if sprite.collide_rect(sprite1, sprite2):
        win.reset3()
        finish = True

    
    for w in Wall:
        if sprite.collide_rect(sprite1, w):
            win.reset3()
            finish = True
  
            

    if sprite.collide_rect(sprite1, sprite3):
        finish = True
        lose.reset4()

    display.update()
    clock.tick(FPS)