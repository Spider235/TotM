import pygame
from pygame import mixer
from world import *
from groups import *
from button import *
from player import Player
from settings import *
from levels import *
from sounds import *

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

pygame.init()

pygame.display.set_caption("Tomb of the mask")
clock = pygame.time.Clock()

player = Player((32, 32))

# load in level data and creatae world
###

restart_button = Button(825, 350, restart_img)
start_button = Button(950, 450, start_img)
exit_button = Button(700, 450, exit_img)

game_over = 0
main_menu = True
score = 0
play_sound = True

run = True

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.key_down = False
            if event.key == pygame.K_UP:
                player.key_up = False
            if event.key == pygame.K_LEFT:
                player.key_left = False
            if event.key == pygame.K_RIGHT:
                player.key_right = False
        if event.type == pygame.KEYDOWN:
            player.key_down = event.key == pygame.K_DOWN
            player.key_up = event.key == pygame.K_UP
            player.key_left = event.key == pygame.K_LEFT
            player.key_right = event.key == pygame.K_RIGHT

        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    if main_menu:
        screen.blit(bg4_image, (0, 0))
        draw_text("How to play:", score_font, yellow_font, screen_width // 2 + 220,
                  screen_height - 550)
        draw_text("Press the arrow keys to move", score_font, yellow_font, screen_width // 2 + 150,
                  screen_height - 500)
        draw_text("Your goal is to get the best score possible and complete every level", score_font, yellow_font,
                  screen_width // 2, screen_height - 450)
        draw_text("Collect starts, and avoid enemies and spikes", score_font, yellow_font,
                  screen_width // 2 + 90, screen_height - 400)

        if exit_button.draw():
            button_pressed_sound.play()
            run = False
        if start_button.draw():
            important_stuff.world = World(level_list[0])
            button_pressed_sound.play()
            main_menu = False
    else:
        game_over = player.update(game_over)
        if game_over == 0:
            important_stuff.world.tile_group.draw(screen)
            important_stuff.world.coin_group.update()
            important_stuff.world.coin_group.draw(screen)
            important_stuff.world.trophy_group.update()
            important_stuff.world.trophy_group.draw(screen)
            important_stuff.world.bat_group.update()
            important_stuff.world.bat_group.draw(screen)
            important_stuff.world.spike_group.draw(screen)
            important_stuff.world.particle_group.update()
            important_stuff.world.particle_group.draw(screen)
            screen.blit(player.image, player.rect)

            # update score & check if the coins has been collected
            if pygame.sprite.spritecollide(player, important_stuff.world.coin_group, True):
                score += 100
                important_stuff.world.score_collected += 100
                coin_sound.play()
            draw_text('Score: ' + str(score), score_font, yellow_font, tile_size, coin_height - 15)
            draw_text('Level: ' + str(important_stuff.level_count + 1), score_font, yellow_font, screen_width // 2, coin_height - 15)

        # if the player died
        if game_over == -1:
            mixer.music.stop()

            screen.blit(bg3_image, (0, 0))
            draw_text('Game Over', game_font, yellow_font, screen_width - 675, screen_height - 680)
            draw_text('Your Score: ' + str(score), score_font, yellow_font, screen_width - 425, screen_height - 575)
            draw_text('Level: ' + str(important_stuff.level_count + 1), score_font, yellow_font, screen_width - 405, screen_height - 525)

            if restart_button.draw():
                score -= important_stuff.world.score_collected
                important_stuff.world = World(level_list[important_stuff.level_count])
                button_pressed_sound.play()
                mixer.music.play(-1, 0.0, 5000)
                player.reset(64, 64)
                game_over = 0

        # if the player has completed the level
        if game_over == 1:
            # reset game and go to next level
            important_stuff.level_count += 1
            if important_stuff.level_count == len(level_list):
                game_over = 2
            player.reset(64, 64)
            if important_stuff.level_count <= max_levels and game_over != 2:
                world_data = []
                important_stuff.world = World(level_list[important_stuff.level_count])
                game_over = 0

        if game_over == 2:
            screen.blit(bg3_image, (0, 0))
            if play_sound:
                victory_sound.play()
                play_sound = False
            draw_text('Victory', game_font, yellow_font, screen_width - 600, screen_height - 700)
            draw_text('Congratulations! you have reached the end of the dungeon', score_font, yellow_font, screen_width - 625, screen_height - 560)
            draw_text('Your score: ' + str(score), end_game_font, yellow_font, screen_width - 600, screen_height - 500)

    pygame.display.update()
    clock.tick(60)




pygame.quit()
