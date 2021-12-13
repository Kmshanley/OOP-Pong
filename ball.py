import pygame.sprite
import pygame.surface
import pygame.mask
from random import randint

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('ball.png'), (15,15))
        self.rect = (randint(0,300),randint(0,300))
        self.speedBase = 5
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect = (100,100)
        self.speed = [self.speedBase,self.speedBase] #speed in x,y direction

        self.lsideHit = 0
        self.rsideHit = 0

    def update(self, screen):
        self.rect = (self.rect[0] + self.speed[0], self.rect[1] + self.speed[1])

        if (self.rect[0] >  screen.get_width() -15):
            self.bounceX()
            self.rsideHit += 1
        if (self.rect[0] < 0):
            self.bounceX()
            self.lsideHit += 1

        if (self.rect[1] < 0): 
            self.bounceY()
        if(self.rect[1] > screen.get_height() - 15):
            self.bounceY()
            

    def speedUp(self, newSpeed):
        self.speed[0] = newSpeed[0]
        self.speed[1] = newSpeed[1]
        
    def bounceX(self):
        #self.rect = (self.rect[0] - self.speed[0], self.rect[1] - self.speed[1])
        self.speed[0] = -self.speed[0]
        self.speed[1] += randint(-1, 2)

        if (self.speed[1] > self.speedBase * 5):
            self.speed[1] -= randint(1,5) 

    def bounceY(self):
        #self.rect = (self.rect[0] - self.speed[0], self.rect[1] - self.speed[1])
        self.speed[1] = -self.speed[1]
        self.speed[0] += randint(-1, 1)

        if (self.speed[0] > self.speedBase * 5):
            self.speed[0] -= randint(1,5) 