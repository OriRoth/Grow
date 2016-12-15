from util.Fonts import Control


class Grid:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.grid = [[none_drawable for _ in range(length)] for _ in range(height)]
        self.fillers = []
        self.claims = [[None for _ in range(length)] for _ in range(height)]
        self._is_sorted = False
        self._sort_key = lambda f: -f.get_priority()

    def fill(self, drawable, i, j):
        self.grid[i][j] = drawable

    def fill_n_claim(self, owner, drawable, i, j):
        self.grid[i][j] = drawable
        self.claims[i][j] = owner

    def register(self, filler):
        self._is_sorted = False
        self.fillers.append(filler)

    def _commit(self):
        if not self._is_sorted:
            self.fillers = sorted(self.fillers, key=self._sort_key)
            self._is_sorted = True
        for filler in self.fillers:
            filler.fill(self)

    def draw(self):
        self._commit()
        res = ''
        res += Control.reset.value
        res += Control.clear_console.value
        for i in range(self.height):
            for j in range(self.length):
                assert self.grid[i][j] is not None
                res += self.grid[i][j].draw()
            res += '\n'
        res += Control.reset.value
        return res

    def available(self, i, j):
        return 0 <= i < self.height and 0 <= j < self.length and not self.claims[i][j]


class Drawable:
    def __init__(self, character, *fonts):
        self.character = character
        self.fonts = fonts

    def draw(self):
        res = ''
        for font in self.fonts:
            res += font.value
        res += self.character
        if len(self.fonts) > 0:
            res += Control.reset.value
        return res


none_drawable = Drawable(' ')
