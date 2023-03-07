from PythonOPPTasks.PythonOPP_Exams.space_station.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_EXHAUSTED = 5

    def __init__(self, name, oxygen=70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.OXYGEN_EXHAUSTED
