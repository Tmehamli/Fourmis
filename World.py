import numpy as np
np.random.seed(42)
class World:
    def __init__(self, nb_cities, nb_ants):
        self.nb_cities = nb_cities
        self.nb_ants = nb_ants
        self.map = None
        self.c = 0.01
        self.initialize()

    def initialize(self):
        self.creat_map()
        self.creat_phe_map()
        self.creat_place_ants()

    def creat_map(self):
        # self.map = np.arange()
        _map = np.random.randint(0, self.nb_cities*2, (self.nb_cities,self.nb_cities))
        _map -= np.diag(_map.diagonal())
        _map = _map + _map.T
        self.map = _map

    def creat_phe_map(self):
        _phe_map = np.full((self.nb_cities,self.nb_cities), self.c)
        _phe_map -= np.diag(_phe_map.diagonal())
        print(_phe_map)

    def run_one_cycle(self):
        pass

    def creat_place_ants(self):
        pass
    
if __name__ == '__main__':
    nb_cities = 5
    nb_ants = 1
    world = World(nb_cities, nb_ants)
