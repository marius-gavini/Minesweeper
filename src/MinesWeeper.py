from src.states.State import State

class MinesWeeper:
    __state = None

    def __init__(self, state: State) -> None:
        self.set_state(state)        


    def set_state(self, state: State):
        self.__state = state
        self.__state.set_context(self)


    def display(self):
        self.__state.display()