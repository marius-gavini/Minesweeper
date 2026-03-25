from src.states.State import State, Observer
from src.interfaces.Subject import Subject
from src.components.Tile import Tile

class Game(State,Subject):

    def __init__(self):
        self.__observers: list[Observer] = []
        self.__init_board()

    def __init_board(self):
        self.__board: list[list[Tile]] = [
            [Tile(False, 0, 0), Tile(False, 0, 1), Tile(False, 0, 2), Tile(False, 0, 3), Tile(False, 0, 4), Tile(False, 0, 5), Tile(False, 0, 6), Tile(True, 0, 7), Tile(False, 0, 8)],
            [Tile(False, 1, 0), Tile(False, 1, 1), Tile(False, 1, 2), Tile(False, 1, 3), Tile(False, 1, 4), Tile(False, 1, 5), Tile(True, 1, 6), Tile(False, 1, 7), Tile(False, 1, 8)],
            [Tile(False, 2, 0), Tile(False, 2, 1), Tile(False, 2, 2), Tile(False, 2, 3), Tile(False, 2, 4), Tile(False, 2, 5), Tile(False, 2, 6), Tile(False, 2, 7), Tile(False, 2, 8)],
            [Tile(False, 3, 0), Tile(True, 3, 1), Tile(True, 3, 2), Tile(False, 3, 3), Tile(False, 3, 4), Tile(False, 3, 5), Tile(False, 3, 6), Tile(False, 3, 7), Tile(False, 3, 8)],
            [Tile(True, 4, 0), Tile(False, 4, 1), Tile(False, 4, 2), Tile(False, 4, 3), Tile(False, 4, 4), Tile(False, 4, 5), Tile(False, 4, 6), Tile(False, 4, 7), Tile(False, 4, 8)],
            [Tile(False, 5, 0), Tile(False, 5, 1), Tile(False, 5, 2), Tile(False, 5, 3), Tile(False, 5, 4), Tile(True, 5, 5), Tile(False, 5, 6), Tile(False, 5, 7), Tile(False, 5, 8)],
            [Tile(False, 6, 0), Tile(False, 6, 1), Tile(False, 6, 2), Tile(False, 6, 3), Tile(False, 6, 4), Tile(False, 6, 5), Tile(True, 6, 6), Tile(False, 6, 7), Tile(False, 6, 8)],
            [Tile(False, 7, 0), Tile(False, 7, 1), Tile(False, 7, 2), Tile(False, 7, 3), Tile(False, 7, 4), Tile(False, 7, 5), Tile(False, 7, 6), Tile(False, 7, 7), Tile(True, 7, 8)],
            [Tile(True, 8, 0), Tile(False, 8, 1), Tile(False, 8, 2), Tile(False, 8, 3), Tile(True, 8, 4), Tile(False, 8, 5), Tile(False, 8, 6), Tile(False, 8, 7), Tile(False, 8, 8)]
        ]

    def __check_tile_value(self, coordinate: tuple):
        y, x = coordinate
        targeted_tile: Tile = self.__board[y][x]

        if targeted_tile.get_is_mine() == True:
            targeted_tile.tile_state = -2
            return 
            
        mine_number = 0
        height = len(self.__board)
        width = len(self.__board[0])

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue

                ny, nx = y + dy, x + dx

                if 0 <= ny < height and 0 <= nx < width:
                    if self.__board[ny][nx].get_is_mine():
                        mine_number += 1

        targeted_tile.tile_state = mine_number

    def __reveal_tiles(self):
        pass

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        for observer in self.__observers:
            self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()

    def update(self, element = None):
        pass

    def display(self):
        pass