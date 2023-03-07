from project_2_exam import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        P = None

        for p in self.planets:
            if p.name == name:
                P = p # P exists in the list
                break

        return P
