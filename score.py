class Score:
    def __init__(self, coordinate, price):
        self.coordinate = coordinate
        self.price = price
        self.profit = 0

    def get_coordinate(self):
        return self.coordinate

    def price_on_world(self, transport_transactions):
        return transport_transactions + self.price

    def set_profit(self, number_clients):
        self.profit = self.price * number_clients

    def get_profit(self):
        return self.profit
