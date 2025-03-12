"""
`main.py` (Supaplex: New Era Engine)
------------------------------------------------

**This program is not affiliated with Supaplex.**

------------------------------------------------

Author: MF366 (Matthew)

Date: March 8th, 2025

License: GLPv3

Description: Runs the engine.
"""

import pygame
import const

from engine import tilemap

pygame.init()

clock = pygame.time.Clock()
game_running = True
# /-/ a = 0 # [i] Testing purposes

if __name__ == '__main__':
    # /-/ mymap = tilemap.Tilemap(5, 10)
    # /-/ mymap.print_tilemap() # only this one failed, but I'm fixing it already
    # /-/ print('\n\n')
    # /-/ mymap._test_a(
    # /-/     [
    # /-/         [1, 2, 3, 4, 5],
    # /-/         [6, 7, 8, 9, 10],
    # /-/         [11, 12, 13, 14, 15],
    # /-/         [16, 17, 18, 19, 20],
    # /-/         [21, 22, 23, 24, 25],
    # /-/         [26, 27, 28, 29, 30],
    # /-/     ]
    # /-/ )
    # /-/ print(mymap.get_line(3))
    # /-/ print(mymap.get_column(2))
    # /-/ print(mymap.get_coord(1, 4))
    # /-/ print(mymap.get_coord(5, 3))
    # /-/ print(mymap.get_coord(0, 2))
    # /-/ 
    # /-/ mymap.print_tilemap()

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        
        clock.tick(const.TICRATE)
        # /-/ a += 1
        # /-/ print(f'Tic #{a}')
        
    pygame.quit()
    print('Thanks for playing Supaplex: New Era Engine.')
    exit()
