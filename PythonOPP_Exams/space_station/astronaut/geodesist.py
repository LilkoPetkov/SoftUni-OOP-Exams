from PythonOPPTasks.PythonOPP_Exams.space_station.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name, oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.OXYGEN_EXHAUSTED
