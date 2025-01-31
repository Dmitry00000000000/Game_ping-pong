from pygame import *
window = display.set_mode((700,500))
window.fill((71,221,254))
GAME = True
FPS = 60
clock = time.Clock()

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
        if keys[K_s] and self.rect.y < 475:
            self.rect.y += self.speed
    def move2(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < 475:
            self.rect.y += self.speed
    def reset(self):
        draw.rect(window,self.color,self.rect)

class Ball(sprite.Sprite):
    def __init__(self,ball_image,width,height,speed,x,y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(ball_image),(self.width,self.height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def move(self):
        self.rect.x -= self.speed
        self.rect.y -= self.speed
        if self.rect.y <= 5:
            self.rect.y += self.speed
        if self.rect.y >= 445:
            self.rect.y -= self.speed
    def move1(self,racket1,racket2):
        if sprite.collide_rect(self,racket1):
            self.rect.x += self.speed
        if sprite.collide_rect(self,racket2):
            self.rect.x -= self.speed

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

ball = Ball('images.jpg',50,50,5,300,250)
racket1 = Racket(20,200,5,5,150,(0,0,255))
racket2 = Racket(20,200,5,675,150,(255,0,0))


while GAME:
    window.fill((71,221,254))
    for e in event.get():
        if e.type == QUIT:
            GAME = False
    racket1.move1()
    racket2.move2()
    ball.move()
    ball.move1(racket1,racket2)
    ball.reset()
    racket1.reset()
    racket2.reset()
    clock.tick(FPS)
    display.update()   
