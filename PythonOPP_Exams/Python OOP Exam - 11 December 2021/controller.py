from project_2_exam import MuscleCar
from project_2_exam import SportsCar
from project_2_exam import Driver
from project_2_exam import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar" or car_type == "SportsCar":
            if car_type == "MuscleCar":
                self.cars.append(MuscleCar(model, speed_limit))
            elif car_type == "SportsCar":
                self.cars.append(SportsCar(model, speed_limit))

            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for d in self.drivers:
            if d.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for r in self.races:
            if r.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = None
        car = None

        for d in self.drivers:
            if d.name == driver_name:
                driver = d
                break
        for c in self.cars[::-1]:
            if c.__class__.__name__ == car_type:
                car = c
                if not c.is_taken:
                    break

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_model = driver.car.model
            driver.car.is_taken = False
            driver.car = car
            driver.car.is_taken = True

            return f"Driver {driver.name} changed his car from {old_model} to {car.model}."

        if not car.is_taken:
            driver.car = car
            car.is_taken = True

            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = None
        driver = None

        for r in self.races:
            if r.name == race_name:
                race = r
        for d in self.drivers:
            if d.name == driver_name:
                driver = d

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        qualified_driver_names = []
        people_qualified = 0
        race = None
        drivers = []
        temp_dict = {}
        result = []

        for r in self.races:
            if r.name == race_name:
                race = r

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        for d in race.drivers:
            drivers.append(d)
        for driver in drivers:
            driver.number_of_wins += 1

            temp_dict[driver.name] = driver.car.speed_limit

        sorted_dict = sorted(temp_dict.items(), key=lambda x: -x[1])

        for key, value in sorted_dict:
            if people_qualified == 3:
                break
            result.append(f"Driver {key} wins the {race_name} race with a speed of {value}.")
            qualified_driver_names.append(key)

            people_qualified += 1

        for d in race.drivers:
            if d.name not in qualified_driver_names:
                d.number_of_wins -= 1

        return "\n".join(result)


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]
