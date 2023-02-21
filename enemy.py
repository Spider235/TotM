import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.bat_pic1 = pygame.image.load(r"Pictures_for_game/bat1.png").convert_alpha()
        self.bat_pic2 = pygame.image.load(r"Pictures_for_game/bat2.png").convert_alpha()
        self.bat_pic3 = pygame.image.load(r"Pictures_for_game/bat4.png").convert_alpha()
        self.bat_pic4 = pygame.image.load(r"Pictures_for_game/bat3.png").convert_alpha()
        self.bat_pic5 = pygame.image.load(r"Pictures_for_game/bat4.png").convert_alpha()
        self.bat_pic6 = pygame.image.load(r"Pictures_for_game/bat2.png").convert_alpha()
        self.bat_pic7 = pygame.image.load(r"Pictures_for_game/bat5.png").convert_alpha()

        self.animation_list = [self.bat_pic1, self.bat_pic2, self.bat_pic3, self.bat_pic4, self.bat_pic5, self.bat_pic6, self.bat_pic7]
        self.frame_index = 0
        self.image = self.animation_list[0]
        self.rect = self.image.get_rect(center=(x + 16, y + 10))
        self.move_direction = 1
        self.move_counter = 0
        self.animation_timer = pygame.time.get_ticks()
        self.flip = False

    def anima(self):
        animation_speed = 150
        self.image = self.animation_list[self.frame_index]
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.image = pygame.transform.flip(self.image, self.flip, False)
        if pygame.time.get_ticks() - self.animation_timer > animation_speed:
            self.frame_index += 1
            self.animation_timer = pygame.time.get_ticks()
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

    def update(self):
        self.anima()
        self.rect.x += self.move_direction # move right
        if self.flip:
            self.move_counter -= 1
            if self.move_counter < -74:
                self.move_direction = 1
                self.flip = False
        else:
            self.move_counter += 1
            if self.move_counter > 59:
                self.move_direction = -1
                self.flip = True



