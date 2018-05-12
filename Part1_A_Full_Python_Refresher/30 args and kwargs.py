def my_method(arg1, arg2):
    return arg1 + arg2

print(my_method(1,2))


def addition_simplified(*args):
    return sum(args)

print(addition_simplified(1, 2, 3, 4, 5, 6, 7, 8, 9))


def what_are_kwargs(*args, **kwargs):
    print(args)     # ()
    print(kwargs)   # {}

what_are_kwargs(12, 13, 56, name = ' Jose', location='UK')



