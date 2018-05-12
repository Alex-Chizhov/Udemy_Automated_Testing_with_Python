# def who_do_you_know():
#     people = input("Enter the names of people you know, separated by commas: ") # John,Rolf,Anna
#     people_list = people.split(',')     #['John', 'Rolf', 'Anna']
#     people_without_spaces = []
#     for person in people_list:
#         people_without_spaces.append(person.strip())  # Возвращает копию указанной строки,
#     return people_without_spaces                      # с обоих концов которой устранены указанные символы.
#                                                       # Если не указана, будут устранены пробельные символы
#                                                       # 'abca'.strip('ac')  # Останется только - 'b'
# def ask_user():
#     person = input("Enter a name of someone you know: ")
#     if person in who_do_you_know():
#         print('You know {}!'.format(person))
#
# ask_user()
#

def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ") # John,Rolf,Anna
    people_list = people.split(',')     #['John', 'Rolf', 'Anna']
    people_without_spaces = [person.strip() for person in people_list]
    return people_without_spaces


def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print('You know {}!'.format(person))

ask_user()

