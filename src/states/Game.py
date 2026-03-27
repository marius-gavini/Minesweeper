from src.states.State import State
from src.interfaces.Observer import Observer
from src.components.Tile import Tile, Button
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display
from random import randint

class Game(State,Observer):

    def __init__(self, difficulty: str):
        self.__difficulty = difficulty
        self.is_first_click = True
        self.__bombs_count = 10
        self.__init_board()
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#5B5B5BFF"))
        self.__buttons: list[Button] = [Button("Reveal",(500,344),(300,60),text = "Reveal 0,1 tile"),
                                        Button("Win",(500,444),(300,60),text = "Win"),
                                        Button("Lose",(500,524),(300,60),text = "Lose"),
                                        Button("Quit",(500,604),(300,60),text = "Quit")]
        

    def __init_board(self):
        match self.__difficulty:
            case "Easy": 
                self.__board = []
                rows = 9
                columns = 9
                self.__bombs_count = 10
                for r in range (0,rows,1):
                    self.__board.append([])
                    for c in range (0,columns,1):
                        self.__board[r].append(Tile(False, r, c))

            case "Medium":
                self.__board = []
                rows = 16
                columns = 16
                self.__bombs_count = 30
                for r in range (0,rows,1):
                    self.__board.append([])
                    for c in range (0,columns,1):
                        self.__board[r].append(Tile(False, r, c))

            case "Hard":
                self.__board = []
                rows = 32
                columns = 16
                self.__bombs_count = 99
                for r in range (0,rows,1):
                    self.__board.append([])
                    for c in range (0,columns,1):
                        self.__board[r].append(Tile(False, r, c))
            case _:
                print("error")

    def __reveal_tiles(self, coordinate: tuple):
        y, x = coordinate
        height = len(self.__board)
        width = len(self.__board[0])

        if 0 <= y < height and 0 <= x < width:
            targeted_tile: Tile = self.__board[y][x]
            if targeted_tile.tile_state == -1:
                targeted_tile.check_tile_value(self.__board, (y, x))
                targeted_tile.reveal()

                if targeted_tile.tile_state == -2:
                        self.mine_explosion()

                
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if targeted_tile.tile_state == 0:
                            if dy == 0 and dx == 0:
                                continue
                
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < height and 0 <= nx < width:
                                self.__reveal_tiles((ny, nx))

                        else:
                            return
            else: 
                return 
            
    def on_click(self, coordinate, event):
        x, y = coordinate
        if event.button == 1 and self.__board[x][y].text == "":
            if self.is_first_click:
                self.place_random_bombs(coordinate)

            self.__reveal_tiles(coordinate)
            self.check_board()

        elif event.button == 3:
            if self.__board[x][y].tile_state != -1:
                return
            else: 
                self.__board[x][y].switch_tag()

    def check_board(self):
        check = "GameInProgress"

        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                
                if self.__board[x][y].tile_state != -1 or (self.__board[x][y].tile_state == -1 and self.__board[x][y].get_is_mine() == True):
                    check = "GameWin"

                else:
                    check= "GameInProgress"
                    break

        if check == "GameWin":
            self.on_board_complete()
    
    def on_board_complete(self):
        self._context.set_state("GameWon")
    
    def on_mine_explosion(self):
        pass

    def mine_explosion(self):

        self.on_mine_explosion()

        self._context.set_state("GameLost")

    def place_random_bombs(self, coordinate):
        self.is_first_click = False
        y, x = coordinate
        i = 0

        while i < self.__bombs_count:
            ry = randint(0, (len(self.__board) - 1))
            rx = randint(0, (len(self.__board[0]) - 1))

            if (ry, rx) == (y, x):
                continue

            elif self.__board[ry][rx].get_is_mine() :
                continue

            else:   
                i += 1
                self.__board[ry][rx].set_is_mine(True)

    def update(self, element = None):
        pass

    def display(self):
        self._screen.blit(self.__background, (0, 0))

        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                self._draw_button(self.__board[x][y])

        for current_event in event.get():
            for x in range(len(self.__board)):
                for y in range(len(self.__board[x])):
                    if self.__board[x][y].rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            self.on_click((x, y), current_event)
                        self.__board[x][y].hovered()
                    else:
                        self.__board[x][y].avoided()
            if current_event.type == QUIT:
                return False
        display.update()
        return True