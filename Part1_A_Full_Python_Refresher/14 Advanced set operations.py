your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}


print(your_lottery_numbers.intersection(winning_numbers))

# http://pythonz.net/references/named/sets.union/
# Элементы данного множества дополняются элементами,
# присутствующими в указанных объектах.
print(your_lottery_numbers.union(winning_numbers))

print({1, 2, 3, 4}.difference({1, 2}))