from pygame import *
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height


        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))


        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y


    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.w = w
        self.h = h
        self.image = transform.scale(image.load(player_image),(self.w,self.h))
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
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3):
                self.rect.x = self.rect.x + self.speed
        if keys[K_d] and self.rect.x < 750:
            self.rect.x = self.rect.x + self.speed
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3):
                self.rect.x = self.rect.x - self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y = self.rect.y - self.speed
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3):
                self.rect.y = self.rect.y + self.speed
        if keys[K_s] and self.rect.y < 550:
            self.rect.y = self.rect.y + self.speed
            if sprite.collide_rect(player,wall) or sprite.collide_rect(player,wall2) or sprite.collide_rect(player,wall3):
                self.rect.y = self.rect.y - self.speed

        

    direction = 'right'
    direction1 = "right"
    def move2(self):
        if self.rect.x == 650:
            self.direction = 'right'
        elif self.rect.x == 750:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += 1
        if self.direction == 'left':
            self.rect.x -= 1
        if self.direction == 'stop':
            self.rect.x +=0
    
    def move3(self):
        if self.rect.x == 0:
            self.direction1 = 'right'
        if self.rect.x == 1000:
            self.direction1 = 'left'

        if self.direction1 == 'right':
            self.rect.x += 1
        if self.direction1 == 'left':
            self.rect.x += 1
        if self.direction1 == 'stop':
            self.rect.x +=0

window = display.set_mode((800,600))
picture = transform.scale(image.load('background.jpg'),(800,600))
player = Object('hero.png',100,400,50,50,5)
enemy = Object('cyborg.png',650,400,50,50,5)
gover = Object('gover.png',0,0,800,600,0)
gwin = Object('win.png',0,0,800,600,0)
gold = Object('fgold.png',700,500,50,50,0)
coin = Object('coin.png',400,500,50,50,0)
nxlevel = transform.scale(image.load('nlvv.jpg'),(200,100))
restart = transform.scale(image.load('restart.png'),(200,100))
wall = Wall(255,0,0,400,0,50,400)
wall2 = Wall(255,0,0,200,200,50,400)
wall3 = Wall(255,0,0,600,200,50,400)

clock = time.Clock()
level = 1
coin_count = 0
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if level == 1:
        window.blit(picture,(0,0))
        enemy.image = transform.scale(image.load("cyborg.png"),(50,50))
        
        coin.reset()
        player.reset()
        player.move()
        enemy.reset()
        enemy.move2()
        if coin_count >= 1:
            gold.reset()
        wall.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()

        if sprite.collide_rect(player,coin):
            coin_count += 1
            coin.rect.x = 1000


        if sprite.collide_rect(player,enemy):
            player.speed = 0
            if player.speed == 0:
                gover.reset()
            enemy.direction = 'stop'
            window.blit(restart,(0,0))

            if restart.get_rect().collidepoint(mouse.get_pos()):
                player.speed = 5
                player.rect.x = 100
                player.rect.y = 400
                enemy.direction = 'right'
                player.reset()
                
        if coin_count >= 1: 
            if sprite.collide_rect(player,gold):
                player.speed = 0
                if player.speed == 0:
                    gwin.reset()
                
                window.blit(nxlevel,(0,0))
                if nxlevel.get_rect().collidepoint(mouse.get_pos()):
                    player.speed = 5
                    level = 2
                    player.rect.x = 100
                    player.rect.y = 400
                    coin_count = 0
                    coin.rect.x = 400

    if level == 2:
        window.blit(picture,(0,0))
        coin.reset()
        player.reset()
        player.move()
        enemy.image = transform.scale(image.load("cyborg.png"),(50,500))
        enemy.rect.x = 10
        enemy.rect.y = 200
        enemy.reset()
        enemy.move3()

        if coin_count >= 1:
            gold.reset()
        wall.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        if sprite.collide_rect(player,coin):
            coin_count += 1
            coin.rect.x = 1000
        if sprite.collide_rect(player,enemy):
            player.speed = 0
            if player.speed == 0:
                gover.reset()
            enemy.direction = 'stop'
            window.blit(restart,(0,0))
            

            if restart.get_rect().collidepoint(mouse.get_pos()):
                player.speed = 5
                player.rect.x = 100
                player.rect.y = 400
                enemy.direction = 'right'
                player.reset()
                level = 1
            if coin_count >= 1: 
                if sprite.collide_rect(player,gold):
                    player.speed = 0
                    if player.speed == 0:
                        gwin.reset()
                    
                    window.blit(nxlevel,(0,0))
                    if nxlevel.get_rect().collidepoint(mouse.get_pos()):
                        player.speed = 5
                        level = 2
                        player.rect.x = 100
                        player.rect.y = 400
                        coin_count = 0
                        coin.rect.x = 400
    display.update()
    clock.tick(60)

    
       


    