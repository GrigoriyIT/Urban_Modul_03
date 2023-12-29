def test(*args):
    print(args)
    for i in args:
        print(i)


test(23, True, 'String')


def test2(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, '-', value)


test2(name='Vasya', married=True, age=25)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n = n - 1)
    return n * factorial_n_minus_1


print(factorial(5))


# Выхлоп
# (23, True, 'String')
# 23
# True
# String
# {'name': 'Vasya', 'married': True, 'age': 25}
# name - Vasya
# married - True
# age - 25
# 120