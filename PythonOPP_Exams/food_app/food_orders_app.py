from PythonOPPTasks.PythonOPP_Exams.food_app.client import Client
from PythonOPPTasks.horse_racing.project import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def __is_registered(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True

    def __get_client(self, phone_number):
        for c in self.clients_list:
            if c.phone_number == phone_number:
                return c

    def register_client(self, client_phone_number):
        if client_phone_number in self.clients_list:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)

        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ != "Starter" and meal.__class__.__name__ != "MainDish" and meal.__class__.__name__ != "Dessert":
                continue
            self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = []

        for item in self.menu:
            result.append(item.details())

        return '\n'.join(s for s in result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities: dict):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        meals_to_order = []
        current_bill = 0
        current_meal_quantity = 0
        client = self.__get_client(client_phone_number)

        if client not in self.clients_list:
            self.clients_list.append(client)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= meal_quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * meal_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill
        client.ordered_meals_quantity += current_meal_quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in meals_to_order)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.__get_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        client.bill = 0
        client.shopping_cart = []

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.__get_client(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        temp_bill = client.bill

        client.bill = 0
        client.shopping_cart = []
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {temp_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
