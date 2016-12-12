from abc import abstractmethod


class Filler:
    @abstractmethod
    def fill(self, grid):
        pass

    @abstractmethod
    def get_priority(self):
        return 0
