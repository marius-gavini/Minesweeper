from src.states.State import State
from src.states.Menu import Menu
from src.states.Game import Game
from src.states.GameWon import GameWon
from src.states.GameLost import GameLost
from src.Constants import FONT_PATH
import pygame 

class MinesWeeper:
    __state = None

    def __init__(self, state: State) -> None:
        
        pygame.init()
        pygame.display.set_caption('MineSweeper')

        self.__screen = pygame.display.set_mode((1300, 731))
        self.__clock = pygame.time.Clock()
        self.__fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50), pygame.font.Font(FONT_PATH, 20)
        
        self.set_state(state)     

    def get_screen(self):
        return self.__screen
    
    def get_clock(self):
        return self.__clock
    
    def get_fonts(self):
        return self.__fonts

    def set_state(self, state: str):
        match state:
            case "Menu":
                self.__state = Menu()
            case "Game":
                self.__state = Game()
            case "GameWon":
                self.__state = GameWon()
            case "GameLost":
                self.__state = GameLost()
            case _:
                self.__state = Menu()

        self.__state.set_context(self)

    def display(self):
        running = True
        while running:
            running = self.__state.display()