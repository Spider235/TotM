from settings import *


# button images
restart_img = pygame.image.load(r"Pictures_for_game/replay.png")
restart_img = pygame.transform.scale(restart_img, (175, 75))
start_img = pygame.image.load(r"Pictures_for_game/play.png")
start_img = pygame.transform.scale(start_img, (175, 75))
exit_img = pygame.image.load(r"Pictures_for_game/ext.png")
exit_img = pygame.transform.scale(exit_img, (175, 75))


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)

        return action
