from src.components.Button import Button

class Tile(Button):

    def __init__(self, is_mine: bool, x_index: int, y_index: int, board_coordinate: tuple):
        Button.__init__(self, target_name=f"{x_index}-{y_index}",lefttop=board_coordinate, widthheight=(30,30), color=(83, 84, 84))
        
        self.__x_index = x_index
        self.__y_index = y_index

        self.__is_mine: bool = is_mine
        self.tile_state: int = -1

        self.__tags = ["","!","?"]
        self.__tags_index = 0
        self.__colors = [(125, 125, 125), (5, 45, 110), (7, 110, 5), (209, 6, 6), (2, 1, 51), (51, 1, 1), (4, 201, 192), (24, 59, 57), (0, 0, 0)]

    def set_tile_color(self):
        if self.tile_state >= 0:
            Button.set_color(self, self.__colors[self.tile_state])

    def set_board_coordinate(self, coordinate_index):
        Button.lefttop = self.__coordinate[coordinate_index]

    def switch_tag(self):
        self.__tags_index += 1
        
        if self.__tags_index == 1:
            self.tile_state = -3
        else:
            self.tile_state = -1
            if self.__tags_index > 2:
                self.__tags_index = 0 
            
        self.text = str(self.__tags[self.__tags_index])

    def check_tile_value(self, board, coordinate: tuple):
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
        self.text = str(self.tile_state)

    def get_is_mine(self):
        return self.__is_mine

    def set_is_mine(self, is_mine):
        self.__is_mine = is_mine