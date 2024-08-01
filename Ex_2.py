# Личные данные

# Примеры вызова и вывода функции

# Вызов #1:
personalData(first_name='John', last_name='Doe', age=28, position='Python developer')

# Вывод #1:
age: 28
first_name: John
last_name: Doe
position: Python developer

# Вызов #2:
personalData(first_name='Jack', last_name='Smith', age=32, work_experience = '5 years', position='Project manager')

# Вывод #2:
age: 32
first_name: Jack
last_name: Smith
position: Project manager
work_experience: 5 years


# Решение
# Способ 1:

def personalData(**kwargs):
	for k, v in sorted(kwargs.items()):
    	print(f'{k}: {v}')
