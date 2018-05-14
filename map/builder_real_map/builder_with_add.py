import numpy as np

from map.builder_real_map.builder_real_map import BuilderRealMap
from map.real_map import RealMap


class BuilderWithAdd(BuilderRealMap):

    def __init__(self, size):
        self.size = size
        self.matrix_population = np.zeros((self.size.value_x(), self.size.value_y()))
        self.matrix_transport_transactions = np.zeros((self.size.value_x(), self.size.value_y()))

    def add_population(self, coordinates, population):
        self.matrix_population[coordinates.value_x()][coordinates.value_y()] = population

    def add_transaction(self, coordinates, transaction):
        self.matrix_transport_transactions[coordinates.value_x()][coordinates.value_y()] = transaction

    def createRealMap(self):
        return RealMap(self.size, self.matrix_population, self.matrix_transport_transactions)
