grades = [77, 80, 90]
tuple_grades = (77, 80, 90) # immutable
set_grades = {77, 80, 90}  # unique & unordered

grades.append(50)
print(grades)
print(grades[0])
grades[0] = 60


tuple_grades = tuple_grades + (100,)  # comma need be!
print(tuple_grades)

set_grades.add(60)
print(set_grades)