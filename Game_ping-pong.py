from pygame import *
window = display.set_mode((700,500))
window.fill((71,221,254))
GAME = True
FPS = 60
clock = time.Clock()
speed = 5
counter_Blue = 0
counter_Red = 0
finish = False
mixer.init()
mixer.music.load('song.ogg')
mixer.music.play()
sound1 = mixer.Sound('sound.ogg')
sound1.set_volume(0.5)

class Racket(sprite.Sprite):
    def __init__(self,width,height,speed,x,y,color):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height
        self.speed = speed
        self.image = Surface((self.width,self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def move1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < 345:
            self.rect.y += self.speed
    def reset(self):
        draw.rect(window,self.color,self.rect)

class Ball(sprite.Sprite):
    def __init__(self,ball_image,width,height,speed_x,speed_y,x,y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(ball_image),(self.width,self.height))
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def move(self):
        self.rect.y -= self.speed_y
        self.rect.x -= self.speed_x
        if self.rect.y <= 5:
            self.speed_y *= -1
        if self.rect.y >= 445:
            self.speed_y *= -1
    def move1(self,racket1,racket2):
        if sprite.collide_rect(self,racket1):
            sound1.play()
            self.speed_x *= -1
        if sprite.collide_rect(self,racket2):
            sound1.play()
            self.speed_x *= -1
            

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
        
ball = Ball('tenis_ball.png',50,50,5,5,300,225)
racket1 = Racket(5,150,5,5,150,(0,0,255))
racket2 = Racket(5,150,5,690,150,(255,0,0))
font.init()
font1 = font.SysFont('arial', 70)
font2 = font.SysFont('arial', 30)
Blue_win = font1.render('Blue win', 1 ,(0,0,230))
Red_win = font1.render('Red win', 1 ,(230,0,0))

while GAME:
    for e in event.get():
        if e.type == QUIT:
            GAME = False
    if finish != True:
        window.fill((71,221,254))
        counter_Blue1 = font2.render('Points: ' + str(counter_Blue),1,(255,255,255))
        counter_Red1 = font2.render('Points: ' + str(counter_Red),1,(255,255,255))
        if counter_Blue >= 10:
            window.blit(Blue_win,(200,225)) 
            finish = True
        if counter_Red >= 10:
            window.blit(Red_win,(200,225))
            finish = True
        if ball.rect.x >= 700:
            ball.rect.y = 200
            ball.rect.x = 300
            counter_Blue +=1
        if ball.rect.x <= 0:
            ball.rect.y = 200
            ball.rect.x = 300
            counter_Red +=1
        window.blit(counter_Blue1,(5,5))
        window.blit(counter_Red1, (580,5))       
        racket1.move1()
        racket2.move2()
        ball.move()
        ball.move1(racket1,racket2)
        ball.reset()
        racket1.reset()
        racket2.reset()
    clock.tick(FPS)
    display.update()   
