from PythonOPPTasks.PythonOPP_Exams.project_2_exam.booths.open_booth import OpenBooth
from PythonOPPTasks.PythonOPP_Exams.project_2_exam.booths.private_booth import PrivateBooth
from PythonOPPTasks.PythonOPP_Exams.project_2_exam.delicacies.gingerbread import Gingerbread
from PythonOPPTasks.PythonOPP_Exams.project_2_exam.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{delicacy.name} already exists!")

        if type_delicacy != "Gingerbread" and type_delicacy != "Stolen":
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == "Gingerbread":
            self.delicacies.append(Gingerbread(name, price))
        elif type_delicacy == "Stolen":
            self.delicacies.append(Stolen(name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth != "Open Booth" and type_booth != "Private Booth":
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == "Open Booth":
            self.booths.append(OpenBooth(booth_number, capacity))
        elif type_booth == "Private Booth":
            self.booths.append(PrivateBooth(booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        available_booth = None

        for booth in self.booths:
            if booth.is_reserved == False and booth.capacity >= number_of_people:
                available_booth = booth
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        if available_booth is None:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        current_booth = None
        current_delicacy = None

        for booth in self.booths:
            if booth.booth_number == booth_number:
                current_booth = booth
        for delicacy in self.delicacies:
            if delicacy.name == delicacy_name:
                current_delicacy = delicacy

        if current_booth is None:
            raise Exception(f"Could not find booth {booth_number}!")
        if current_delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        current_booth.delicacy_orders.append(current_delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_booth = [booth for booth in self.booths if booth.booth_number == booth_number][0]
        current_total_bill = 0

        for delicacy in current_booth.delicacy_orders:
            current_total_bill += delicacy.price
        current_total_bill += current_booth.price_for_reservation
        self.income += current_total_bill

        current_booth.delicacy_orders = []
        current_booth.is_reserved = False
        current_booth.price_for_reservation = 0

        return '\n'.join([
            f"Booth {booth_number}:",
            f"Bill: {current_total_bill:.2f}lv."
                ])

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
