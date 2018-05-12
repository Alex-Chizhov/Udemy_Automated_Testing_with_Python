def methodception(another):
    return another()

def add_too_numbers():
    return 35 + 77

# передаем без ()
# print(methodception(add_too_numbers))

# print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 484]
#my_list.remove(13)


# Identical
print(list(filter(lambda x: x != 13, my_list)))
# and
def not_thirteen(x):
    return x != 13
print(list(filter(not_thirteen, my_list)))



# Identical
(lambda x: x * 3)(5)
# and
def f(x):
    return x * 3

f(5)




l = (lambda x,y: x * y)(10, 10)
print(l)