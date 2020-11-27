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
        self.__isReady = True    # готовность работы

    def transport(self, what, from_where, to_where):
        """Транспортировка"""
        if self.__isReady:      # проверка на готовность
            self.__isReady = False
            print('Транспортировка ', what, ' из ', from_where, ' до ', to_where)
            for i in tqdm(range(0, 10)):
                time.sleep(0.01)

            print('\nПередача завершена')

            self.__isReady = True
        else:
            print('Мобильный робот занят')


class CuttingMachine:
    """Класс Станка для резки прута
    Приемка происходит при условиях:
        -в станке нет детали
        -не осуществляется какой-либо процесс (приемка/резка/выдача)

    Резка происходит при условиях:
        -процесс приемки закончен
        -деталь в станке

    Выдача происходит при условиях:
        -процесс резки закончен"""

    def __init__(self):
        self.__isReadyForAccept = True      # готовность приемки
        self.__isReadyForCutting = False     # готовность резки
        self.__isReadyForIssue = False      # готовность выдачи

    def Accept(self, detail):
        """Функция приемки детали"""
        if self.__isReadyForAccept:
            print('Приемка ', detail)
            self.__isReadyForAccept = False
            self.__isReadyForCutting = True
        else:
            print('Станок не готов к приемке')

    def Cutting(self, detail):
        """Функция резки детали"""
        if self.__isReadyForCutting:
            print('Резка ', detail)
            self.__isReadyForCutting = False
            self.__isReadyForIssue = True
        else:
            print('Станок не готов к резке')

    def Issue(self):
        """Функция выдачи"""
        if self.__isReadyForIssue:
            print('Выдача')
            self.__isReadyForIssue = False
            print('Станок пуст и готов к приемке')
            self.__isReadyForAccept = True
        else:
            print('Станок не готов к выдаче')


class StationaryRobot:
    """Класс стационарного робота"""
    def __init__(self, detail=None):
        self.detail = detail
        self.__isReady = True
        pass

    def Load(self, get_msgs):
        """Функция загрузки деталей с тары на токарный станок"""
        if not get_msgs:       # сообщение о готовности
            print('Тара или станок не готовы')
            return 0
        if self.__isReady:
            if self.detail is not None:
                print('Захват детали')
                self.__isReady = False
                print('Деталь установлена')
                self.__isReady = True
            else:
                print('Нет детали')
        else:
            print('Стационарный робот не готов')

    def Move(self, get_msgs_tok, get_msgs_frez):
        """Функция перемещения деталей с токарного станка на фрезерный"""
        if not get_msgs_tok:       # Проверка сигнала о готовности выдачи с токарного станка
            print('Выдача с токарного станка не готова')
            return 0

        if not get_msgs_frez:      # Проверка сигнала о готовности выдачи с токарного станка
            print('Фрезерный станок не готов к приемке')
            return 0

        if self.__isReady:
            self.__isReady = False
            print('Захват детали с фрезерного станка')
            print('Установка детали на фрезерный станок')
            print('Деталь установлена')
            self.__isReady = True
        else:
            print('Стационарный робот не готов')

    def Removing(self, get_msgs):
        """Функция снятия деталей с фрезерного станка"""
        if not get_msgs:           # Проверка готовности фрезерного станка
            print('Фрезерный станок не готов к выдаче')
            return 0

        if self.__isReady:
            self.__isReady = False
            print("Захват детали с фрезерного станка")
            print("Перемещение детали в тару")
            self.__isReady = True
        else:
            print('Стационарный робот не готов')


if __name__ == "__main__":
    robot = Agent('Жора')
    sklad = Storage(2)
    sklad.Accept('всякой хуйни')
    sklad.Accept('всякой хуйни_2')
    sklad.Accept('всякой хуйни_3')
    sklad.Issue('всякой хуйни_3')
    sklad.Issue('всякой хуйни')
    tr_rob = MobileRobot()
    tr_rob.transport('деталь', 'прокат', 'резка')
    tr_rob.transport('деталь', 'прокат', 'резка')
    cutmach = CuttingMachine()
    statrob = StationaryRobot('деталь')
    statrob.Load(False or True)
    statrob.Load(True)
   # help(CuttingMachine())
