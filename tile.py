import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        tile_pic = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(tile_pic, (32, 32))
        self.rect = self.image.get_rect(topleft=pos)




