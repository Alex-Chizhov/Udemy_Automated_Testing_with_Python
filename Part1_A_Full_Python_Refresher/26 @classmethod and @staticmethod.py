class Students:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school")

    @classmethod
    def go_to_home(cls):
        print("I'm going to home")



anna = Students('Anna', 'MIT')

anna.go_to_school()
Students.go_to_school()

anna.go_to_home()
Students.go_to_home()