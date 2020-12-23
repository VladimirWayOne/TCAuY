class Auctioneer:
    def __init__(self, name, total_funds):
        self.name = name    # имя аукционера
        self.total_funds = total_funds  # всего средств
        self.current_rate = None

    def take_bet(self, bet):       # предложить стоимость
        if bet > self.total_funds:
            print("Недостаточно средств")
        else:
            self.current_rate = bet


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

        print(self.current_winner.name)
        return self.current_winner


if __name__ == "__main__":
    zakaz = Lot("Доставка до склада", 1)
    auct1 = Auctioneer("Мобильный робот 1", 100)
    auct2 = Auctioneer("Мобильный робот 2", 50)
    auct3 = Auctioneer("Мобильный робот 3", 25)
    pass
