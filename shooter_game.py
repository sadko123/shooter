#Создай собственный Шутер!

from pygame import *
from random import *


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
        bullet = Bullet(bullet_image, self.rect.centerx, self.rect.top, (bullet_widht, bullet_hight), 10 )
        bullet_group.add(bullet)

class Enemy(GameSprite):
    def update(self):
       self.rect.y += self.speed
       if self.rect.y >= window_hight:
           self.rect.x = randint(0, window_widht - vrag_widht)
           self.rect.y = 0
           global lost_vrag
           lost_vrag += 1



    
        
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y - bullet_hight <= 0:
            self.kill()


window_widht = 700
window_hight = 500

ship_hight = 80
ship_wight = 40
ship_start_x = window_widht / 2
ship_start_y = window_hight - ship_hight - 5

vrag_hight = 80
vrag_widht = 40
vrag_start_y = 0

bullet_hight = 10
bullet_widht = 5



clock = time.Clock()

FPS = 60

lost_vrag = 0

def_vrag = 0

mixer.init()
mixer.music.load('music/space.ogg')
mixer.music.play()

window = display.set_mode((700, 500))

background = image.load('images/galaxy.jpg')
background = transform.scale(background, (700, 500))

ship_image = 'images/rocket.png'
vrag_image = 'images/ufo.png'
bullet_image = 'images/bullet.png'

font.init()
font1 = font.Font (None, 40)
font2 = font.Font (None, 40)
win = font2.render('Вы выиграли' , True , (255, 215,0))
lose = font2.render('Вы проиграли' , True , (255, 215,0))

win_text = font1.render('Пропущенно: ' + str(lost_vrag), 1 , (255, 215,0))
win_text2 = font2.render('Счёт:' + str(def_vrag), 1, (150, 150, 0))

space_ship = Player(ship_image, ship_start_x, ship_start_y, (ship_wight, ship_hight), 10 )

monsters = sprite.Group()

for i in range(5):
    vrag_x = randint(0, window_widht - ship_wight)
    vrag_speed = randint(1, 4) 
    vrag = Enemy(vrag_image, vrag_x, vrag_start_y, (vrag_widht, vrag_hight), vrag_speed)
    monsters.add(vrag)

bullet_group = sprite.Group()



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
        monsters.update()
        bullet_group.update()
        
        window.blit(background, (0,0))
        win_text = font1.render('Пропущенно: ' + str(lost_vrag), 1 , (255, 215,0))
        
        window.blit(win_text, (10, 100))
        


        space_ship.reset()
        monsters.draw(window)
        bullet_group.draw(window)

        if sprite.spritecollide(space_ship, monsters, False):
            print('проиграли')
            window.blit(lose, (250, 350))
            finish = True
            
        dead_vrag_list = sprite.groupcollide(monsters, bullet_group, True, True)

        for monster in dead_vrag_list:
            def_vrag += 1
            print(def_vrag)
            win_text2 = font1.render('Счёт:' + str(def_vrag), 1, (150, 150, 0))
            vrag_x = randint(0, window_widht - ship_wight)
            vrag_speed = randint(1, 4) 
            vrag = Enemy(vrag_image, vrag_x, vrag_start_y, (vrag_widht, vrag_hight), vrag_speed)
            monsters.add(vrag)

        if def_vrag >= 5:
            print('выиграли')
            window.blit(win, (250, 350))
            finish = True
            
        
        display.update()
        clock.tick(FPS)
   