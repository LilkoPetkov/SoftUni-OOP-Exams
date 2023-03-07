from PythonOPPTasks.PythonOPP_Exams.project.player import Player
from PythonOPPTasks.PythonOPP_Exams.project.supply.drink import Drink
from PythonOPPTasks.PythonOPP_Exams.project.supply.food import Food
from PythonOPPTasks.PythonOPP_Exams.project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args: Player):
        if args:
            added_players = []
            for player in args:
                if player in self.players:
                    continue
                self.players.append(player)
                added_players.append(player.name)

            return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = None
        food = None
        drink = None

        for p in self.players:
            if player_name == p.name:
                player = p
                break

        if not player or sustenance_type != "Food" or sustenance_type != "Drink":
            return None

        if sustenance_type == "Food":
            for s in self.supplies[::-1]:
                if s.__class__.__name__ == "Food":
                    food = s
                    break

        if sustenance_type == "Drink":
            for d in self.supplies[::-1]:
                if d.__class__.__name__ == "Drink":
                    drink = d
                    break

        if sustenance_type == "Food" and not food:
            raise Exception("There are no food supplies left!")
        if sustenance_type == "Drink" and not drink:
            raise Exception("There are no drink supplies left!")

        if player:
            if player.stamina == 100:
                return f"{player_name} have enough stamina."
            elif food:
                if player.stamina + food.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += food.energy

                food_name = food.name
                self.supplies.reverse()
                self.supplies.remove(food)
                self.supplies.reverse()
                return f"{player_name} sustained successfully with {food_name}."

            elif drink:
                if player.stamina + drink.energy > 100:
                    player.stamina = 100
                else:
                    player.stamina += drink.energy

                drink_name = drink.name
                self.supplies.reverse()
                self.supplies.remove(drink)
                self.supplies.reverse()
                return f"{player_name} sustained successfully with {drink_name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina.\nPlayer {second_player.name} does not " \
                   f"have enough stamina."
        elif first_player.stamina == 0:
            return f"Player {first_player.name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player.name} does not have enough stamina."

        if first_player.stamina < second_player.stamina:
            if second_player.stamina - (first_player.stamina / 2) < 0:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"
            second_player.stamina -= (first_player.stamina / 2)

            if first_player.stamina - (second_player.stamina / 2) < 0:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"
            first_player.stamina -= (second_player.stamina / 2)
        else:
            if first_player.stamina - (second_player.stamina / 2) < 0:
                first_player.stamina = 0
                return f"Winner: {second_player.name}"
            first_player.stamina -= (second_player.stamina / 2)

            if second_player.stamina - (first_player.stamina / 2) < 0:
                second_player.stamina = 0
                return f"Winner: {first_player.name}"
            second_player.stamina -= (first_player.stamina / 2)

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"
        else:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) < 0:
                p.stamina = 0
            else:
                p.stamina -= (p.age * 2)

        for p in self.players:
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = []

        for player in self.players:
            result.append(player)
        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(str(s) for s in result)


c = Controller()
c.add_player(Player("test", 26, 26), Player("T", 20, 56))
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
c.add_supply(cheese, apple, cheese, apple, juice, water, water)
print(c.sustain("Te", "Food"))
