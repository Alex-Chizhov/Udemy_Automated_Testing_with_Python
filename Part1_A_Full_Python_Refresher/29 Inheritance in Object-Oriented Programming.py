class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = [1,2]

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent('Anna','Oxford', 20000)
print(anna.name, anna.school, anna.salary )

friend = WorkingStudent.friend(anna, 'Greg', 18000)
print(friend.name, friend.school, friend.salary)


