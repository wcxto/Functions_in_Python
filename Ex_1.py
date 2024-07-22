# Продукты
# Примеры вызова и вывода функции

# Вызов #1:

printGroceries('Бананы', [1, 2], ('Python',), 'Яблоки', '', 'Макароны', 5, True, 'Кофе', False)

# Вывод #1:

1) Бананы
2) Яблоки
3) Макароны
4) Кофе

# Вызов #2:

Нет продуктов


# Решение
# Способ 1:

def printGroceries(*args):
	products = [i for i in args if type(i) is str and i != '']
	if len(products) != 0:
    	res = [str(i+1)+')' + ' ' + products[i] for i in range(len(products))]
    	result = '\n'.join(res)
    	print(result)
	else:
    	print('Нет продуктов')
