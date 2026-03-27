from src.states.EnumState import EnumState
from src.states.Menu import Menu
from src.states.Game import Game
from src.states.GameWon import GameWon
from src.states.GameLost import GameLost
from src.Constants import FONT_PATH
from src.Difficulty import Difficulty
import pygame 

class MinesWeeper:
    __state = None

    def __init__(self, state: EnumState) -> None:
        
        pygame.init()
        pygame.display.set_caption('MineSweeper')

        self.__screen = pygame.display.set_mode((1300, 731))
        self.__clock = pygame.time.Clock()
        self.__fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50), pygame.font.Font(FONT_PATH, 20)
        
        self.difficulty = Difficulty.MEDIUM
        self.board = None

        self.set_state(state)     

    def get_screen(self):
        return self.__screen
    
    def get_clock(self):
        return self.__clock
    
    def get_fonts(self):
        return self.__fonts

    def set_state(self, state: EnumState):
        match state:
            case EnumState.MENU:
                self.__state = Menu(self.difficulty)
            case EnumState.GAME:
                self.__state = Game(self.difficulty)
            case EnumState.GAMEWON:
                self.__state = GameWon(self.board)
            case EnumState.GAMELOST:
                self.__state = GameLost(self.board)
            case _:
                self.__state = Menu(self.difficulty)
        self.__state.set_context(self)

    def display(self):
        running = True
        while running:
            running = self.__state.display()