import pygame.sprite
import pygame.surface

class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('ball.png'), (15,15))
        self.pos = (150,300)
        self.speed = 5

    def draw(self, screen, size):
        screen.blit(self.image, self.pos)
        self.pos = (self.pos[0] + self.speed, self.pos[1])
        if(int(self.pos[0]) >  int(size[0]-15) or int(self.pos[0]) < int(0)):
            self.speed = self.speed * -1

    def speedUp(self, newSpeed):
        self.speed = newSpeed