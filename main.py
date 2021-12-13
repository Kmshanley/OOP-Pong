import pygame, sys
import pygame.freetype 
from pygame.locals import *
from ball import ball
from puck import puck, AIpuck, DupePuck
from terrain import terrain
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class PongMainMenu:
    def __init__(self):                 #intializing all values
        self._running = True
        self.size = self.weight, self.height = 1200, 800
        self.cursor = 0
        self.gameMode = -99
        self.textSpacing = 30
        self.selected = False
        self.fps = pygame.time.Clock()
        self.menuFont = pygame.freetype.SysFont("Copperplate", 40)
        self.tileFont = pygame.freetype.SysFont("Copperplate", 90)
        self.screen = pygame.display.set_mode(self.size)
        self.opt1, self.opt1Bound = self.menuFont.render("AI", fgcolor=WHITE)
        self.opt2, self.opt2Bound = self.menuFont.render("Local", fgcolor=WHITE)
        self.opt3, self.opt3Bound = self.menuFont.render("Online", fgcolor=WHITE)
        self.title, self.tileBound = self.menuFont.render("PONG", fgcolor=WHITE)
        self.title = pygame.transform.smoothscale(self.title, (self.title.get_width() * 5, self.title.get_height() * 5))
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
        self.screen.blit(self.title, (self.screen.get_width() / 2 - self.title.get_width() / 2, int(self.screen.get_height() * 0.25)))
        if self.cursor == -1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx, self.starty, self.opt1.get_width(), self.opt1.get_height()),  2)
        if self.cursor == 0:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx + self.opt1.get_width() + self.textSpacing, self.starty, self.opt2.get_width(), self.opt2.get_height()),  2)
        if self.cursor == 1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx + self.opt1.get_width() + self.opt2.get_width() + self.textSpacing*2, self.starty, self.opt3.get_width(), self.opt3.get_height()),  2)


class PongCharSelect:
    def __init__(self):                 #intializing all values
        self._running = True
        self.size = self.weight, self.height = 1200, 800
        self.cursor = 1
        self.character = -99
        self.textSpacing = 30
        self.selected = False
        self.fps = pygame.time.Clock()
        self.menuFont = pygame.freetype.SysFont("Copperplate", 40)
        self.screen = pygame.display.set_mode(self.size)
        self.opt1, self.opt1Bound = self.menuFont.render("Basic", fgcolor=WHITE)
        self.opt2, self.opt2Bound = self.menuFont.render("Baller", fgcolor=WHITE)
        self.startx = (self.screen.get_width() - (self.opt1.get_width() + self.opt2.get_width()+ 30)) / 2
        self.starty = self.opt1.get_height() / 2 + self.screen.get_height() / 2

    def on_event(self, event):          #event based logic for all possible cases
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.cursor = -self.cursor 
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.cursor = -self.cursor
            if event.key == pygame.K_RETURN:
                self.selected = True
                self.character = self.cursor
                
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
            if (self.selected):
                break
 
        return self.character
        
    def render_menu(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.opt1, (self.startx, self.starty))
        self.screen.blit(self.opt2, (self.startx + self.opt1.get_width() + self.textSpacing, self.starty))
        if self.cursor == -1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx, self.starty, self.opt1.get_width(), self.opt1.get_height()),  2)
        if self.cursor == 1:
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.startx + self.opt1.get_width() + self.textSpacing, self.starty, self.opt2.get_width(), self.opt2.get_height()),  2)



class Pong():
    def __init__(self):                 #intializing all values
        self._running = True
        self.size = self.width, self.height = 1200, 800
        self.fps = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)
        self.ballObj = ball()
        self.pucks = list()
        self.balls = list()

        self.rscore = 0
        self.lscore = 0

        self.all_sprites = pygame.sprite.Group()

        self.balls.append(self.ballObj)
        self.niceTerrain = terrain((int(self.width / 2),self.height), (int(self.width * 0.25), 0))
        self.scoreFont = pygame.freetype.SysFont("Copperplate", 40)
        
        self.all_sprites.add(self.ballObj)
        self.all_sprites.add(self.niceTerrain)

    def charBase(self, side):
        self.playerPuck = puck(1)
        self.pucks.append(self.playerPuck)
        self.all_sprites.add(self.playerPuck)

    def charBaller(self, side):
        self.playerPuck = DupePuck(1)
        self.pucks.append(self.playerPuck)
        self.all_sprites.add(self.playerPuck)

    def on_render(self):
        self.screen.fill(BLACK)
        self.scoreFont.render_to(self.screen, (int(self.screen.get_width() * 0.15), 10), str(self.rscore), fgcolor=WHITE)
        self.scoreFont.render_to(self.screen, (int(self.screen.get_width() * 0.85), 10), str(self.lscore), fgcolor=WHITE)  
        self.all_sprites.draw(self.screen)

        pygame.display.update()
        self.fps.tick(60)

    def on_loop(self):              
        for b in self.balls:
            for p in self.pucks:
                if pygame.sprite.collide_mask(b, p):
                    b.bounceX()
                    #print("pygame.sprite.collide_mask(b, p)")
            if pygame.sprite.collide_mask(b, self.niceTerrain):
                collisionPoint = pygame.sprite.collide_mask(b, self.niceTerrain)
                if (collisionPoint[0] > (collisionPoint[1] * 2) or collisionPoint[1] * 2 > collisionPoint[0]):
                    b.bounceX()
                    b.bounceY()
                else:
                    b.bounceX()

        self.lscore = 0
        self.rscore = 0
        for b in self.balls:
            self.rscore += b.rsideHit
            self.lscore += b.lsideHit
            b.update(self.screen)

        if len(self.balls) > 1:
            for b in self.balls:
                for a in self.balls:
                    if b == a:
                        continue
                    if pygame.sprite.collide_mask(b,a):
                        b.bounceX()
                        a.bounceX()



    def on_execute(self):
        while(self._running ):
            for event in pygame.event.get(): # User did something
                self.on_event(event)
            self.on_loop()
            self.on_render() #render should be last


class AIPong(Pong):
    def __init__(self):                 #intializing all values
        super().__init__()
        self.AIPuck = AIpuck(0, xend=self.width)
        self.pucks.append(self.AIPuck)
        self.all_sprites.add(self.AIPuck)

    def on_event(self, event):          #event based logic for all possible cases
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if (keys[ord('s')] or keys[pygame.K_DOWN]):
                self.playerPuck.move(False)
            if (keys[ord('w')] or keys[pygame.K_UP]):
                self.playerPuck.move(True)
            if keys[pygame.K_SPACE]:
                if self.playerPuck.ability():
                    self.newBall = ball()
                    self.newBall.speedUp((self.newBall.speed[0]/2, self.newBall.speed[1]))
                    self.balls.append(self.newBall)
                    self.all_sprites.add(self.newBall)

    def on_loop(self):
        super().on_loop()
        self.AIPuck.update(self.ballObj)


class LocalPong(Pong):
    def __init__(self):                 #intializing all values
        super().__init__()
        self.playerPuck2 = puck(0, xend = self.width)
        self.pucks.append(self.playerPuck2)
        self.all_sprites.add(self.playerPuck2)

    def on_event(self, event):          #event based logic for all possible cases
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == KEYDOWN:
            keys = pygame.key.get_pressed()     #returns and places bools of all keys pressed
            if keys[ord('s')]:
                self.playerPuck.move(False)
            if keys[ord('w')]:
                self.playerPuck.move(True)

            if keys[pygame.K_DOWN]:
                self.playerPuck2.move(False)
            if keys[pygame.K_UP]:
                self.playerPuck2.move(True)

            if keys[pygame.K_SPACE]:
                if self.playerPuck.ability():
                    self.newBall = ball()
                    self.newBall.speedUp((self.newBall.speed[0]/2, self.newBall.speed[1]))
                    self.balls.append(self.newBall)
                    self.all_sprites.add(self.newBall)


if __name__ == "__main__" :
    pygame.init()
    pygame.display.set_caption("Pong")
    pygame.key.set_repeat(200) #keys held down sent a event every 100 ms
    playPong = PongMainMenu()
    gamemode = playPong.on_execute() #will block until player selects a gamemode
    charSelect = PongCharSelect()
    character = charSelect.on_execute()

    if (gamemode == -1):
        playPong = AIPong()
    if (gamemode == 0):
        playPong = LocalPong()
    if (gamemode == 1):
        pass

    if (character == -1):
        playPong.charBase(1)
    if (character == 1):
        playPong.charBaller(1)

    pygame.key.set_repeat(100) #keys held down sent a event every 100 ms
    playPong.on_execute() #will loop forever

    pygame.quit()
    sys.exit()