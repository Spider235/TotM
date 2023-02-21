import pygame


class Spikes(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        spike_pic = pygame.image.load(image).convert()
        self.image = pygame.transform.scale(spike_pic, (32, 32))
        self.rect = self.image.get_rect(topleft=pos)
