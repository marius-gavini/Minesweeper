from src.states.State import State
from src.components.Button import Button
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display

class Menu(State):

    def __init__(self):
        self.__buttons: list[Button] = [Button("Play",(500,444),(300,60),text = "Play"),
                                 Button("Difficulty",(500,524),(300,60),text = "Change difficulty"),
                                 Button("Quit",(500,604),(300,60),text = "Quit")]
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#066895"))

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