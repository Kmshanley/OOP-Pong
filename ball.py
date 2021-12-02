import pygame.sprite
import pygame.surface

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ballImg = pygame.image.load('ball.png')
        self.ballSurf = pygame.transform.scale(self.ballImg, (30,30))
        self.pos = (150,300)
        self.speed = 5

    def draw(self, screen, size):
        screen.blit(self.ballSurf, self.pos)
        self.pos = (self.pos[0] + self.speed, self.pos[1])
        print(f'{self.pos[0]=} {size[0]=}')
        if(int(self.pos[0]) >  int(size[0]) or int(self.pos[0]) < int(0)):
            self.speed = self.speed * -1
    def speedUp(self, newSpeed):
        self.speed = newSpeed