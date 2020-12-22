class Auctioneer:
    def __init__(self, name, total_funds):
        self.name = name
        self.total_funds = total_funds
        self.current_rate = None


class Lot:
    def __init__(self, min_price=0.1):
        self.min_price = min_price


class Auction:
    def __init__(self, initial_rate=1, step=1):
        self.initial_rate = initial_rate
        self.step = step
