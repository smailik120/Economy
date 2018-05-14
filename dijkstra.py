import numpy as np

from coordinate import Coordinate


def update_list(old_list, element):
    if element is not None:
        old_list.append(element)
    return old_list


class Dijkstra:

    def __init__(self, matrix):
        self.matrix = matrix
        self.finished_vertices = []
        self.result = None

    def give_element(self, coordinates):
        if 0 <= coordinates.value_x() < len(self.matrix) and 0 <= coordinates.value_y() < len(self.matrix[0]):
            return ElementDijkstra(coordinates, self)
        return None

    def finished(self, element):
        return element in self.finished_vertices

    def run(self, coordinates):
        self.finished_vertices = []
        self.result = np.zeros((len(self.matrix), len(self.matrix[0]))) - 1

        element = self.give_element(coordinates)
        element.value(0)
        waiting_for_processing = [element]
        while len(waiting_for_processing) > 0:
            min_index = 0
            for i in range(len(waiting_for_processing)):
                if waiting_for_processing[i].value() < waiting_for_processing[min_index].value():
                    min_index = i

            min_element = waiting_for_processing[min_index]
            for element in min_element.list_neighbors():
                if not self.finished(element):
                    new_value = element.value_transaction() + min_element.value()
                    if new_value < element.value() or element.value() == -1:
                        element.value(new_value)
                    waiting_for_processing.append(element)
            self.finished_vertices.append(min_element)
            del waiting_for_processing[min_index]

        return self.result


class ElementDijkstra:

    def __init__(self, coordinates, dijkstra):
        self.dijkstra = dijkstra
        self.coordinates = coordinates

    def value(self, new_value=None):
        if new_value is not None:
            self.dijkstra.result[self.coordinates.value_x()][self.coordinates.value_y()] = new_value
        return self.dijkstra.result[self.coordinates.value_x()][self.coordinates.value_y()]

    def value_transaction(self):
        return self.dijkstra.matrix[self.coordinates.value_x()][self.coordinates.value_y()]

    def get_coordinates(self):
        return self.coordinates

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def list_neighbors(self):
        result = []
        for i in (Coordinate(0, -1), Coordinate(1, 0), Coordinate(0, 1), Coordinate(-1, 0)):
            result = update_list(result, self.dijkstra.give_element(self.coordinates + i))

        return result
