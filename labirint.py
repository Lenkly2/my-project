from pygame import *

class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x = self.rect.x - self.speed
        if keys[K_d] and self.rect.x < 700:
            self.rect.x = self.rect.x + self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y = self.rect.y + self.speed
window = display.set_mode((800,600))
picture = transform.scale(image.load('back.jpg'),(800,600))
player = Object('008.jpg',100,400,100,100,5)
bari = Object('010.png',100,200,20,80,1)
clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            
    window.blit(picture,(0,0))
    player.reset()
    player.move()
    bari.reset()
    display.update()
    clock.tick(60)

    
       


    