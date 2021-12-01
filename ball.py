import pygame.sprite
import pygame.surface

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.Surface([1,1])
        self.pos = 0
        self.speed = 1
    
    def __init__(self, size, speed):
        super().__init__()
        pygame.surface([size])
        self.speed = speed
        self.pos = 0

    def draw(self):
        pass

    def speedUp(self, newSpeed):
        self.speed = newSpeed