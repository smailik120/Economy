from map.constant_map import ConstantMap
from coordinate import Coordinate
from seller import Seller

world = ConstantMap(Coordinate(5, 5), 1, 10)
Sasha = Seller()
world.new_store(Sasha.new_score(Coordinate(0, 0), 3))
Petr = Seller()
world.new_store(Petr.new_score(Coordinate(4, 4), 3))
Baba_Nura = Seller()
world.new_store(Baba_Nura.new_score(Coordinate(2, 2), 2))
world.calc_profit()
print(Sasha.get_profit())
print(Petr.get_profit())
print(Baba_Nura.get_profit())
