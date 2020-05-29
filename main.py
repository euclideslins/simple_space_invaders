import pygame
import random
import math

##START PYGAME
pygame.init()

##CREATE SCREEN
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("assets/background.jpg")
pygame.display.set_caption('Space Invaders')


enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemys = 6

for i in range(number_of_enemys):
    enemyImg.append( pygame.image.load("assets/alien.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)


playerImg = pygame.image.load("assets/player64.png")
playerX = 370
playerY = 480
playerX_change=0


score = 0

#Bullet

# 1- ready - you cannot see the bullet
# 2- fire - the bullet is on move

bulletImg = pygame.image.load("assets/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change=10
bullet_state = "ready"

##Function of each 'object'
def player(x,y):
    screen.blit(playerImg, (x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

##Collider function

def collider(enemyX, bulletX, enemyY, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if(distance <27):
        return True
    else:
        return False


##Loop game
running = True
while running:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

## KEYS MOVE ACTION
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                playerX_change = -3
            if(event.key == pygame.K_RIGHT):
                playerX_change = 3
            if(event.key == pygame.K_SPACE):
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT ):
                playerX_change = 0



    playerX += playerX_change

##OUTBOUNDS CONDITION
    if(playerX <= 0):
        playerX=0
    elif(playerX >= 736):
        playerX = 736

    for i in range(number_of_enemys):
        
        enemyX[i] += enemyX_change[i]
        if(enemyX[i] <= 0):
            enemyX_change[i]= 2
            enemyY[i] += enemyY_change[i]
        elif(enemyX[i] >= 736):
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        
        collision = collider(enemyX[i],bulletX, enemyY[i], bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)


        enemy(enemyX[i],enemyY[i],i)





    if(bulletY <= 0):
        bullet_state="ready"
        bulletY = 480
    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX,playerY)
    pygame.display.update()