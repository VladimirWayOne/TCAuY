import time
from tqdm import tqdm


class Agent:
    """Единый класс Агента"""
    def __init__(self, name):
        print('Агент ' + name + ' готов')


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
    """Класс мобильного робота"""
    def __init__(self):
        pass
    __isReady = True    # готовность работы

    def transport(self, what, from_where, to_where):
        """Транспортировка"""
        if self.__isReady:      # проверка на готовность
            self.__isReady = False
            print('Транспортировка ', what, ' из ', from_where, ' до ', to_where)
            for i in tqdm(range(0, 10)):
                time.sleep(0.1)
            self.__isReady = True
        else:
            print('Мобильный робот занят')
    pass


if __name__ == "__main__":
    robot = Agent('Жора')
    sklad = Storage(10)
    sklad.Accept('всякой хуйни')
    sklad.Accept('всякой хуйни_2')
    sklad.Accept('всякой хуйни_3')
    sklad.Issue('всякой хуйни_3')
    sklad.Issue('всякой хуйни')
    tr_rob = MobileRobot()
    tr_rob.transport('деталь', 'прокат', 'резка')
    tr_rob.transport('деталь', 'прокат', 'резка')
