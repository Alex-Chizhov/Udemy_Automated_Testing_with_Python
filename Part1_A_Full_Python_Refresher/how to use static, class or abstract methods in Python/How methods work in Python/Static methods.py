# Static methods are a special case of methods.
# Sometimes, you'll write code that belongs to a class, but that doesn't use the object itself at all.


class Pizza():

    @staticmethod
    def mix_ingredients(x,y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

p = Pizza()
print(p.mix_ingredients(1,2))
