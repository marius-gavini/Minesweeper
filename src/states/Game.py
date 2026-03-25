from src.states.State import State, Observer
from src.interfaces.Subject import Subject
from src.components.Tile import Tile, Button
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display
from random import randint

class Game(State,Subject):

    def __init__(self):
        self.__observers: list[Observer] = []
        self.__init_board()
        self.is_first_click = True
        self.difficulty = "easy"
        self.bombs = None
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#5B5B5BFF"))
        self.__buttons: list[Button] = [Button("Reveal",(500,344),(300,60),text = "Reveal 0,1 tile"),
                                        Button("Win",(500,444),(300,60),text = "Win"),
                                        Button("Lose",(500,524),(300,60),text = "Lose"),
                                        Button("Quit",(500,604),(300,60),text = "Quit")]

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

    def reveal_tiles(self, coordinate: tuple):
        y, x = coordinate
        height = len(self.__board)
        width = len(self.__board[0])

        if 0 <= y < height and 0 <= x < width:
            targeted_tile: Tile = self.__board[y][x]
            if targeted_tile.tile_state == -1:
                targeted_tile.check_tile_value(self.__board, (y, x))
                targeted_tile.reveal()

                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if targeted_tile.tile_state == 0:
                                if dy == 0 and dx == 0:
                                    continue
                    
                                ny, nx = y + dy, x + dx
                                if 0 <= ny < height and 0 <= nx < width:
                                    self.reveal_tiles((ny, nx))

                        else:
                            return
            else: 
                return 
            
    def place_random_bombs(self, coordinate):
        self.is_first_click = False
        y, x = coordinate
        i = 0

        while i < self.bombs:
            ry = randint(len(self.__board))
            rx = randint(len(self.__board[0]))

            if (ry, rx) == (y, x):
                continue

            elif self.__board[ry][rx].mine :
                continue

            else:   
                i += 1
                self.__board[ry][rx].mine == True

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
        self._screen.blit(self.__background, (0, 0))

        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                self._draw_button(self.__board[x][y])

        for button in self.__buttons:
                self._draw_button(button)

        for current_event in event.get():
            for button in self.__buttons:
                if button.rect.collidepoint(mouse.get_pos()):
                    if current_event.type == MOUSEBUTTONDOWN:
                        match button.get_target_name():
                            case "Reveal":
                                res = self.reveal_tiles((0, 1))
                                print(res)
                            case "Win":
                                self._context.set_state("GameWon")
                                return self._context.display()
                            case "Lose":
                                self._context.set_state("GameLost")
                                return self._context.display()
                            case "Quit":
                                return False
                    button.hovered()
                else:
                    button.avoided()
                    
            for x in range(len(self.__board)):
                for y in range(len(self.__board[x])):
                    if self.__board[x][y].rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            res = self.reveal_tiles((x, y))
                            print(res)
                        self.__board[x][y].hovered()
                    else:
                        self.__board[x][y].avoided()
            if current_event.type == QUIT:
                return False
        display.update()
        return True