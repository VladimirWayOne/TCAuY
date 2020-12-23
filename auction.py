import random
import time


class Auctioneer:
    def __init__(self, name, total_funds):
        self.name = name    # имя аукционера
        self.total_funds = total_funds  # всего средств
        self.current_rate = 0
        self.ready_to_bet = True

    def take_bet(self):       # предложить стоимость
        print("{} делает шаг в ".format(self.name), end=' ')
        bet = random.randint(-1, 100)                      # float(input("{} делает шаг в ".format(self.name)))
        print(bet)
        if bet + self.current_rate > self.total_funds:
            print("Недостаточно средств ({}), выбывает".format(self.name))
            self.ready_to_bet = False
        elif bet <= -1:
            print("{} выбывает".format(self.name))
            self.ready_to_bet = False
        elif bet == 0:
            print("{} сохраняет ставку".format(self.name))
            self.ready_to_bet = False
        else:
            self.current_rate += bet


class Lot:
    def __init__(self, name, min_price=0.1):
        self.name = name    # имя лота
        self.min_price = min_price  # минимальная цена


class Auction:
    def __init__(self, Lot, Participants, initial_rate=1, step=1):
        self.Lot = Lot
        self.Participants = Participants    # список участников
        self.initial_rate = initial_rate    # начальная ставка
        self.step = step                # шаг
        self.current_winner = None      # текущий победитель
        self.winning_rate = 0

    def winner(self, participants):     # поиск победителя
        for participant in participants:
            if participant.current_rate > self.winning_rate:
                self.winning_rate = participant.current_rate
                self.current_winner = participant

        print('Текущий победитель:', self.current_winner.name)
        return self.current_winner

    def start_auction(self):
        while [False for i in range(0, len(self.Participants))] != [x.ready_to_bet for x in self.Participants[:]]:
            for participant in self.Participants:
                time.sleep(0.5)
                if not participant.ready_to_bet:
                    continue
                participant.take_bet()
            self.current_winner = self.winner(self.Participants)

        return self.current_winner


if __name__ == "__main__":
    zakaz = Lot("Доставка до склада", 1)
    auct1 = Auctioneer("Мобильный робот 1", 100)
    auct2 = Auctioneer("Мобильный робот 2", 50)
    auct3 = Auctioneer("Мобильный робот 3", 25)
    auctioneers = [auct1, auct2, auct3]
    auction = Auction(zakaz, auctioneers)
    a = [x.ready_to_bet for x in auction.Participants[:]]
    z = [False for i in range(0, len(auction.Participants))]
    winner = auction.start_auction()
    print(winner.name)
    pass
