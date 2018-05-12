lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (12, 23, 46, 57, 22)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (12, 23, 46, 57, 22)

    def total(self):
        return sum(self.numbers)

player11  = LotteryPlayer('Alex')
player12 = LotteryPlayer('John')

print(player11.name)
print(player11.numbers)
print(player11.total())

print(player12.name)