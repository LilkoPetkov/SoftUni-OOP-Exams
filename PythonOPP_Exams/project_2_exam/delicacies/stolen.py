from PythonOPPTasks.PythonOPP_Exams.project_2_exam.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name, price, portion=250):
        super().__init__(name, portion, price)
        self.portion = 250

    def details(self):
        return f"Stolen {self.name}: 250g - {self.price:.2f}lv."
