from sounds import *
from settings import important_stuff, screen
from particle import Particle


x = 64
y = 64
width = 64
height = 64
vel = 15


class Player:
    def __init__(self, pos):
        self.height = None
        self.width = None
        self.rect = None
        self.vel_x = None
        self.vel_y = None
        self.reset(pos[0], pos[1])
        self.image = pygame.image.load(r"Pictures_for_game/C1.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.timer = 0
        self.key_up = False
        self.key_down = False
        self.key_right = False
        self.key_left = False

    def update(self, game_over):

        if game_over == 0:
            # get key presses
            if self.vel_x == 0 and self.vel_y == 0:
                if self.key_left:
                    self.key_left = False
                    self.image = pygame.image.load(r"Pictures_for_game/playermid.png")
                    self.image = pygame.transform.scale(self.image, (32, 32))
                    slide_sound.play()
                    self.vel_x = -vel
                if self.key_right:
                    self.key_right = False
                    self.image = pygame.image.load(r"Pictures_for_game/playermid.png")
                    self.image = pygame.transform.scale(self.image, (32, 32))
                    slide_sound.play()
                    self.vel_x = vel
                if self.key_up:
                    self.key_up = False
                    self.image = pygame.image.load(r"Pictures_for_game/playermid.png")
                    self.image = pygame.transform.scale(self.image, (32, 32))
                    slide_sound.play()
                    self.vel_y = -vel
                if self.key_down:
                    self.key_down = False
                    self.image = pygame.image.load(r"Pictures_for_game/playermid.png")
                    self.image = pygame.transform.scale(self.image, (32, 32))
                    slide_sound.play()
                    self.vel_y = vel

            # check for collison
            self.rect.x += self.vel_x
            for tile in important_stuff.world.tile_group:
                # collision in x-axis
                if tile.rect.colliderect(self.rect):
                    # moving right
                    if self.vel_x > 0:
                        self.image = pygame.image.load(r"Pictures_for_game/C2.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
                        self.rect.right = tile.rect.left
                        self.vel_x = 0
                    # moving left
                    elif self.vel_x < 0:
                        self.image = pygame.image.load(r"Pictures_for_game/C2.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
                        self.image = pygame.transform.flip(self.image, True, False)
                        self.rect.left = tile.rect.right
                        self.vel_x = 0

            #  collision in y-axis
            self.rect.y += self.vel_y
            for tile in important_stuff.world.tile_group:
                if tile.rect.colliderect(self.rect):
                    if self.vel_y < 0:
                        self.image = pygame.image.load(r"Pictures_for_game/C1.png")
                        self.image = pygame.transform.flip(self.image, False, True)
                        self.image = pygame.transform.scale(self.image, (32, 32))
                        self.rect.top = tile.rect.bottom
                        self.vel_y = 0
                    elif self.vel_y > 0:
                        self.image = pygame.image.load(r"Pictures_for_game/C1.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
                        self.rect.bottom = tile.rect.top
                        self.vel_y = 0

            if self.vel_y != 0:
                self.timer += 1
            elif self.vel_x != 0:
                self.timer += 1
            else:
                self.timer = 0

            if self.timer % 2 == 0 and self.timer != 0:
                angle = 0
                if self.vel_x != 0:
                    angle = 90
                elif self.vel_y != 0:
                    angle = 0
                important_stuff.world.particle_group.add(Particle(self.rect.x, self.rect.y, angle))

            # check for collision with enemies
            for bat in important_stuff.world.bat_group:
                if bat.rect.colliderect(self.rect):
                    player_eliminated_sound.play()
                    game_over = -1

            # check for collision with spikes
            for spike in important_stuff.world.spike_group:
                if spike.rect.colliderect(self.rect):
                    player_eliminated_sound.play()
                    game_over = -1

            # check if player have left the game borders
            if self.rect.top > 768:
                player_eliminated_sound.play()
                game_over = -1
            if self.rect.bottom < 0:
                player_eliminated_sound.play()
                game_over = -1
            if self.rect.left > 1280:
                player_eliminated_sound.play()
                game_over = -1
            if self.rect.right < 0:
                player_eliminated_sound.play()
                game_over = -1

            # check collision with the trophy (end of level)
            if pygame.sprite.spritecollide(self, important_stuff.world.trophy_group, True):
                game_over = 1

        # draw player onto screen
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return game_over

    def reset(self, r_x, r_y):
        img = pygame.image.load(r"Pictures_for_game/C1.png")
        self.image = pygame.transform.scale(img, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.vel_x = 0
