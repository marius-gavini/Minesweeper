from src.MinesWeeper import MinesWeeper
from src.states.Menu import Menu
from src.states.Game import Game

if __name__ == "__main__":
    minesweeper = MinesWeeper(Game())
    minesweeper.display()