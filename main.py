import pygame
import random
##START PYGAME
pygame.init()

##CREATE SCREEN
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Space Invaders')

enemyImg = pygame.image.load("assets/alien.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change=0.3

playerImg = pygame.image.load("assets/player64.png")
playerX = 370
playerY = 480
playerX_change=0


def player(x,y):
    screen.blit(playerImg, (x,y))
def enemy(x,y):
    screen.blit(enemyImg, (x,y))

##Loop game
running = True
while running:
    screen.fill((10,200,30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

## KEYS MOVE ACTION
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                playerX_change = -0.2
            if(event.key == pygame.K_RIGHT):
                playerX_change = 0.2
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
        enemyX_change= 0.3
    elif(enemyX >= 736):
        enemyX_change = -0.3


    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()