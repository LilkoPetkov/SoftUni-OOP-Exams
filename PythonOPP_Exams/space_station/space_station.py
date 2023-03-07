from PythonOPPTasks.PythonOPP_Exams.space_station.astronaut.astronaut_repository import AstronautRepository
from project_2_exam import Biologist
from PythonOPPTasks.PythonOPP_Exams.space_station.astronaut.geodesist import Geodesist
from PythonOPPTasks.PythonOPP_Exams.space_station.astronaut.meteorologist import Meteorologist
from project_2_exam import Planet
from PythonOPPTasks.PythonOPP_Exams.space_station.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                return f"{name} is already added."

        if astronaut_type != "Biologist" and astronaut_type != "Geodesist" and astronaut_type != "Meteorologist":
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == "Biologist":
            self.astronaut_repository.add(Biologist(name))
        elif astronaut_type == "Geodesist":
            self.astronaut_repository.add(Geodesist(name))
        elif astronaut_type == "Meteorologist":
            self.astronaut_repository.add(Meteorologist(name))

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        for p in self.planet_repository.planets:
            if p.name == name:
                return f"{name} is already added."

        split_items = items.split(", ")

        self.planet_repository.add(Planet(name))

        planet_object = self.planet_repository.find_by_name(name)
        planet_object.items = split_items

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(self.astronaut_repository.find_by_name(name))
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        ASTRONAUT_LIMIT = 5
        astronaut_count = 0
        astronauts_visited = []
        suitable_astronauts = []

        if not planet:
            raise Exception("Invalid planet name!")

        for a in self.astronaut_repository.astronauts:
            if a.oxygen > 30 and len(suitable_astronauts) <= ASTRONAUT_LIMIT:
                suitable_astronauts.append(a)

        if len(suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_suitable_astronauts = sorted(suitable_astronauts, key=lambda x: -x.oxygen)

        for astronaut in sorted_suitable_astronauts:
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

                if astronaut not in astronauts_visited:
                    astronaut_count += 1
                astronauts_visited.append(astronaut)

        if len(planet.items) == 0:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {astronaut_count} astronauts participated in collecting items."

        self.unsuccessful_missions += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.successful_missions} successful missions!",
                 f"{self.unsuccessful_missions} missions were not completed!",
                 f"Astronauts' info:"]

        for a in self.astronaut_repository.astronauts:
            result.append(f"Name: {a.name}")
            result.append(f"Oxygen: {a.oxygen}")

            if len(a.backpack) > 0:
                result.append(f"Backpack items: {', '.join(a.backpack)}")
            else:
                result.append("none")

        return '\n'.join(result)
