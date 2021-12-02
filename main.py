import pygame, sys
import pygame.freetype 
from pygame.locals import *
from ball import ball
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
class Pong:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
        self.cursor = 0
        self.gameMode = -99
        self.textSpacing = 30
        self.selected = True
    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Pong")
        self.fps = pygame.time.Clock()
        self.menuFont = pygame.freetype.SysFont("Copperplate", 40)
        self.screen = pygame.display.set_mode(self.size)
        self._running = True
        self.opt1, self.opt1Bound = self.menuFont.render("AI", fgcolor=WHITE)
        self.opt2, self.opt2Bound = self.menuFont.render("Local", fgcolor=WHITE)
        self.opt3, self.opt3Bound = self.menuFont.render("Online", fgcolor=WHITE)
        self.startx = (self.screen.get_width() - (self.opt1.get_width() + self.opt2.get_width() + self.opt3.get_width() + 30)) / 2
        self.starty = self.opt1.get_height() / 2 + self.screen.get_height() / 2
        self.ballObj = ball()
    def on_event(self, event):
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
            if event.type == K_RETURN:
                self.selected = False
                self.gameMode = self.cursor
    def on_loop(self):
        pass
    def on_render(self):
        if (self.selected):
            self.render_menu()
        pygame.display.update()
        self.fps.tick(60)
    def on_cleanup(self):
        pygame.quit()
        sys.exit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running ):
            for event in pygame.event.get(): # User did something
                self.on_event(event)
                self.on_render()
            self.on_render()
            self.on_loop()
        self.on_cleanup()
        

    def render_menu(self):
        self.screen.fill(BLACK)
        self.ballObj.draw(self.screen, (self.screen.get_width(),self.screen.get_height()))
        self.screen.blit(self.opt1, (self.startx, self.starty))
        self.screen.blit(self.opt2, (self.startx + self.opt1.get_width() + self.textSpacing, self.starty))
        self.screen.blit(self.opt3, (self.startx + self.opt1.get_width() + self.opt2.get_width() + self.textSpacing * 2, self.starty))
        if self.cursor == -1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx, self.starty, self.opt1.get_width(), self.opt1.get_height()),  2)
        if self.cursor == 0:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx + self.opt1.get_width() + self.textSpacing, self.starty, self.opt2.get_width(), self.opt2.get_height()),  2)
        if self.cursor == 1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx + self.opt1.get_width() + self.opt2.get_width() + self.textSpacing*2, self.starty, self.opt3.get_width(), self.opt3.get_height()),  2)

if __name__ == "__main__" :
    playPong = Pong()
    playPong.on_execute()