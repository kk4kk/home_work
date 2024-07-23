# Задача 1.
print('\n Задача 1. \n')
# Функция на вход получает два произвольных числа. Вывести в консоль наибольшее из чисел.

def largest_number(a: int, b: int):
   if a < b:
       print(b)
   elif a > b:
       print(a)
   else:
       print('Числа равны')

largest_number(74, 102)


# Задача 2.
print('\n Задача 2. \n')
# Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”

def difference_135(a: int, b: int):
   if (a - b) == 135 or (b - a) == 135:
       print('yes')
   else:
       print('no')

difference_135(-135, 0)


# Задача 3.
print('\n Задача 3. \n')
# Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень).
print('Вариант 1')
def season(month):
    if month == 12 or month in range (1, 3):
        print('Зима')
    elif 3 <= month <= 5:
        print('Весна')
    elif 6 <= month <= 8:
        print('Лето')
    elif 9 <= month <= 12:
        print('Осень')
    else:
        print('Некорректное число')

season(7)

# Или так:
print('\nВариант 2')
def season_in(month, winter = (12, 1, 2), spring = (3, 4, 5), summer = (6, 7, 8), autumn = (9, 10, 11)):
    if month in winter:
        print('Зима')
    elif month in spring:
        print('Весна')
    elif month in summer:
        print('Лето')
    elif month in autumn:
        print('Осень')
    else:
        print('Некорректное число')

season_in(7)


# Задача 4.
print('\n Задача 4. \n')
# Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”.

def numbers(a, b, c):
    if a > 10 and b > 10 and c >10:
        print('yes')
    else:
        print ('no')

numbers(11, 20, 13)


# Задача 5*.
print('\n Задача 5*. \n')
# Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.
print('Вариант 1')
def positive_num(l:list = [1, 3, 7, 8, 6]) -> int:
    a = []
    for i in l:
        if i > 0:
            a.append(0)
    return len(a)

print(positive_num())

print('\nВариант 2')
def pos_num(l:list = [1, 3, 7, 8, 6]) -> int:
    a = 0 # Создаю переменную равную 0. Это будет счётчик положительных чисел.
    for i in l: # цикл для элементов в списке 'l':
        if i > 0: # Если любой элемент списка больше 0,
            a += 1 # то переменная 'a' увеличится на 1.
    return a

print(pos_num())

# Задача 6*.
print('\n Задача 6*. \n')
# Функция на вход получает 2 переменные.
# a. Кол-во лет (int)
# b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

def counting_days(y: int, m: int):
    if y < 0:
        print('Нельзя вводить отрицательные числа')
    elif m < 0:
        print('Давайте мыслить положительно')
    else:
        d = y * 12 * 29 + m * 29
        print((d), 'дней')
counting_days(0, 1)

