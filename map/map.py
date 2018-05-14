from abc import abstractmethod

from coordinate import Coordinate


class Map:
    def __init__(self, size):
        self.list_store = []
        self.size = size

    def new_store(self, store):
        self.list_store.append(store)

    @abstractmethod
    def get_transport_transactions(self, coordinate_score):
        pass

    @abstractmethod
    def get_clients(self, coordinate_score) -> int:
        pass

    def calc_profit(self):
        list_price = []
        for i in self.list_store:
            list_price.append(i.price_on_world(self.get_transport_transactions(i.get_coordinate())))

        clients = []
        for _ in self.list_store:
            clients.append(0)

        for x in range(len(list_price[0])):
            for y in range(len(list_price[0][x])):
                minimum = list_price[0][x][y]
                store_in_call = [0]
                for i in range(1, len(list_price)):
                    if list_price[i][x][y] < minimum:
                        minimum = list_price[i][x][y]
                        store_in_call = [i]
                    elif list_price[i][x][y] == minimum:
                        store_in_call.append(i)
                for i in store_in_call:
                    clients[i] += self.get_clients(Coordinate(x, y))/len(store_in_call)

        for i in range(len(self.list_store)):
            self.list_store[i].set_profit(clients[i])
