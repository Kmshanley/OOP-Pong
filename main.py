import pygame, sys
import pygame.freetype 
from pygame.locals import *
from ball import ball
from puck import puck
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class PongMainMenu:
    def __init__(self):                 #intializing all values
        self._running = True
        self.size = self.weight, self.height = 640, 400
        self.cursor = 0
        self.gameMode = -99
        self.textSpacing = 30
        self.selected = False
        self.fps = pygame.time.Clock()
        self.menuFont = pygame.freetype.SysFont("Copperplate", 40)
        self.screen = pygame.display.set_mode(self.size)
        self.opt1, self.opt1Bound = self.menuFont.render("AI", fgcolor=WHITE)
        self.opt2, self.opt2Bound = self.menuFont.render("Local", fgcolor=WHITE)
        self.opt3, self.opt3Bound = self.menuFont.render("Online", fgcolor=WHITE)
        self.startx = (self.screen.get_width() - (self.opt1.get_width() + self.opt2.get_width() + self.opt3.get_width() + 30)) / 2
        self.starty = self.opt1.get_height() / 2 + self.screen.get_height() / 2

    def on_event(self, event):          #event based logic for all possible cases
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if self.cursor == -1:
                    self.cursor = 1
                elif self.cursor == 1:
                    self.cursor = 0
                else:
                    self.cursor = -1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if self.cursor == -1:
                    self.cursor = 0
                elif self.cursor == 1:
                    self.cursor = -1
                else:
                    self.cursor = 1
            if event.key == pygame.K_RETURN:
                self.selected = True
                self.gameMode = self.cursor
                

    def on_loop(self):              #
        pass
    def on_render(self):            #
        if (~self.selected):
            self.render_menu()
        pygame.display.update()
        self.fps.tick(60)
    def on_cleanup(self):
        pygame.quit()
        sys.exit()
    def on_execute(self):
        while(self._running ):
            for event in pygame.event.get(): # User did something
                self.on_event(event)
            self.on_render()
            self.on_loop()
            if (self.selected):
                break

        return self.gameMode
        
    def render_menu(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.opt1, (self.startx, self.starty))
        self.screen.blit(self.opt2, (self.startx + self.opt1.get_width() + self.textSpacing, self.starty))
        self.screen.blit(self.opt3, (self.startx + self.opt1.get_width() + self.opt2.get_width() + self.textSpacing * 2, self.starty))
        if self.cursor == -1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx, self.starty, self.opt1.get_width(), self.opt1.get_height()),  2)
        if self.cursor == 0:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx + self.opt1.get_width() + self.textSpacing, self.starty, self.opt2.get_width(), self.opt2.get_height()),  2)
        if self.cursor == 1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx + self.opt1.get_width() + self.opt2.get_width() + self.textSpacing*2, self.starty, self.opt3.get_width(), self.opt3.get_height()),  2)

class AIPong:
    def __init__(self):                 #intializing all values
        self._running = True
        self.size = self.weight, self.height = 640, 400
        self.fps = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self.ballObj = ball()
        self.playerPuck = puck(1)
        self.AIPuck = puck(0)

    def on_render(self):
        self.screen.fill(BLACK) 
        self.playerPuck.draw(self.screen)
        self.AIPuck.draw(self.screen)
        pygame.display.update()
        self.fps.tick(60)

    def on_loop(self):              #
        pass

    def on_event(self, event):          #event based logic for all possible cases
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.playerPuck.move(False)
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.playerPuck.move(True)
            if event.key == pygame.K_RETURN:
                pass

    def on_execute(self):
        while(self._running ):
            for event in pygame.event.get(): # User did something
                self.on_event(event)
            self.on_render()
            self.on_loop()

if __name__ == "__main__" :
    pygame.init()
    pygame.display.set_caption("Pong")
    pygame.key.set_repeat(200) #keys held down sent a event every 100 ms
    playPong = PongMainMenu()
    gamemode = playPong.on_execute() #will block until player selects a gamemode

    if (gamemode == -1):
        playPong = AIPong()
    if (gamemode == 0):
        pass
    if (gamemode == 1):
        pass

    pygame.key.set_repeat(100) #keys held down sent a event every 100 ms
    playPong.on_execute() #will loop forever

    pygame.quit()
    sys.exit()