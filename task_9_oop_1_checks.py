# Задача 5*.
print('\n Задача 5*. \n')
# В файле task_9_oop_1.py (сделал в task_9_oop_1_checks.py):
# c. наследуйте все классы от класса Checks
# i. чтобы использовать класс из другого файла его нужно импортировать
# from название файла(без расширения) import название класса
# d. переделайте все 4 класса в файле task_9_oop_1.py так чтоб в объектах можно было использовать методы родительского класса
# e. распечатайте в консоль результаты метода .check_text() вызванного от каждого объекта классов файла task_9_oop_1.py

# предыдущие принты закомментил, чтобы не мешали.

from task_9_checks import Checks
class Input(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Input('Поле ввода', 'input#search')

#print(search.text, search.loc)
print(search.check_text())

class Button(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Button('Найти', 'button#search')

#print(search.text, search.loc)
print(search.check_text())


class Title(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Title('Поиск', 'title#search')

#print(search.text, search.loc)
print(search.check_text())


class Link(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Link('Найти', 'link#search')

#print(search.text, search.loc)
print(search.check_text())