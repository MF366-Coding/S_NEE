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

pygame.init()

clock = pygame.time.Clock()
game_running = True
# /-/ a = 0 # [i] Testing purposes

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
