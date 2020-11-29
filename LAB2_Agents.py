import time
from tqdm import tqdm


class Agent:
    """Единый класс Агента"""
    def __init__(self, name):
        self.name = name
        #print('Агент ' + self.name + ' готов')


class Storage:
    """Класс Склада"""
    def __init__(self, maximum_things=10):
        self.maximum = maximum_things       # размер хранилища
        # print('Склад: Допустимая нагружемость: ', self.maximum)

    _current = 0
    _storage = []

    def Accept(self, thing):
        """Функция приемки на складе"""
        isReadyToAccept = True  #готовность к приемке
        isReadyToIssue = False  #готовность к выдаче
        if self._current < self.maximum:
            self._current += 1
            self._storage.append(thing)
            print('Склад: Процесс приемки ', thing)
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
                # return thing
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
            print('Мобильный робот: Транспортировка ', what, ' из ', from_where, ' до ', to_where)
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
        self.detail = None                  # текущая деталь в станке

    def Accept(self, detail):
        """Функция приемки детали"""
        if self.__isReadyForAccept:
            print('Станок для резки: Приемка ', detail)
            self.__isReadyForAccept = False
            self.__isReadyForCutting = True
        else:
            print('Станок для резки: Станок не готов к приемке')

    def Cutting(self, detail):
        """Функция резки детали"""
        if self.__isReadyForCutting:
            print('Резка ', detail)
            self.__isReadyForCutting = False
            self.__isReadyForIssue = True
        else:
            print('Станок для резки: Станок не готов к резке')

    def Issue(self, detail):
        """Функция выдачи"""
        if self.__isReadyForIssue:
            print('Выдача', detail)
            self.__isReadyForIssue = False
            print('Станок для резки: Станок пуст и готов к приемке')
            self.__isReadyForAccept = True
            # return detail
        else:
            print('Станок для резки: Станок не готов к выдаче')


class StationaryRobot:
    """Класс стационарного робота"""
    def __init__(self, detail=None):
        self.detail = detail
        self.__isReady = True
        pass

    def Load(self, detail):
        """Функция загрузки деталей с тары на токарный станок"""
        if detail is None:       # сообщение о готовности
            print('Тара или станок не готовы')
            return 0
        if self.__isReady:
            if self.detail is not None:
                print('Захват', detail)
                self.__isReady = False
                print('Стационарный робот: %s установлена' % detail)
                self.__isReady = True
            else:
                print('Стационарный робот: Нет детали')
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
           # print('Захват детали с фрезерного станка')
            #print('Установка детали на токарный станок')
            #print('Деталь установлена')
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
           # print("Захват детали с фрезерного станка")
        # print("Перемещение детали в тару")
            self.__isReady = True
        else:
            print('Стационарный робот не готов')


class Machine:
    """Класс токарного/фрезерного станков"""
    def __init__(self):
        self.isReadyToAccept = True
        self.__isReady = True
        self.isReadyToMove = False
        self.isReadyToIssue = False
        pass

    def Accept(self, detail):
        if not self.isReadyToAccept:
            print("Станок не готов к приемке")
            return 0
        else:
            if self.__isReady:
                self.__isReady = False
                print("Установка ", detail, " на станок")
                self.__isReady = True
            else:
                print("Станок не готов")

    def ProcessingTok(self):
        """Обработка на токарном станке"""
        if self.__isReady:
            self.__isReady = False
            print("Обработка")
            print("Конец обработки")
            self.__isReady = True
            self.isReadyToIssue = True
        else:
            print("Токарный станок не готов")

    def ProcessingFrez(self):
        """Обработка на фрезерном станке"""
        if self.__isReady:
            self.__isReady = False
            print("Фрезеровка")
            print("Конец фрезеровки")
            self.__isReady = True
            self.isReadyToIssue = True
        else:
            print("Фрезерный станок не готов")

    def Move(self):
        """Отправка запроса на перемещение"""
        self.isReadyToMove = True

    def Issue(self):
        """Выдача готовых деталей"""
        if self.isReadyToIssue:     # Проверка на готовность к выдаче
            print("Выдача")
        else:
            print('Станок не готов к выдаче')


class Container:
    """Тара для заготовок и готовых изделий"""
    def __init__(self, maximum=10, name='Тара_1'):
        self.maximum = maximum      # Максимальное количество содержимого в таре (по умолчанию 10)
        self.isReadyToAccept = True
        self.__isReadyToTransport = False
        self.content = []
        self.isReadyToIssue = False
        self.name = name
        pass

    def __isFull(self):
        """Приватный метод класса для проверки заполненности тары"""
        if len(self.content) == self.maximum:
            self.isReadyToIssue = True
            return True
        else:
            return False

    def __isEmpty(self):
        """Приватный метод класса для опустошенности тары"""
        if len(self.content) == 0:
            self.isReadyToIssue = False
            self.isReadyToAccept = True
            return True
        else:
            return False

    def Accept(self, detail):
        """Прием промежуточных заготовок и готовых деталей"""
        if self.__isFull():
            print('Тара переполненна')
            self.isReadyToAccept = False
        else:
            if self.isReadyToAccept:
                self.isReadyToAccept = False
                print("В процессе загрузки")
                self.content.append(detail)
                print('В', self.name, len(self.content), 'деталей')  # Заполненность
                self.__isReadyToTransport = True
                print("Готово к транспортировке")
                self.isReadyToIssue = True
                self.isReadyToAccept = True
            else:
                print("Тара не готова к приемке")

    def Transporting(self):
        """Перемещение тары посредством Мобильного робота"""
        if self.__isReadyToTransport:
            print("К транспортировке готово")

    def Issue(self, detail):
        """Выдача прутков на последующую обработку"""
        if self.__isEmpty():        # Проверка на пустоту
            print('Тара пуста')
            return 0

        if self.isReadyToIssue:          # Проверка на готовность к выдаче
            if detail in self.content:
                print('Выдача')
                self.content.remove(detail)
                self.isReadyToAccept = True
                if self.__isEmpty():    # Сообщение об опустошении
                    print('Тара пуста')
            else:
                print('Данной детали нет')
        else:
            print("Тара не готова к выдаче")


class Server:
    """
    Сервер, с помощью которого производится управление системой
    """
    def __init__(self, Agent, Storage, MobileRobot, CuttingMachine, StationaryRobot, Machine, Container):
        self.Agent = Agent
        self.Storage = Storage
        self.MobileRobot = MobileRobot
        self.CuttingMachine = CuttingMachine
        self.StationaryRobot = StationaryRobot
        self.Machine = Machine
        self.Container = Container

    def P1(self, detail):   # Приемка на складе
        if self.Storage.isReadyToAccept:
            self.Storage.Accept(detail)
        else:
            print('Error!')

    def P2(self, detail):   # Готовность выдачи
        if self.Storage.isReadyToIssue:
            return self.Storage.Issue(detail)
        else:
            print('Error!')

    def P3(self, what, from_where, to_where):   # Готовность транспортировки
        self.MobileRobot(what, from_where, to_where)

    def P4(self, detail):       # Готовность приемa
        self.CuttingMachine.Accept(detail)

    def P5(self, detail):       # Готовность резки прутка
        self.CuttingMachine.Cutting(detail)

    def P6(self, detail):       # Готовность выдачи
        self.CuttingMachine.Issue(detail)

    def P7(self, detail):               # Готовность приема ТОК_ФРЕЗ
        self.Machine.Accept(detail)

    def P8(self, machine):               # Обработка ТОК_ФРЕЗ
        if machine == 'фрез':
            self.Machine.ProcessingFrez()
        elif machine == 'ток':
            self.Machine.ProcessingTok()
        else:
            print("Такого станка нет")

    def P9(self):               # Отправка запроса на перемещение
        self.Machine.Move()
        self.P12()

    def P10(self):              # Готовность выдачи ТОК_ФРЕЗ
        self.Machine.Issue()

    def P11(self, detail):              # Прием сигнала о готовности тары и станка
        self.StationaryRobot.Load(detail)

    def P12(self):              # Прием сигнала о готовности выдачи с токарного станка
        self.StationaryRobot.Move(True, True)

    def P13(self):              # Прием сигнала с фрезерного станка о готовности выдачи
        self.StationaryRobot.Removing(True)

    def P14(self, detail):      # Загрузить в тару
        self.Container.Accept(detail)

    def P15(self,  what, from_where, to_where): # Транспортировка
        self.Container.Transporting()
        self.MobileRobot.transport(what, from_where, to_where)

    def P16(self, detail):                      # Выдача из контейнера
        self.Container.Issue(detail)

    """
    def StartProcCycle(self, detail):       # рабочий цикл для одной детали
        ""Полный цикл обработки""
        self.P4(detail)
        self.P5(detail)
        self.P6(detail)
        self.P14(detail)
        self.P15(detail, 'Станок для резки', 'Токарно-фрезерные станки')
        self.P16(detail)
        pass
    """

    def CuttingProcCycle(self, detail):
        """Цикл резки"""
        self.P4(detail)
        self.P5(detail)
        self.P6(detail)
        self.P14(detail)

    def TransportingProcCycle(self, container, from_where, to_where):
        """Рабочий цикл перевозки тары"""
        self.P15(container, from_where, to_where)

    def ProcessingProcCycle(self, detail):
        """Рабочий цикл обработки деталей"""
        self.P16(detail)

        self.P11(detail)
        self.P7(detail)
        self.P8('фрез')
        self.P9()
        self.P10()
        self.P12()
        self.P7(detail)
        self.P8('ток')
        self.P9()
        self.P10()
        self.P13()
        self.P14(detail)


if __name__ == "__main__":
    Agents = [Agent('деталь_1'), Agent("деталь_2"), Agent('Деталь_3')]
    # details = ['det1', 'det2', 'det3']
    agent = Agent('test')
    storage = Storage()
    mobilerobot = MobileRobot()
    cuttingmachine = CuttingMachine()
    statrobot = StationaryRobot()
    machine = Machine()
    contain = Container()
    server = Server(agent, storage, mobilerobot, cuttingmachine, statrobot, machine, contain)
    for ag in Agents:
        server.CuttingProcCycle(ag.name)

    server.TransportingProcCycle(server.Container.name, 'Отрезной станок', 'ТОК_ФРЕЗ станки')

    print(server.Container.content)
    copy_cont = server.Container.content.copy()
    for det in copy_cont:
        server.ProcessingProcCycle(det)

    server.TransportingProcCycle(server.Container.name, 'ТОК_ФРЕЗ станки', 'Цех сборки')
