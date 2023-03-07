from PythonOPPTasks.PythonOPP_Exams.space_station.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astronaut = None

        for a in self.astronauts:
            if a.name == name:
                astronaut = a
                break

        if astronaut:
            return astronaut
