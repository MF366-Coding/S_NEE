"""
`tilemap.py` (Supaplex: New Era Engine)
------------------------------------------------

**This program is not affiliated with Supaplex.**

------------------------------------------------

Author: MF366 (Matthew)

Date: March 12th, 2025

License: GLPv3

Description: Store the data required for the tilemap.
"""

from typing import NoReturn


class Tilemap:
    def __init__(self, width: int, height: int):        
        self._tilemap: list[list[int]] = [[0] * width for _ in range(height)]
        
    def get_line(self, tx: int):
        return self._tilemap[tx].copy()
    
    def get_column(self, ty: int):
        return [i[ty] for i in self._tilemap]
    
    def get_coord(self, tx: int, ty: int):
        return self.get_line(tx)[ty]
    
    def load_level(self) -> NoReturn:
        raise NotImplementedError('TODO') # TODO
    
    def _test_a(self, new_tilemap: list[list[int]]) -> None:
        self._tilemap = new_tilemap
        
    def print_tilemap(self) -> None:
        for i in self._tilemap:
            print(i)


if __name__ == "__main__":
    mymap = Tilemap(5, 10)
    mymap.print_tilemap() # only this one failed, but I'm fixing it already
    print('\n\n')
    mymap._test_a(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
        ]
    )
    print(mymap.get_line(3))
    print(mymap.get_column(2))
    print(mymap.get_coord(1, 4))
    print(mymap.get_coord(5, 3))
    print(mymap.get_coord(0, 2))
    
    mymap.print_tilemap()
