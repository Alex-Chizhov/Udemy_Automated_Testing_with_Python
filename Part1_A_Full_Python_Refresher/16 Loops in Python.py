# my_variable = "Hello"
#
# for character in my_variable:   # iterables are strings, lists, tuples, and more
#     print(character)
#
# my_list = [1, 2, 3, 4, 5]
#
# for numer in my_list:
#     print(numer ** 2)

# user_wants_number = True
# while user_wants_number == True:
#     print(100)
#     user_wants_number = False

user_wants_number = True
while user_wants_number == True:
    print(100)
    user_input = input('Should we print again? (y/n): ')
    if user_input == 'n':
        user_wants_number = False