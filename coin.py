import pygame
#from Settings import *

coin_height = 21
coin_width = 22


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.star_img1 = pygame.image.load(r"Pictures_for_game/stars1.png")
        self.star_img2 = pygame.image.load(r"Pictures_for_game/stars2.png")
        self.star_img3 = pygame.image.load(r"Pictures_for_game/stars3.png")
        self.star_img4 = pygame.image.load(r"Pictures_for_game/stars4.png")
        self.image = pygame.transform.scale(self.star_img1, (22, 22))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation_index = 0
        self.list_index = 0
        self.animation_list = [self.star_img1, self.star_img2, self.star_img3, self.star_img4]

    def anima(self):
        self.animation_index += 1
        if self.animation_index % 7 == 0:
            self.list_index += 1
            if self.list_index == len(self.animation_list):
                self.list_index = 0
            self.image = self.animation_list[self.list_index]
            self.image = pygame.transform.scale(self.image, (22, 22))

    def update(self):
        self.anima()









