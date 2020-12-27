import random
import time


class Auctioneer:
    def __init__(self, name, total_funds, bet=5):
        self.name = name    # имя аукционера
        self.total_funds = total_funds  # всего средств
        self.current_rate = 0
        self.ready_to_bet = True
        self.bet = bet

    def take_bet(self, min_current):       # предложить стоимость
        #print("{} делает ставку в ".format(self.name), end=' ')
        #bet = random.randint(-1, 100)                      # float(input("{} делает шаг в ".format(self.name)))
        #print(self.current_rate)
        if self.bet + self.current_rate > self.total_funds:
            print("Недостаточно средств ({}), выбывает".format(self.name))
            self.ready_to_bet = False
        elif self.bet <= -1:
            print("{} выбывает".format(self.name))
            self.ready_to_bet = False
        elif self.bet == 0:
            print("{} сохраняет ставку".format(self.name))
            self.ready_to_bet = False
        else:
            while self.current_rate <= min_current:
                self.current_rate += self.bet
                #print(self.name, self.current_rate, min_current)
            print("{} делает ставку в ".format(self.name), end=' ')
            print(self.current_rate)



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
        while [x.ready_to_bet for x in self.Participants[:]].count(True) > 1:
            for participant in self.Participants:
                time.sleep(0.5)
                if not participant.ready_to_bet:
                    continue
                #print(self.winning_rate)
                min_current = self.winning_rate
                print("Текущая ставка:", min_current)
                participant.take_bet(min_current)
                self.current_winner = self.winner(self.Participants)

        return self.current_winner


if __name__ == "__main__":
    zakaz = Lot("Производство", 1)
    auct1 = Auctioneer("Заказ 1", 100, 20)
    auct2 = Auctioneer("Заказ 2", 70, 10)
    auct3 = Auctioneer("Заказ 3", 25)
    auctioneers = [auct1, auct2, auct3]
    auction = Auction(zakaz, auctioneers)
    a = [x.ready_to_bet for x in auction.Participants[:]]
    z = [False for i in range(0, len(auction.Participants))]
    winner = auction.start_auction()
    print(winner.name)
