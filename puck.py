import pygame.sprite
import pygame.surface

class puck(pygame.sprite.Sprite):
    def __init__(self, character = 'standardPuck.png', pos = (10,10)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(character), (10,100))
        self.pos = pos
        self.speed = 7

    def draw(self, screen, size):
        screen.blit(self.image, self.pos)
        self.pos = (self.pos[0], self.pos[1] + self.speed)
        if(int(self.pos[1]) >  int(size[1]-90) or int(self.pos[1]) < int(0)):
            self.speed = self.speed * -1