import pygame
import os

WIDTH , HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First_game")


WHITE = (255,255,255)

FPS = 60  # FPS -> Frame Per Seconds.
SPACESHIP_WIDTH , SPACESHIP_HEIGHT = 55, 40
VEL = 5
BORDER = pygame.Rect(WIDTH/2 - 5 , 0, 10, HEIGHT)

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH , SPACESHIP_HEIGHT)), 270)

def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,(0,0,0),BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))   
    pygame.display.update()

def yellow_handle_movement(key_pressed,yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x :
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y  - VEL > 0:
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height + 10  < HEIGHT:
        yellow.y += VEL

def red_handle_movement(key_pressed,red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL  > BORDER.x + BORDER.width:
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y  - VEL > 0:
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + 75 < HEIGHT:
        red.y += VEL    


def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        key_pressed = pygame.key.get_pressed()
        draw_window(red,yellow)
        yellow_handle_movement(key_pressed,yellow)
        red_handle_movement(key_pressed,red)
    pygame.quit()

if __name__ == "__main__":
    main()