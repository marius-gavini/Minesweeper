from src.states.EnumState import EnumState
from src.states.State import State
from src.components.Button import Button
from pygame import Surface,Color,event,mouse,MOUSEBUTTONDOWN,QUIT,display

class Menu(State):

    def __init__(self):
        self.__background = Surface((1300, 731))
        self.__background.fill(Color("#066895"))
        self.__difficulties = ["Easy","Medium","Hard"]
        self.__difficulties_colors = [(50,150,50),(50,50,150),(150,50,50),(100,50,50)]
        self.__difficulties_hover_colors = [(20,100,20),(20,20,100),(100,20,20),(50,20,20)]
        self.__difficulty_index = 1
        self.__buttons: list[Button] = [Button("Play",(500,444),(300,60),text = "Play"),
                                        Button("Difficulty",(500,524),(300,60),
                                                               text = self.__difficulties[self.__difficulty_index],
                                                               color = self.__difficulties_colors[self.__difficulty_index],
                                                               hover_color= self.__difficulties_hover_colors[self.__difficulty_index]),
                                         Button("Quit",(500,604),(300,60),text = "Quit")]

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
<<<<<<< Updated upstream
                                    self._context.set_state("Game")                             
=======
                                    self._context.difficulty = self.__difficulty
                                    self._context.set_state(EnumState.GAME)                       
>>>>>>> Stashed changes
                                case "Difficulty":
                                    self.__difficulty_index += 1
                                    if self.__difficulty_index > 2:
                                         self.__difficulty_index = 0
                                    self.__buttons[1] = Button("Difficulty",(500,524),(300,60),
                                                               text = self.__difficulties[self.__difficulty_index],
                                                               color = self.__difficulties_colors[self.__difficulty_index],
                                                               hover_color= self.__difficulties_hover_colors[self.__difficulty_index])
                                    self._context.difficulty = self.__difficulties[self.__difficulty_index]
                                case "Quit":
                                    return False
                        button.hovered()
                    else:
                        button.avoided()
                if current_event.type == QUIT:
                    return False
            display.update()
            return True