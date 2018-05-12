# Class methods are methods that are not bound to an object, but to… a class!

class Pizza():
    radius = 42

    @classmethod
    def get_radius(cls):
        return cls.radius

print(Pizza.get_radius)
print(Pizza().get_radius)
print(Pizza.get_radius())
