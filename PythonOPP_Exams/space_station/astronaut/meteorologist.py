from PythonOPPTasks.PythonOPP_Exams.space_station.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_EXHAUSTED = 15

    def __init__(self, name, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.OXYGEN_EXHAUSTED
