from src.states.EnumState import EnumState
from src.states.State import State
from src.components.Button import Button
from src.Difficulty import Difficulty
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display

class Menu(State):

    def __init__(self, difficulty : Difficulty = Difficulty.MEDIUM):
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#066895"))

        self.__difficulty = difficulty
        self.__difficulties_colors = {
                                        Difficulty.EASY : (50,150,50),
                                        Difficulty.MEDIUM : (50,50,150),
                                        Difficulty.HARD: (150,50,50)
                                     }
        self.__difficulties_hover_colors = {
                                        Difficulty.EASY : (20,100,20),
                                        Difficulty.MEDIUM : (20,20,100),
                                        Difficulty.HARD: (100,20,20)}
        
        self.__buttons: list[Button] = [Button("Play",(500,444),(300,60),text = "Play"),
                                        Button("Difficulty",(500,524),(300,60),
                                                               text = self.__difficulty.name.capitalize(),
                                                               color = self.__difficulties_colors[self.__difficulty],
                                                               hover_color= self.__difficulties_hover_colors[self.__difficulty]),
                                         Button("Quit",(500,604),(300,60),text = "Quit")]

    def display(self):
            self._screen.blit(self.__background, (0, 0))
            title = self._fonts[1].render('Mine Sweeper', False, (255, 255, 255))
            self._screen.blit(title, (490,200))
            for button in self.__buttons:
                    self._draw_button(button)
                    
            for current_event in event.get():
                for button in self.__buttons:
                    self._draw_button(button)
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "Play":                     
                                    self._context.difficulty = self.__difficulty
                                    self._context.set_state(EnumState.GAME)                     
                                case "Difficulty":
                                    if self.__difficulty.value < 3:
                                        self.__difficulty = Difficulty(self.__difficulty.value + 1)
                                    else:
                                         self.__difficulty = Difficulty(1)
                                    self.__buttons[1] = Button("Difficulty",(500,524),(300,60),
                                                               text = self.__difficulty.name.capitalize(),
                                                               color = self.__difficulties_colors[self.__difficulty],
                                                               hover_color= self.__difficulties_hover_colors[self.__difficulty])
                                case "Quit":
                                    return False
                        button.hovered()
                    else:
                        button.avoided()
                if current_event.type == QUIT:
                    return False
            display.update()
            return True