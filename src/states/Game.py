from src.states.EnumState import EnumState
from src.states.State import State
from src.interfaces.Observer import Observer
from src.components.Tile import Tile, Button
from src.Difficulty import Difficulty
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display,time,font
from random import randint

class Game(State,Observer):

    def __init__(self, difficulty: Difficulty):
        self.__difficulty = difficulty
        self.__is_first_click = True
        self.__bombs_count = 10
        self.__init_board()
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#5B5B5BFF"))
        self.__buttons: list[Button] = [Button("Reset",(100,630),(300,60),text = "Reset"),
                                        Button("Menu",(900,630),(300,60),text = "Menu")]
        self.__timer = time.get_ticks()

    def __init_board(self):
        match self.__difficulty:
            case Difficulty.EASY: 
                self.__board = []
                rows = 9
                columns = 9
                self.__bombs_count = 10
                for r in range (0,rows,1):
                    self.__board.append([])
                    for c in range (0,columns,1):
                        self.__board[r].append(Tile(False, r, c))

            case Difficulty.MEDIUM:
                self.__board = []
                rows = 16
                columns = 16
                self.__bombs_count = 30
                for r in range (0,rows,1):
                    self.__board.append([])
                    for c in range (0,columns,1):
                        self.__board[r].append(Tile(False, r, c))

            case Difficulty.HARD:
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
                targeted_tile.set_tile_color()

                if targeted_tile.tile_state == -2:
                        self.__mine_explosion()

                
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
            
    def __on_click(self, coordinate, event):
        x, y = coordinate
        if event.button == 1 and self.__board[x][y].text == "":
            if self.__is_first_click:
                self.__place_random_bombs(coordinate)

            self.__reveal_tiles(coordinate)
            self.__check_board()

        elif event.button == 3:
            if self.__board[x][y].tile_state > -1 or self.__is_first_click:
                return
            else: 
                self.__board[x][y].switch_tag()

    def __check_board(self):
        check = "GameInProgress"

        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                if self.__board[x][y].tile_state == -1 or self.__board[x][y].tile_state == -3:
                    if self.__board[x][y].get_is_mine():
                        check = "GameWin"
                        continue

                    else:
                        check = "GameInProgress"
                        return

        if check == "GameWin":
            self.__on_board_complete()
    
    def __on_board_complete(self):
        self._context.board = self.__board
        self._context.set_state(EnumState.GAMEWON)
    
    def __on___mine_explosion(self):
        pass

    def __mine_explosion(self):
        self.__on___mine_explosion()
        self._context.board = self.__board
        self._context.set_state(EnumState.GAMELOST)

    def __place_random_bombs(self, coordinate):
        self.__is_first_click = False
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
        seconds = str((time.get_ticks() - self.__timer) / 1000)
        text_surface = self._fonts[1].render(seconds, False, (0, 0, 0))
        self._screen.blit(text_surface, (600,630))
        
        for button in self.__buttons:
                self._draw_button(button)

        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                self._draw_button(self.__board[x][y])
        
        for current_event in event.get():
            for x in range(len(self.__board)):
                for y in range(len(self.__board[x])):
                    if self.__board[x][y].rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            self.__on_click((x, y), current_event)
                            
                        self.__board[x][y].hovered()
                    else:
                        self.__board[x][y].avoided()

            for button in self.__buttons:
                if button.rect.collidepoint(mouse.get_pos()):
                    if current_event.type == MOUSEBUTTONDOWN:
                        match button.get_target_name():
                            case "Reset":
                                self._context.set_state(EnumState.GAME)
                            case "Menu":
                                self._context.set_state(EnumState.MENU)

                    button.hovered()
                else:
                    button.avoided()
            if current_event.type == QUIT:
                return False
        display.update()
        return True