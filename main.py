import pygame, sys
import pygame.freetype
from pygame.locals import *
import puck, ball

pygame.init()
fps = pygame.time.Clock()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
defaultFont = pygame.freetype.SysFont("Copperplate", 24)

selected = True
cursor = 0
gameMode = -99
while selected:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              pygame.quit()
              sys.exit()
        if event.type == KEYUP:
            if cursor == 1:
                cursor = -1
            else:
                cursor += 1
        if event.type == KEYDOWN:
            if cursor == -1:
                cursor = 1
            else:
                cursor -= 1
        if event.type == K_RETURN:
            selected = False
            gameMode = cursor

    screen.fill(BLACK)
    defaultFont.render_to(screen, (350, 350), "Hello World!", WHITE)
    pygame.display.update()
    fps.tick(60)
 
while True:
    #Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              pygame.quit()
              sys.exit()
        if event.type == KEYUP:
            pass
        if event.type == KEYUP:
            pass
        if event.type == K_KP_ENTER:
            pass
    #input logic should go here
 
    #clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
    #update the screen with what we've drawn.
    pygame.display.update()
     
    fps.tick(60) #delay this loop to 60 times a second
 