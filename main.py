from src.MinesWeeper import MinesWeeper
from src.states.Menu import Menu

if __name__ == "__main__":
    minesweeper = MinesWeeper(Menu())
    minesweeper.display()