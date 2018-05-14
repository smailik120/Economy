from map.map import Map
from dijkstra import *


class RealMap(Map):

    def __init__(self, size, matrix_population, matrix_transport_transactions):
        super().__init__(size)
        self.matrix_population = matrix_population
        self.matrix_transport_transactions = matrix_transport_transactions

    def get_clients(self, coordinate_score) -> int:
        return self.matrix_population[coordinate_score.value_x()][coordinate_score.value_y()]

    def get_transport_transactions(self, coordinate_score):
        return Dijkstra(self.matrix_transport_transactions).run(coordinate_score)
