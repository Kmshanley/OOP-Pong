import pygame.sprite
import pygame.surface
import pygame.mask
from perlin_noise import PerlinNoise

class terrain(pygame.sprite.Sprite):
    def __init__(self,size, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.frombuffer(self.gen((50,50)), (50,50), 'RGB'), size)
        self.image.set_colorkey((0,0,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]
 
    @staticmethod
    def gen(size):
        noise = PerlinNoise(octaves=8)
        pic = [[noise([i/size[0], j/size[1]]) for j in range(size[0])] for i in range(size[1])]
        map = bytearray()

        for i in pic:
            for j in i:
                if j > 0.4:
                    map.extend(b'\xff\xff\xff') #black
                else:
                    map.extend(b'\x00\x00\x00') #white

        return map