import numpy as np
import copy
from Fourmis import Fourmi
np.random.seed(42)

class World:
    c = .001
    Q = 100
    alpha = 1
    beta = 0.25
    rho = .3
    def __init__(self, nb_epoch, nb_cities, nb_ants, same_start = False):
        self.n = nb_cities
        self._m = nb_ants
        self.nb_epoch = nb_epoch
        self._ants = None
        self.dist_map = None
        self.phero_map = None
        self.same_start = same_start
        self.creat_map()
        self.creat_phero_map()
        self.creat_place_ants()
        self.best_lk = 10000
        self.best_path = []

    def initialize(self):
        [ant.initialize() for ant in self._ants]

    def creat_map(self):
        _map = np.random.randint(1, self.n, (self.n,self.n))
        _map = _map + _map.T 
        self.dist_map = _map

    def creat_phero_map(self):
        _phero_map = np.full((self.n,self.n), self.c)
        _phero_map -= np.diag(_phero_map.diagonal())
        self.phero_map = _phero_map

    def creat_place_ants(self):
        self._ants = np.empty(self._m, dtype=object)
        if self.same_start:
            index = np.random.choice(self.n)
            for i in range(self._m):
                start_pos = index
                self._ants[i] = Fourmi(i, start_pos)
        else:
            not_placed_on = [city for city in range(self.n)]
            for i in range(self._m):
                index = np.random.choice(np.arange(len(not_placed_on)))
                start_pos = not_placed_on.pop(index)
                self._ants[i] = Fourmi(i, start_pos)

    def run_one_ite(self):
        for ant in self._ants:
            new_pos = ant.make_choice(ant.current_pos, self.phero_map, self.dist_map, self.alpha, self.beta)
            ant.apply_choice(new_pos)

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
            info = 'distance: {}\n route: {}'.format(ant.l_k, ant.memory)
            print(info)

    def run_simulation(self):
        for i in range(self.nb_epoch):
            info = 'epoch: {}'.format(i)
            print(info)
            self.run_one_cycle()
            info = 'actual best: \n - distance: {}\n - path: {}\n'.format(self.best_lk, self.best_path)
            print(info)

            # https://www.csestack.org/python-check-if-all-elements-in-list-are-same/
            if all(self._ants[0].memory == ant.memory for ant in self._ants):
                break
        return self.best_path

    def __str__(self):
        HEADER = '*'*61 + '\n'
        HEADER += ' '*25 + 'TSP Ants' + '\n'
        HEADER += ' '*25 + 'Theo Mehamli' + '\n'
        HEADER += ' '*25 + 'Promo IA - 2020' + '\n'
        HEADER += '*'*61 + '\n'

        PARAM = ' '*5 + 'Parameters:' + '\n'
        PARAM += ' '*10 + '- c : ' + str(self.c) + '\n'
        PARAM += ' '*10 + '- Q : ' + str(self.Q) + '\n'
        PARAM += ' '*10 + '- alpha : ' + str(self.alpha) + '\n'
        PARAM += ' '*10 + '- beta : ' + str(self.beta) + '\n'
        PARAM += ' '*10 + '- rho : ' + str(self.rho) + '\n'
        PARAM += ' '*10 + '- nb_cities : ' + str(self.n) + '\n'
        PARAM += ' '*10 + '- nb_ants : ' + str(self._m) + '\n'
        PARAM += ' '*10 + '- nb_epoch : ' + str(self.nb_epoch) + '\n'
    
        _str = HEADER + PARAM
        return _str


if __name__ == '__main__':
    nb_cities = 30
    nb_ants = 10
    nb_epoch = 10
    world = World(nb_epoch, nb_cities, nb_ants, same_start = True)
    print(world)
    best_path = world.run_simulation()
    info = 'Final best: \n - path: {}'.format(best_path)
    print(info)

