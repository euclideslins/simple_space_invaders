import pygame
import random
##START PYGAME
pygame.init()

##CREATE SCREEN
screen = pygame.display.set_mode((800,600))
background = pygame.image.load("assets/background.jpg")
pygame.display.set_caption('Space Invaders')


enemyImg = pygame.image.load("assets/alien.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change=4
enemyY_change=40


playerImg = pygame.image.load("assets/player64.png")
playerX = 370
playerY = 480
playerX_change=0

#Bullet

# 1- ready - you cannot see the bullet
# 2- fire - the bullet is on move

bulletImg = pygame.image.load("assets/bullet.png")
bulletX = 0
bulletY = 480
bulletY_change=10
bullet_state = "ready"


def player(x,y):
    screen.blit(playerImg, (x,y))
def enemy(x,y):
    screen.blit(enemyImg, (x,y))
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


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
                bullet(playerX, bulletY)
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT ):
                playerX_change = 0



    playerX += playerX_change

##OUTBOUNDS CONDITION
    if(playerX <= 0):
        playerX=0
    elif(playerX >= 736):
        playerX = 736


    enemyX += enemyX_change
    if(enemyX <= 0):
        enemyX_change= 4
        enemyY += enemyY_change
    elif(enemyX >= 736):
        enemyX_change = -4
        enemyY += enemyY_change


    if bullet_state is "fire":
        bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()