from src.interfaces.Subject import Subject
from src.interfaces.Observer import Observer
from src.components.Button import Button

class Tile(Subject, Button):

    def __init__(self, is_mine: bool, x_index: int, y_index: int):
        Button.__init__(self, target_name=f"{x_index}-{y_index}",lefttop=(x_index*20,y_index*20), widthheight=(20,20))
        
        self.__x_index = x_index
        self.__y_index = y_index

        self.__observers: list[Observer] = []
        self.__is_mine: bool = is_mine
        self.tile_state: int = -1
    
    def check_tile_value(self, board: list[list[Tile]], coordinate: tuple):
        
        y, x = coordinate
        targeted_tile: Tile = board[y][x]

        if targeted_tile.get_is_mine() == True:
            targeted_tile.tile_state = -2
            return 
            
        mine_number = 0
        height = len(board)
        width = len(board[0])

        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue

                ny, nx = y + dy, x + dx
            
                if 0 <= ny < height and 0 <= nx < width:
                    if board[ny][nx].get_is_mine():
                        mine_number += 1

        targeted_tile.tile_state = mine_number

    def reveal(self):
        pass

    def get_is_mine(self):
        self.__is_mine

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        for observer in self.__observers:
            self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()

    def get_y_index(self):
        return self.__y_index
    
    def get_x_index(self):
        return self.__x_index
    
    def __set_tile_state(self):
        pass

    def __reveal(self):
        pass

    def __on_reveal(self):
        pass

    def __on_put_flag(self):
        pass

    def __on_put_question_mark(self):
        pass

    def __on_remove_indication(self):
        pass