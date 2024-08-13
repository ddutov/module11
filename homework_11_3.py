import inspect

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now



v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
videos = [v1, v2]

def introspection_info(obj):
    print(obj)  #
    help(obj)   # возможная справка по объекту и его методам
    print(type(obj))   # проверка типа объекта
    print(dir(obj))  # проверка доступных атрибутов и методов объекта
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        print(attr_name, type(attr))  # вызов доступных атрибутов и методов объекта и проверка его типа
    print(callable(obj))  # проверка объекта на возможность быть вызванным
    print(inspect.ismodule(obj))  # проверка на принадлежность проверяемого объекта к библиотеке
    print(inspect.isclass(obj))  # проверка на принадлежность проверяемого объекта к классу
    print(inspect.isfunction(obj))  # проверка на принадлежность проверяемого объекта к функции
    print(inspect.isbuiltin(obj))  # проверка на принадлежность проверяемого объекта к встроенной в Pithon функции


print('\033[32m информации об объекте класса Video \033[0m')
introspection_info(v1)
print(40 * '-')
print(40 * '-')
print('\033[32m информации об объекте "список объектов класса Video"\033[0m')
introspection_info(videos)
print(40 * '-')
print(40 * '-')
print(callable(introspection_info))

