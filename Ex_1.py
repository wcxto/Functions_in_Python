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


# Способ 2:

def printGroceries(*args):
	list_products = [i for i in args if type(i) == str and len(i) > 0]
	if len(list_products) == 0:
    	print("Нет продуктов")
	else:
    	for i in range(len(list_products)):
        	print(f'{i+1}) {list_products[i]}')
