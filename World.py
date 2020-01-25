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
        self.c = 0.01
        self.initialize()

    def initialize(self):
        self.creat_map()
        self.creat_phero_map()
        self.creat_place_ants()

    def creat_map(self):
        # self.map = np.arange()
        _map = np.random.randint(0, self.n*2, (self.n,self.n))
        _map -= np.diag(_map.diagonal())
        _map = _map + _map.T
        self.map = _map
        print(self.map)
        # np.linspace()

    def creat_phero_map(self):
        _phero_map = np.full((self.n,self.n), self.c)
        _phero_map -= np.diag(_phero_map.diagonal())
        print(_phero_map)

    def creat_place_ants(self):
        self._ants = np.empty(self._m, dtype=Fourmis)
        for i in self._m:
            ant = Fourmis(i, )
        for city in self.map:
            

    def run_one_cycle(self):
        pass

    
if __name__ == '__main__':
    nb_cities = 5
    nb_ants = 1
    world = World(nb_cities, nb_ants)
