import pygame.sprite
import pygame.surface
import pygame.mask

class puck(pygame.sprite.Sprite):
    def __init__(self, side, character = 'standardPuck.png', xend = 0):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(character), (10,100))
        self.side = side
        self.speed = 70
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        if self.side:
            self.rect[0] = 10
        else:
            self.rect[0] = xend - 10 - self.image.get_width()

    def move(self, direction):
        if direction and (self.rect[1]>= self.speed):
            self.rect[1] -= self.speed
        elif ~direction and (self.rect[1] + self.speed < 800 - self.image.get_height()/2):
            self.rect[1] += self.speed

    def ability(self):
        pass

class DupePuck(puck):
    def __init__(self, side, character = 'standardPuck.png', xend = 0):
        super().__init__(side, character, xend)

    def ability(self):
            return True


class AIpuck(puck):
    def __init__(self, side, character = 'standardPuck.png', xend = 0):
        super().__init__(side, character, xend)

    def update(self, ball):
        if (ball.rect[1] > self.rect[1] + self.speed/2):
            self.move(0)
        elif (ball.rect[1] < self.rect[1] - self.speed/2):
            self.move(1)