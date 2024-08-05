# Задача 1.
print('\n Задача 1. \n')
# создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


    def perimeter(self):
        return (self.width + self.height) * 2

rectangle_1 = Rectangle(5, 7)
rectangle_2 = Rectangle(1, 4)
rectangle_3 = Rectangle(12, 10)

print(rectangle_1.area())
print(rectangle_1.perimeter())
print(rectangle_2.area())
print(rectangle_2.perimeter())
print(rectangle_3.area())
print(rectangle_3.perimeter())

# Или я мог бы отдельно прописать метод вывода:
#     def print_results(self):
#          print("Площадь прямоугольника:", self.area())
#          print("Периметр прямоугольника:", self.perimeter())
#
# Объекты:
# rectangle_1 = Rectangle(5, 7)
# rectangle_2 = Rectangle(1, 4)
# rectangle_3 = Rectangle(12, 10)
#
# и вызвать так:
# rectangle_1.print_results()
# rectangle_2.print_results()
# rectangle_3.print_results()


# Задача 2.
print('\n Задача 2. \n')
# Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


    def multiplication(self):
        return self.a * self.b


    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print('Деление на ноль')


    def subtraction(self):
        return self.a - self.b


result = Math(1.5, 5)

print(result.addition())
print(result.multiplication())
print(result.division())
print(result.subtraction())


# Задача 3.
print('\n Задача 3. \n')
# откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc


    def click(self):
        print(f'Клик по кнопке {self.text}')

button_1 = Button('Text Box', 'Button', '')
button_2 = Button('Check Box', 'Button','')
button_3 = Button('Radio Button', 'Button', '')
button_4 = Button('Web Tables', 'Button', '')
button_5 = Button('Buttons', 'Button', '')
button_6 = Button('Links', 'Button', '')
button_7 = Button('Broken Links - Images', 'Button', '')
button_8 = Button('Upload and Download', 'Button', '')
button_9 = Button('Dynamic Properties', 'Button', '')

print(button_1.text)
print(button_2.text)
print(button_3.text)
print(button_4.text)
print(button_5.text)
print(button_6.text)
print(button_7.text)
print(button_8.text)
print(button_9.text, '\n')

button_1.click()
button_2.click()
button_3.click()
button_4.click()
button_5.click()
button_6.click()
button_7.click()
button_8.click()
button_9.click()