from util.Fonts import Control


class Grid:
    def __init__(self, length, height, printer=lambda x: print(x), pre_draw=None, post_draw=None):
        self.length = length
        self.height = height
        self.grid = [[none_drawable] * length] * height
        self.fillers = []
        self._is_sorted = False
        self._sort_key = lambda f1, f2: f1.get_priority() < f2.get_priority()
        self.printer = printer
        self.pre_draw = pre_draw
        self.post_draw = post_draw

    def fill(self, drawable, i, j):
        self.grid[i][j] = drawable

    def register(self, filler):
        self._is_sorted = False
        self.fillers.append(filler)

    def draw(self):
        self.printer(Control.reset.value)
        self.printer(Control.clear_console)
        self.pre_draw(self.printer)
        for i in range(self.height):
            for j in range(self.length):
                assert self.grid[i][j] is not None
                self.grid[i][j].draw(self.printer)
        self.post_draw(self.printer)
        self.printer(Control.reset.value)


class Drawable:
    def __init__(self, character, *fonts):
        self.character = character
        self.fonts = fonts

    def draw(self, printer):
        for font in self.fonts:
            printer(font.value)
        printer(self.character)
        printer(Control.reset.value)


none_drawable = Drawable(' ')
