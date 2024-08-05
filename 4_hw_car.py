# Задача 4*.
print('\n Задача 4*. \n')
# Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа.
# iv. Пятый — присвоение автомобилю цвета.

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def start_engine(self):
        print('Автомобиль заведён')


    def stop_engine(self):
        print('Автомобиль заглушен')


    def year_car(self):
        print(f'Год выпуска автомобиля: {self.year}')


    def type_car(self):
        print(f'Тип автомобиля: {self.type}')


    def color_car(self):
        print(f'Цвет автомобиля: {self.color}')

car_1 = Car('yellow', 'coupe', 2024)

car_1.start_engine()
car_1.stop_engine()
car_1.color_car()
car_1.type_car()
car_1.year_car()