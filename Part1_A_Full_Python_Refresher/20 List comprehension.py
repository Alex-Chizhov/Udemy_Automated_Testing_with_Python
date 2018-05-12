my_list = [1, 2, 3, 4, 5]
an_equal_list = [x for x in range(6)]
print(an_equal_list)

multiply_list = [x * 3 for x in range(6)]
print(multiply_list)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

people_you_know = ['John', '  Rolf', 'anna', 'ALEX']
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)