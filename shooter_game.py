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

        if key_pressed[K_RIGHT] and self.rect.x < window_widht - ship_wight:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
    
    def shoot(self):
        
        print('стреляю')

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

ship_hight = 80
ship_wight = 40
ship_start_x = window_widht / 2
ship_start_y = window_hight - ship_hight - 5



clock = time.Clock()

FPS = 60

mixer.init()
mixer.music.load('music/space.ogg')
mixer.music.play()

window = display.set_mode((700, 500))

background = image.load('images/galaxy.jpg')
background = transform.scale(background, (700, 500))

ship_image = 'images/rocket.png'



space_ship = Player(ship_image, ship_start_x, ship_start_y, (ship_wight, ship_hight), 10 )




run = True
finish = False

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                space_ship.shoot()
    
    if not finish:
        space_ship.update()
        
        window.blit(background, (0,0))
    
        space_ship.reset()

        display.update()
        clock.tick(FPS)
   