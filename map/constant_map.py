import numpy as np

from map.map import Map


class ConstantMap(Map):
    def __init__(self, size, population, transport_transactions):
        super().__init__(size)
        self.population = population
        self.transport_transactions = transport_transactions

    def get_transport_transactions(self, coordinate_score):
        result = np.zeros((self.size.value_x(), self.size.value_y()), np.int8)
        for i in range(len(result)):
            for j in range(len(result[i])):
                result[i][j] = abs(i-coordinate_score.value_x()) + abs(j-coordinate_score.value_y())
        result *= self.transport_transactions
        return result

    def get_clients(self, coordinate_score) ->int:
        return self.population
