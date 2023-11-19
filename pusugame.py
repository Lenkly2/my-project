from pygame import *

x = 100
y = 400
sizepx = 150
sizepy = 300
size = (1000,700)
window = display.set_mode((size))
picture = transform.scale(image.load('background.jpg'),(size))
player = transform.scale(image.load('itsuko.png'),(sizepx,sizepy))
player2 = transform.scale(image.load('kurumi.png'),(150,300))
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(picture,(0,0))
    window.blit(player,(x,y))
    player = transform.scale(image.load('itsuko.png'),(sizepx,sizepy))
    key_pressed = key.get_pressed()
    if key_pressed[K_d] and x < 900:
        x = x+5
    if key_pressed[K_a]and x > 0:
        x = x-5
    if key_pressed[K_w] and y > 200:
        y = y-5
        if sizepx > 0:
            sizepx = sizepx-5
        if sizepy > 0:
            sizepy = sizepy-10 
    if key_pressed[K_s] and y < 400:
        y = y+5
        if sizepx > 0:
            sizepx = sizepx+5
        if sizepy > 0:
            sizepy = sizepy+10 
    display.update()
    clock.tick(60)

    
       


    