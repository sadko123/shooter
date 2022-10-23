#Создай собственный Шутер!

from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_size, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.speed = sprite_speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):

        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y < window_hight - sprite_hight:
            self.rect.y += self.speed
        if key_pressed[K_DOWN] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < window_widht - sprite_widht:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= window_widht * 3 / 4:
            self.direction = 'right'
        if self.rect.x >= window_widht - sprite_widht:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



window_widht = 700
window_hight = 500
sprite_widht = 50
sprite_hight = 50

clock = time.Clock()

FPS = 60

mixer.init()
mixer.music.load('music/space.ogg')
mixer.music.play()

window = display.set_mode((700, 500))

background = image.load('images/galaxy.jpg')
background = transform.scale(background, (700, 500))

run = True
finish = False

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    
        window.blit(background, (0,0))
    
        display.update()
        clock.tick(FPS)
   