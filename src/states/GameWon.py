from src.states.State import State, Observer
from src.interfaces.Subject import Subject

class GameWon(State,Subject):

    def __init__(self):
        self.__observers: list[Observer] = []

    def update(self, element = None):
        pass

    def display(self):
        pass

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        for observer in self.__observers:
            self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update()