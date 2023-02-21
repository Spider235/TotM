from enemy import Enemy
from spikes import Spikes
from coin import *
from trophy import *
from tile import *
from yenemy import Yenemy

tile_size = 32


class World:
    def __init__(self, data):
        self.tile_list = []
        self.tile_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.trophy_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.bat_group = pygame.sprite.Group()
        self.spike_group = pygame.sprite.Group()
        self.score_collected = 0
        self.particle_group = pygame.sprite.Group()
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    # check if tile in top left
                    if col_count * tile_size == 0 and row_count * tile_size == 0:
                        top = True
                        left = True
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        bottom = data[1][0] == 1 or data[1][0] == 5
                    elif col_count * tile_size == 1280 - tile_size and row_count * tile_size == 0:
                        top = True
                        right = True
                        left = row[-2] == 1 or row[-2] == 5
                        bottom = data[1][-1] == 1 or data[1][-1] == 5
                    elif col_count * tile_size == 0 and row_count * tile_size == 768 - tile_size:
                        bottom = True
                        left = True
                        top = data[-2][0] == 1 or data[-2][0] == 5
                        right = row[1] == 1 or row[1] == 5
                    elif col_count * tile_size == 1280 - tile_size and row_count * tile_size == 768 - tile_size:
                        bottom = True
                        right = True
                        top = data[-2][-1] == 1 or data[-2][-1] == 5
                        left = row[-2] == 1 or row[-2] == 5
                    elif row_count * tile_size == 0:
                        top = True
                        bottom = data[1][col_count] == 1 or data[1][col_count] == 5
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        left = row[col_count - 1] == 1 or row[col_count - 1] == 5
                    elif row_count * tile_size == 768 - tile_size:
                        bottom = True
                        top = data[-2][col_count] == 1 or data[-2][col_count] == 5
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        left = row[col_count - 1] == 1 or row[col_count - 1] == 5
                    elif col_count * tile_size == 0:
                        left = True
                        right = row[1] == 1 or row[1] == 5
                        top = data[row_count - 1][0] == 1 or data[row_count - 1][0] == 5
                        bottom = data[row_count + 1][0] == 1 or data[row_count + 1][0] == 5
                    elif col_count * tile_size == 1280 - tile_size:
                        right = True
                        left = row[-2] == 1 or row[-2] == 5
                        top = data[row_count - 1][-1] == 1 or data[row_count - 1][-1] == 5
                        bottom = data[row_count + 1][-1] == 1 or data[row_count + 1][-1] == 5
                    else:
                        top = data[row_count - 1][col_count] == 1 or data[row_count - 1][col_count] == 5
                        bottom = data[row_count + 1][col_count] == 1 or data[row_count + 1][col_count] == 5
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        left = row[col_count - 1] == 1 or row[col_count - 1] == 5
                    if not top and not bottom and not right and not left:
                        image = r"Pictures_for_game\block2all.png"
                    elif not top and not bottom and not right and left:
                        image = r"Pictures_for_game\3sidednoright.png"
                    elif not top and not bottom and right and not left:
                        image = r"Pictures_for_game\blockleftall.png"
                    elif not top and bottom and not right and not left:
                        image = r"Pictures_for_game\3sidednobot.png"
                    elif top and not bottom and not right and not left:
                        image = r"Pictures_for_game\3sidednotop.png"
                    elif not top and bottom and not right and left:
                        image = r"Pictures_for_game\topandright.png"
                    elif top and not bottom and not right and left:
                        image = r"Pictures_for_game\rightandbot.png"
                    elif top and not bottom and right and not left:
                        image = r"Pictures_for_game\botandleft.png"
                    elif not top and bottom and right and not left:
                        image = r"Pictures_for_game\leftandtop.png"
                    elif top and bottom and not right and not left:
                        image = r"Pictures_for_game\2sidedyaxis.png"
                    elif not top and not bottom and right and left:
                        image = r"Pictures_for_game\2sidedxaxis.png"
                    elif not top and bottom and right and left:
                        image = r"Pictures_for_game\bottomblock.png"
                    elif top and bottom and right and not left:
                        image = r"Pictures_for_game\rightblock.png"
                    elif top and not bottom and right and left:
                        image = r"Pictures_for_game\topblock2.png"
                    elif top and bottom and not right and left:
                        image = r"Pictures_for_game\leftblock1.png"
                    else:
                        image = r"Pictures_for_game\blackblock.png"
                    tile = Tile(((col_count * tile_size), (row_count * tile_size)), image)
                    self.tile_group.add(tile)
                if tile == 2:
                    coin = Coin((col_count * tile_size + 5), (row_count * tile_size + 6))
                    self.coin_group.add(coin)
                if tile == 3:
                    tropy = Trophy((col_count * tile_size), (row_count * tile_size))
                    self.trophy_group.add(tropy)
                if tile == 4:
                    enemy = Enemy((col_count * tile_size), (row_count * tile_size))
                    self.bat_group.add(enemy)
                if tile == 5:
                    if col_count * tile_size == 0 and row_count * tile_size == 0:
                        top = True
                        left = True
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        bottom = data[1][0] == 1 or data[1][0] == 5
                    elif col_count * tile_size == 1280 - tile_size and row_count * tile_size == 0:
                        top = True
                        right = True
                        left = row[-2] == 1 or row[-2] == 5
                        bottom = data[1][-1] == 1 or data[1][-1] == 5
                    elif col_count * tile_size == 0 and row_count * tile_size == 768 - tile_size:
                        bottom = True
                        left = True
                        top = data[-2][0] == 1 or data[-2][0] == 5
                        right = row[1] == 1 or row[1] == 5
                    elif col_count * tile_size == 1280 - tile_size and row_count * tile_size == 768 - tile_size:
                        bottom = True
                        right = True
                        top = data[-2][-1] == 1 or data[-2][-1] == 5
                        left = row[-2] == 1 or row[-2] == 5
                    elif row_count * tile_size == 0:
                        top = True
                        bottom = data[1][col_count] == 1 or data[1][col_count] == 5
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        left = row[col_count - 1] == 1 or row[col_count - 1] == 5
                    elif row_count * tile_size == 768 - tile_size:
                        bottom = True
                        top = data[-2][col_count] == 1 or data[-2][col_count] == 5
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        left = row[col_count - 1] == 1 or row[col_count - 1] == 5
                    elif col_count * tile_size == 0:
                        left = True
                        right = row[1] == 1 or row[1] == 5
                        top = data[row_count - 1][0] == 1 or data[row_count - 1][0] == 5
                        bottom = data[row_count + 1][0] == 1 or data[row_count + 1][0] == 5
                    elif col_count * tile_size == 1280 - tile_size:
                        right = True
                        left = row[-2] == 1 or row[-2] == 5
                        top = data[row_count - 1][-1] == 1 or data[row_count - 1][-1] == 5
                        bottom = data[row_count + 1][-1] == 1 or data[row_count + 1][-1] == 5
                    else:
                        top = data[row_count - 1][col_count] == 1 or data[row_count - 1][col_count] == 5
                        bottom = data[row_count + 1][col_count] == 1 or data[row_count + 1][col_count] == 5
                        right = row[col_count + 1] == 1 or row[col_count + 1] == 5
                        left = row[col_count - 1] == 1 or row[col_count - 1] == 5
                    if not top and not bottom and not right and not left:
                        spike_image = r"Pictures_for_game\onlyspikeblock.png"
                    elif not top and not bottom and not right and left:
                        spike_image = r"Pictures_for_game\3sidednorightspike.png"
                    elif not top and not bottom and right and not left:
                        spike_image = r"Pictures_for_game\3sidednoleftspike.png"
                    elif not top and bottom and not right and not left:
                        spike_image = r"Pictures_for_game\3sidednobotspike.png"
                    elif top and not bottom and not right and not left:
                        spike_image = r"Pictures_for_game\3sidednotopspike.png"
                    elif not top and bottom and not right and left:
                        spike_image = r"Pictures_for_game\topandrightspike.png"
                    elif top and not bottom and not right and left:
                        spike_image = r"Pictures_for_game\rightandbotspike.png"
                    elif top and not bottom and right and not left:
                        spike_image = r"Pictures_for_game\botandleftspike.png"
                    elif not top and bottom and right and not left:
                        spike_image = r"Pictures_for_game\leftandtopspike.png"
                    elif top and bottom and not right and not left:
                        spike_image = r"Pictures_for_game\2sidedspikelnr.png"
                    elif not top and not bottom and right and left:
                        spike_image = r"Pictures_for_game\2sidedspikes.png"
                    elif not top and bottom and right and left:
                        spike_image = r"Pictures_for_game\upperspike.png"
                    elif top and bottom and right and not left:
                        spike_image = r"Pictures_for_game\leftspike.png"
                    elif top and not bottom and right and left:
                        spike_image = r"Pictures_for_game\downspike.png"
                    elif top and bottom and not right and left:
                        spike_image = r"Pictures_for_game\rightspike.png"
                    else:
                        spike_image = r"Pictures_for_game\blackblock.png"
                    spike = Spikes(((col_count * tile_size), (row_count * tile_size)), spike_image)
                    self.spike_group.add(spike)
                if tile == 6:
                    yenemy = Yenemy((col_count * tile_size), (row_count * tile_size))
                    self.bat_group.add(yenemy)
                #if tile == 4:
                  #  p_character = Player(((col_count * tile_size), (row_count * tile_size)))
                  #  self.player_group.add(p_character)

                col_count += 1
            row_count += 1


