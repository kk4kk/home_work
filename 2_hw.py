# ДЗ 2.
# Задача 1.
print('\n Задача 1. \n')
def task_1(a: int = 123, b: float = 1.5, c: str = 'Строка', d: list = ['из списка 1', 'из списка 2', 'из списка 3'], e: bool = True) -> str:
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))

task_1()


# Задача 2.
print('\n Задача 2. \n')
def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]) -> list:
    print(a[0:3])
    print('Если правильно понял вопрос наименования последовательности: \n 1, 2, 3, 5, 8, 13, 21 - это часть ряда Фибоначчи, \n 1, 2, 3 - просто ряд натуральных чисел.')

task_2()


# Задача 3.
print('\n Задача 3. \n')

def task_3(a:int = 11) -> int:
    return a * a

print(task_3())
