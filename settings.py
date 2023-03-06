import pygame
from world import World
from levels import *

screen_width = 1280
screen_height = 768

screen = pygame.display.set_mode([screen_width, screen_height])

# score_font
pygame.font.init()
font_of_score = r'Fonts_for_game\TechnoRaceItalic-eZRWe.otf'
score_font = pygame.font.Font(font_of_score, 20)
color_font = (255, 255, 255) # white
yellow_font = (255, 255, 0)
general_font = r'Fonts_for_game\general_font.otf'
game_font = pygame.font.Font(general_font, 105)
end_game_font = pygame.font.Font(font_of_score, 65)

bg3_image = pygame.image.load(r"Pictures_for_game/bg_g.png")
bg3_image = pygame.transform.scale(bg3_image, (screen_width, screen_height))
bg4_image = pygame.image.load(r"Pictures_for_game/totmbg.png")
bg4_image = pygame.transform.scale(bg4_image, (screen_width, screen_height))

max_levels = 14


class LevelStuff:
    def __init__(self):
        self.world = World(level_list[0])
        self.level_count = 0


important_stuff = LevelStuff()


def draw_text(text, font, text_colour, x, y):
    image = font.render(text, True, text_colour)
    screen.blit(image, (x, y))
