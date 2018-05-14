from score import Score


class Seller:
    def __init__(self):
        self.list_score = []

    def new_score(self, coordinate, price):
        store = Score(coordinate, price)
        self.list_score.append(store)
        return store

    def get_profit(self):
        profit = 0
        for i in self.list_score:
            profit += i.profit
        return profit
