from src.states.EnumState import EnumState
from src.states.State import State
from src.components.Tile import Tile, Button
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display

class GameWon(State):

    def __init__(self, board: list[list[Tile]]):
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#006F4CFF"))
        self.__board = board
        self.__flag_bombs()
        self.__buttons: list[Button] = [Button("PlayAgain",(100,630),(300,60),text = "Play again"),
                                 Button("Menu",(500,630),(300,60),text = "Menu"),
                                 Button("Quit",(900,630),(300,60),text = "Quit")]

    def __flag_bombs(self):
        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                if self.__board[x][y].get_is_mine():
                    self.__board[x][y].text = "!"

    def display(self):
        self._screen.blit(self.__background, (0, 0))
        
        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                self._draw_button(self.__board[x][y])

        for button in self.__buttons:
                self._draw_button(button)
                
        for current_event in event.get():
            for button in self.__buttons:
                self._draw_button(button)
                if button.rect.collidepoint(mouse.get_pos()):
                    if current_event.type == MOUSEBUTTONDOWN:
                        match button.get_target_name():
                            case "PlayAgain":
                                self._context.set_state(EnumState.GAME)
                            case "Menu":
                                self._context.set_state(EnumState.MENU)
                            case "Quit":
                                return False
                    button.hovered()
                else:
                    button.avoided()
            if current_event.type == QUIT:
                return False
        display.update()
        return True