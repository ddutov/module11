import inspect
from pprint import pprint


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now


v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
videos = [v1, v2]


def introspection_info(obj):
    result = []
    print(obj)  #
    result.append(help(obj))  # возможная справка по объекту и его методам
    result.append(type(obj))  # проверка типа объекта
    result.append(dir(obj))  # проверка доступных атрибутов и методов объекта
    dict_attr = {}
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        dict_attr[attr_name] = type(attr)
    result.append(dict_attr)  # вызов доступных атрибутов и методов объекта и проверка его типа
    result.append(callable(obj))  # проверка объекта на возможность быть вызванным
    result.append(inspect.ismodule(obj))  # проверка на принадлежность проверяемого объекта к библиотеке
    result.append(inspect.isclass(obj))  # проверка на принадлежность проверяемого объекта к классу
    result.append(inspect.isfunction(obj))  # проверка на принадлежность проверяемого объекта к функции
    result.append(inspect.isbuiltin(obj))  # проверка на принадлежность проверяемого объекта к встроенной в Pithon функции
    return result


print('\033[32m информации об объекте класса Video \033[0m')
pprint(introspection_info(v1))
print(40 * '-')
print(40 * '-')
print('\033[32m информации об объекте "список объектов класса Video"\033[0m')
pprint(introspection_info(v1))
print(40 * '-')
print(40 * '-')
pprint(callable(introspection_info))
