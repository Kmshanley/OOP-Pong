import pygame, sys
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
 
# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
 
while True:
    #Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              pygame.quit()
              sys.exit()
        if event.type == KEYUP:
            pass
        if event.type == KEYDOWN:
            pass
    #input logic should go here
 
    #clear the screen to black. 
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
 
    #update the screen with what we've drawn.
    pygame.display.update()
     
    fps.tick(60) #delay this loop to 60 times a second
 