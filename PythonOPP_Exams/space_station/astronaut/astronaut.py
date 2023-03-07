from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_EXHAUSTED = 10

    def __init__(self, name, oxygen=0):
        self.name = name
        self. oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= self.OXYGEN_EXHAUSTED

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
