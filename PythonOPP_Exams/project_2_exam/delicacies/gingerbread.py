from PythonOPPTasks.PythonOPP_Exams.project_2_exam.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name, price, portion=200):
        super().__init__(name, portion, price)
        self.portion = 200

    def details(self):
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."
