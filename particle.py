import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, rotate_angle):
        pygame.sprite.Sprite.__init__(self)
        self.rotate_angle = rotate_angle
        self.image = pygame.image.load(r"Pictures_for_game/Particle2.png").convert_alpha()
        self.rect = self.rect = self.image.get_rect(center=(x + 16, y + 16))
        self.timer = 0
        self.image = pygame.transform.rotate(self.image, rotate_angle)

    def update(self):
        self.timer += 1
        if self.timer == 10:
            self.image = pygame.image.load(r"Pictures_for_game/Particle3.png").convert_alpha()
            self.image = pygame.transform.rotate(self.image, self.rotate_angle)
        elif self.timer == 20:
            self.kill()
