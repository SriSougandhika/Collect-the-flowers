import pygame
import random

from pygame import mixer
mixer.init()

mixer.music.load("background.mp3")
mixer.music.play(-1)

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("FLOWERS COLLECTOR")

basket = pygame.image.load("basket.png")
bx = 370
by = 480
bxc = 0
def basket_show(x,y):
    screen.blit(basket,(x,y))

f = ["flower1.png", "flower2.png", "flower3.png", "flower4.png", "cactus.png"]
flowers = []
fx = []
fy = []
ftype = []

num_flowers = 5
for i in range(num_flowers):
    x = random.choice(f)
    flowers.append(pygame.image.load(x))
    fx.append(random.randint(20,740))
    fy.append(random.randint(0,50))
    if x == "cactus.png":
        ftype.append("c")
    else:
        ftype.append("f")

def flower_show(x,y):
    global num_flowers
    for i in range(num_flowers):
        screen.blit(flowers[i],(x[i],y[i]))

def collide(BX,BY,FX,FY):
    dist = (((BX-FX)**2)+((BY-FY)**2))**0.5
    if dist < 30:
        return True
    else:
        return False


score = 0
minus = 0
lives = 3
level = 1
target = 10
gameovertime = 1
font = pygame.font.Font("Corporation Games.otf",30)
tX = 10
tY = 10
def showScore():
    global score
    scoreR = font.render("SCORE : "+str(score), True, (102,0,102))
    screen.blit(scoreR,(tX,tY))
    global lives
    l = font.render("LIVES LEFT : "+str(lives), True, (102,0,102))
    screen.blit(l, (tX, tY+30))
    global level
    lvl = font.render("LEVEL : "+str(level), True, (102,0,102))
    screen.blit(lvl, (tX, tY+60))
    global target
    lvl = font.render("TARGET : " + str(target), True, (102, 0, 102))
    screen.blit(lvl, (tX, tY + 90))

go = pygame.font.Font("Corporation Games.otf",60)
def gameover():
    overtext1 = go.render('--GAME OVER--', True, (102,0,102))
    screen.blit(overtext1, (160,250))
run = True
while run:
    screen.fill((229, 204, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                bxc = 0.3
            elif e.key == pygame.K_LEFT:
                bxc = -0.3
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                bxc = 0
    bx += bxc
    for i in range(num_flowers):
        fy[i] += 0.1
        if fy[i] > 480:
            some = random.choice(f)
            flowers[i] = pygame.image.load(some)
            fx[i] = random.randint(200,600)
            fy[i] = random.randint(0,300)
            if some == "cactus.png":
                ftype[i] = "c"
            else:
                ftype[i] = "f"
    if bx > 750:
        bx = 750
    elif bx < 50:
        bx = 50
    for i in range(num_flowers):
        if collide(bx,by,fx[i],fy[i]):
            cs = mixer.Sound("coin.mp3")
            cs.play()
            if ftype[i] == "c":
                strc = mixer.Sound("strike.mp3")
                strc.play()
                minus += 1
                lives -= 1
                print("minus point")
            else:
                score += 1
                print(score)
            some = random.choice(f)
            flowers[i] = pygame.image.load(some)
            fx[i] = random.randint(200,600)
            fy[i] = random.randint(0,300)
            if some == "cactus.png":
                ftype[i] = "c"
            else:
                ftype[i] = "f"
    if target == score:
        lus = mixer.Sound("LevelUp.mp3")
        lus.play()
        target += 20
        level += 1
    if minus == 3:
        if gameovertime == 1:
            gos = mixer.Sound("gameover.mp3")
            gos.play()
            gameovertime += 1
        gameover()
        for i in range(num_flowers):
            fy[i] = 2000
    basket_show(bx,by)
    flower_show(fx,fy)
    showScore()
    pygame.display.update()


