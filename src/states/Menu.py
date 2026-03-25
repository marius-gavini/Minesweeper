from src.states.State import State, Observer
from src.interfaces.Subject import Subject
from src.components.Button import Button
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display

class Menu(State,Subject):

    def __init__(self):
        self.__observers: list[Observer] = []
        self.__buttons: list[Button] = [Button("Play",(500,444),(300,60),text = "Play"),
                                 Button("Difficulty",(500,524),(300,60),text = "Change difficulty"),
                                 Button("Quit",(500,604),(300,60),text = "Quit")]
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#066895"))

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
            for button in self.__buttons:
                    self._draw_button(button)
            for current_event in event.get():
                for button in self.__buttons:
                    self._draw_button(button)
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "Play":
                                    self._context.set_state("Game")
                                    return self._context.display()
                                case "Difficuly":
                                    pass
                                case "Quit":
                                    return False
                        button.hovered()
                    else:
                        button.avoided()
                if current_event.type == QUIT:
                    return False
            display.update()
            return True