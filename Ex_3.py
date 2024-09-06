# Значение многочлена

3 Многочленом степени n называется выражение вида

# Напишите функцию evaluate(coefficients, x), которая принимает список коэффициентов и значение аргумента x. 
# При реализации можно использовать анонимные lambda-функции, а также встроенные функции map() и reduce().

# Способ 1:

from functools import reduce
import operator
def evaluate(a, x):
	xi = map(lambda i: x**i, range(len(a)-1, -1, -1))
	axi = map(operator.mul, a, xi)         	
	return reduce(operator.add, axi, 0)
a = list(map(int, input().split()))
x = int(input())
print(evaluate(a, x))


# Способ 2:

from functools import reduce
evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)
print(evaluate([*map(int, input().split())], int(input())))
