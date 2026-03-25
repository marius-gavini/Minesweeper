from abc import abstractmethod
from src.interfaces.Observer import Observer

class State(Observer):

    _context = None

    def get_context(self):
        return self._context
    
    def set_context(self, context):
        self._context = context

    @abstractmethod
    def update(self, element = None):
        pass

    @abstractmethod
    def display(self):
        pass