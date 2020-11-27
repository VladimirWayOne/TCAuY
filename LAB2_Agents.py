class Agent:
    """Единый класс Агента"""
    def __init__(self, name):
        print('Агент ' + name +' готов')


class Storage:
    """Класс Склада"""
    def __init__(self, maximum_things=10):
        self.maximum = maximum_things       # размер хранилища
        print('Допустимая нагружемость: ', self.maximum)

    _current = 0
    _storage = []

    def Accept(self, thing):
        """Функция приемки на складе"""

        if self._current < self.maximum:
            self._current += 1
            self._storage.append(thing)
            print('Процесс приемки ', thing)
        else:
            print('Склад переполнен')

    def Issue(self, thing):
        """Функция выдачи со склада"""

        if self._current < 1:        # если склад пустой
            print('Склад пуст')
        else:
            if thing in self._storage:   # есть ли запрашиваемая вещь на складе
                print('Процесс выдачи ', thing)
                self._storage.remove(thing)
            else:
                print(thing, ': данного предмета/вещи нет')


class MobileRobot:
    pass


if __name__ == "__main__":
    robot = Agent('Жора')
    sklad = Storage(10)
    sklad.Accept('всякой хуйни')
    sklad.Accept('всякой хуйни_2')
    sklad.Accept('всякой хуйни_3')
    sklad.Issue('всякой хуйни_3')
    sklad.Issue('всякой хуйни')
    # help(Storage.Issue)
