import pygame, sys
import pygame.freetype
from pygame.locals import *
#import puck, ball

pygame.init()
fps = pygame.time.Clock()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
 
# Open a new window
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
menuFont = pygame.freetype.SysFont("Copperplate", 40)

selected = True
cursor = 0
gameMode = -99
textSpacing = 30
opt1, opt1Bound = menuFont.render("AI", fgcolor=WHITE)
opt2, opt2Bound = menuFont.render("Local", fgcolor=WHITE)
opt3, opt3Bound = menuFont.render("Online", fgcolor=WHITE)
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
    startx = (screen.get_width() - (opt1.get_width() + opt2.get_width() + opt3.get_width() + 30)) / 2
    starty = opt1.get_height() / 2 + screen.get_height() / 2
    screen.blit(opt1, (startx, starty))
    screen.blit(opt2, (startx + opt1.get_width() + textSpacing, starty))
    screen.blit(opt3, (startx + opt1.get_width() + opt2.get_width() + textSpacing * 2, starty))

    if cursor == -1:
        pygame.draw.rect(screen, RED, pygame.Rect(startx, starty, opt1.get_width(), opt1.get_height()),  2)
    if cursor == 0:
        pygame.draw.rect(screen, RED, pygame.Rect(startx + opt1.get_width() + textSpacing, starty, opt2.get_width(), opt2.get_height()),  2)
    if cursor == 1:
        pygame.draw.rect(screen, RED, pygame.Rect(startx + opt1.get_width() + opt2.get_width() + textSpacing*2, starty, opt3.get_width(), opt3.get_height()),  2)

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
 