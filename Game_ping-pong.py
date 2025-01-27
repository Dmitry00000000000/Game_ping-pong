from pygame import *
window = display.set_mode((700,500))
window.fill((71,221,254))
GAME = True
FPS = 60
clock = time.Clock()

while GAME:
    for e in event.get():
        if e.type == QUIT:
            GAME = False
    clock.tick(FPS)
    display.update()

        