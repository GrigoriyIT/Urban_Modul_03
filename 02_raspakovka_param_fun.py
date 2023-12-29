def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25) # Предупреждает, но работает. Вилимо благодаря динамической типизации
print_params(c=[1, 2, 3]) # Предупреждает, но работает. Вилимо благодаря динамической типизации


values_list = [20, 'строка', True]
values_dict = {'b': 'STRING', 'a': 11, 'c': True}


print_params(*values_list)
print_params(**values_dict)


values_list_2=[33, 'StRiNg']


print_params(*values_list_2, 42) # Работает


# Выхлоп
# 1 строка True
# 1 25 True
# 1 строка [1, 2, 3]
# 20 строка True
# 11 STRING True
# 33 StRiNg 42
