class Students:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

anna = Students('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.average())