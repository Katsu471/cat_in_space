import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption("Collision Test")

WINDOW_SIZE = (800,600)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

player_image = pygame.image.load("Data/images/player.png")

moveing_up = False
moveing_left = False
moveing_right = False

player_location = [50,50]
player_y_momentum = 0 #Gravity var

player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height()) #collision
test_rect = pygame.Rect(400,540,100,100)
#

while True:
    screen.fill((146,244,255))
    # the rest of gravity start
    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = 0
    else:
        player_y_momentum += 0.1
    player_location[1] += player_y_momentum
    # the rest of gravuty end

    #collision start
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255,100,100), test_rect)

    else:
        pygame.draw.rect(screen,(0,0,0), test_rect)

    #collision end
    
    screen.blit(player_image,player_location)

    if moveing_up == True:
        player_location[1] -= 4
    if moveing_left == True:
        player_location[0] -= 4
    if moveing_right == True:
        player_location[0] += 4

    for event in pygame.event.get():
        if event.type == QUIT:
            print ("death")
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moveing_right = True
            if event.key == K_LEFT:
                moveing_left = True
            if event.key == K_UP:
                moveing_up = True
                
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moveing_right = False
            if event.key == K_LEFT:
                moveing_left = False
            if event.key == K_UP:
                moveing_up = False
                
    pygame.display.update()
    clock.tick(60)
