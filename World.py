import numpy as np
import copy
from Fourmis import Fourmi
np.random.seed(42)

class World:
    c = .001
    Q = 100
    alpha = 1
    beta = 0.25
    rho = .5
    def __init__(self, nb_epoch, nb_cities, nb_ants):
        self.n = nb_cities
        self._m = nb_ants
        self.nb_epoch = nb_epoch
        self._ants = None
        self.dist_map = None
        self.phero_map = None
        self.creat_map()
        self.creat_phero_map()
        self.creat_place_ants()
        self.best_lk = 10000
        self.best_path = []
        # self.initialize()

    def initialize(self):
        [ant.initialize() for ant in self._ants]

    def creat_map(self):
        _map = np.random.randint(1, self.n, (self.n,self.n))
        # _map -= np.diag(_map.diagonal())
        _map = _map + _map.T 
        self.dist_map = _map
        # print(self.map)

    def creat_phero_map(self):
        _phero_map = np.full((self.n,self.n), self.c)
        _phero_map -= np.diag(_phero_map.diagonal())
        self.phero_map = _phero_map
        # self.phero_map = copy.deepcopy(1/(self.dist_map+np.eye(self.n)))
        # print(self.phero_map)

    def creat_place_ants(self):
        self._ants = np.empty(self._m, dtype=object)
        not_placed_on = [city for city in range(self.n)]
        for i in range(self._m):
            index = np.random.choice(np.arange(len(not_placed_on)))
            start_pos = not_placed_on.pop(index)
            self._ants[i] = Fourmi(i, start_pos)
        # print([ant.start_position for ant in self._ants])

    def run_one_ite(self):
        for ant in self._ants:
            new_pos = ant.make_choice(ant.current_pos, self.phero_map, self.dist_map, self.alpha, self.beta)
            ant.apply_choice(new_pos)
        # print([ant.memory for ant in self._ants])

    def update_phero_map(self):
        new_phero_m = copy.deepcopy(self.phero_map)
        for ant in self._ants:
            for i in range(1, len(ant.memory)):
                l, c = ant.memory[i-1], ant.memory[i]
                if ant.LK[i-1] == 0:
                    print(l,c)
                new_phero_m[l,c] += self.Q / ant.LK[i-1]
            if ant.l_k < self.best_lk:
                self.best_lk = ant.l_k
                self.best_path = ant.memory
        for l, phero_l in enumerate(self.phero_map):
            for c, phero in enumerate(phero_l):
                new_phero_m[l,c] += phero * self.rho
        self.phero_map = copy.deepcopy(new_phero_m)

    def run_one_cycle(self):
        self.initialize()
        for t in range(self.n):
            self.run_one_ite()
        self.update_phero_map()
        for ant in self._ants:
            print(ant.l_k, ant.memory)
        print("\n")

    def run_simulation(self):
        for i in range(self.nb_epoch):
            self.run_one_cycle()
            # https://www.csestack.org/python-check-if-all-elements-in-list-are-same/
            if all(self._ants[0].memory == ant.memory for ant in self._ants):
                break
        return self.best_path

if __name__ == '__main__':
    nb_cities = 7
    nb_ants = 2
    nb_epoch = 3
    world = World(nb_epoch, nb_cities, nb_ants)
    print(world.run_simulation())

