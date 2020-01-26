import numpy as np
from Fourmis import Fourmi
np.random.seed(42)

class World:

    def __init__(self, nb_cities, nb_ants):
        self.n = nb_cities
        self._B = []
        self._m = nb_ants
        self._ants = None
        self.map = None
        self.phero_map = None
        self.c = 0.01
        self.alpha = 0.5
        self.beta = 0.5
        self.initialize()

    def initialize(self):
        self.creat_map()
        self.creat_phero_map()
        self.creat_place_ants()

    def creat_map(self):
        _map = np.random.randint(0, self.n*2, (self.n,self.n))
        _map -= np.diag(_map.diagonal())
        _map = _map + _map.T
        self.map = _map
        # print(self.map)

    def creat_phero_map(self):
        _phero_map = np.full((self.n,self.n), self.c)
        _phero_map -= np.diag(_phero_map.diagonal())
        self.phero_map = _phero_map
        # print(_phero_map)

    def creat_place_ants(self):
        self._ants = np.empty(self._m, dtype=object)
        not_placed_on = [city for city in range(self.n)]
        for i in range(self._m):
            index = np.random.choice(np.arange(len(not_placed_on)))
            start_pos = not_placed_on.pop(index)
            self._ants[i] = Fourmi(i, start_pos)
        # print([ant.start_position for ant in self._ants])
            

    def run_one_cycle(self):
        for ant in self._ants:
            print(ant.make_choice(ant.start_pos, self.phero_map, self.map, self.alpha, self.beta))
    
if __name__ == '__main__':
    nb_cities = 3
    nb_ants = 1
    world = World(nb_cities, nb_ants)
    world.run_one_cycle()
