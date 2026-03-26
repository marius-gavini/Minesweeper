from abc import abstractmethod
from src.components.Button import Button
from pygame import Surface, time, font

class State:

    _context = None
    _screen = None
    _clock = None
    _fonts = None

    def get_context(self):
        return self._context
    
    def set_context(self, context):
        self._context = context
        self._screen: Surface = context.get_screen()
        self._clock: time.Clock = context.get_clock()
        self._fonts: tuple[font.Font] = context.get_fonts()

    def _draw_button(self, button: Button):
        if button.get_bg_image() != None and button.get_hover_bg_image() != None:
            surface = button.current_bg_image

        else:
            surface = Surface((button.widthheight))
            surface.fill(button.current_color)

        if button.text != "":
            text_surf = self._fonts[0].render(button.text, True, button.current_font_color)
            surface.blit(text_surf, text_surf.get_rect(center = surface.get_rect().center))

        self._screen.blit(surface, button.lefttop)
        
    @abstractmethod
    def display(self):
        pass