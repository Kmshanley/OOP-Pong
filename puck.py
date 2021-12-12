import pygame.sprite
import pygame.surface

class puck(pygame.sprite.Sprite):
    def __init__(self, side, character = 'standardPuck.png'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(character), (10,100))
        self.side = side
        self.ypos = 0
        self.yposTarget = 0
        self.speed = 7

    def draw(self, screen):
        if self.yposTarget > self.ypos:
            self.ypos += 1
        elif self.yposTarget < self.ypos:
            self.ypos -= 1
            
        if self.side:
            screen.blit(self.image, (10, self.ypos))
        else:
            screen.blit(self.image, (screen.get_width(), self.ypos))

    def move(self, direction):
        if direction:
            self.yposTarget -= self.speed
        else:
            self.yposTarget += self.speed