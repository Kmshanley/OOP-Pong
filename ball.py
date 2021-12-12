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
        self.speed = [self.speedBase,self.speedBase] #speed in x,y direction

    def update(self, screen):
        self.rect = (self.rect[0] + self.speed[0], self.rect[1] + self.speed[1])

        if((self.rect[0] >  screen.get_width() -15) or int(self.rect[0]) < int(0)):
            self.bounceX()

        if (self.rect[1] < 0 or self.rect[1] > screen.get_height()):
            self.bounceY()

    def speedUp(self, newSpeed):
        self.speed = newSpeed
        
    def bounceX(self):
        self.speed[0] = -self.speed[0]
        #self.speed[1] = randint(-self.speedBase, self.speedBase)

    def bounceY(self):
        self.speed[1] = -self.speed[1]
        #self.speed[0] = randint(-self.speedBase, self.speedBase)