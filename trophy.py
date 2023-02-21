import pygame


class Trophy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.trophy_img1 = pygame.image.load(r"Pictures_for_game/exit1.png")
        self.trophy_img2 = pygame.image.load(r"Pictures_for_game/exit2.png")
        self.trophy_img3 = pygame.image.load(r"Pictures_for_game/exit3.png")
        self.trophy_img4 = pygame.image.load(r"Pictures_for_game/exit4.png")
        self.trophy_img5 = pygame.image.load(r"Pictures_for_game/exit5.png")
        self.trophy_img6 = pygame.image.load(r"Pictures_for_game/exit6.png")
        self.trophy_img7 = pygame.image.load(r"Pictures_for_game/exit7.png")
        self.trophy_img8 = pygame.image.load(r"Pictures_for_game/exit8.png")
        self.trophy_img9 = pygame.image.load(r"Pictures_for_game/exit9.png")
        self.trophy_img10 = pygame.image.load(r"Pictures_for_game/exit10.png")
        self.trophy_img11 = pygame.image.load(r"Pictures_for_game/exit11.png")
        self.trophy_img12 = pygame.image.load(r"Pictures_for_game/exit12.png")

        self.image = pygame.transform.scale(self.trophy_img1, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.animation_index = 0
        self.list_index = 0
        self.animation_list = [self.trophy_img1, self.trophy_img2, self.trophy_img3, self.trophy_img4, self.trophy_img5,
                               self.trophy_img6, self.trophy_img7, self.trophy_img8, self.trophy_img9,
                               self.trophy_img10, self.trophy_img11, self.trophy_img12]

    def anima(self):
        self.animation_index += 1
        if self.animation_index % 7 == 0:
            self.list_index += 1
            if self.list_index == len(self.animation_list):
                self.list_index = 0
            self.image = self.animation_list[self.list_index]

    def update(self):
        self.anima()
