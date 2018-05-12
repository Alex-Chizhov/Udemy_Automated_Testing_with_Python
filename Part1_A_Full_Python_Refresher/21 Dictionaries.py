my_set = {1,2,3}
my_dic = { 'name': 'Alex', 'age': 90, 'grades': [13, 45, 66, 90]}
another_dic = {1: 15, 2: 75, 3: 150}
#print(my_dic['grades'])

lottery_player = {
    'name': 'Rolf',
    'numbers': [12, 23, 46, 57, 22]

}

universities = [
    {
       'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

my_sum = sum(lottery_player['numbers'])
print(my_sum)

lottery_player['name'] = 'John'
lottery_player['numbers'][0] = 50
print('1')