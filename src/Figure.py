from abc import ABC, abstractmethod
class Figure(ABC):
    @property
    @abstractmethod
    def get_area(self):
        pass

    @property
    @abstractmethod
    def get_perimetr(self):
        pass


    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"{figure} not a Figure object")

        return self.get_area + figure.get_area

