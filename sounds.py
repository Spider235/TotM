import pygame
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
mixer.init()

# sounds
# background music
pygame.mixer.music.load(r'Sounds_for_game/bg_music.mp3')
pygame.mixer.music.play(-1, 0.0, 5000)
pygame.mixer.music.set_volume(0.3)

# in-game action sounds
coin_sound = pygame.mixer.Sound(r'Sounds_for_game/coin.wav')
coin_sound.set_volume(0.35)
slide_sound = pygame.mixer.Sound(r'Sounds_for_game/slide.ogg')
slide_sound.set_volume(0.2)
player_eliminated_sound = pygame.mixer.Sound(r'Sounds_for_game/elim.wav')
player_eliminated_sound.set_volume(0.5)
button_pressed_sound = pygame.mixer.Sound(r'Sounds_for_game/btnp.mp3')
button_pressed_sound.set_volume(0.5)
victory_sound = pygame.mixer.Sound(r'Sounds_for_game/win.wav')
victory_sound.set_volume(0.5)
