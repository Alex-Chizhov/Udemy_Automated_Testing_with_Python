class Pizza(object):

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

p = Pizza(32)
print(p.get_size())

print(Pizza(42).get_size)
print(Pizza(42).get_size())

m = Pizza(4).get_size
print(m())

# if you wanted to know which object this bound method is bound to? Here's a little trick:

print(m.__self__)

print(m == m.__self__.get_size)
print(type(m))