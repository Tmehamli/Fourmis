import copy
import random as rd
import numpy as np

class Fourmis():
    Q = 1
    RHO = 0.25
    # Q = rd.uniform(0,1) 
    def __init__(self, g_d_p):
        self._chemin = []
        self._alpha = 0.5#rd.uniform(0,1) 
        self._beta = 0.30#rd.uniform(0,1)
        self.g_d_p = copy.deepcopy(g_d_p)
        self.phero_map = {}
        for duo_v, _gdp in g_d_p.items():
            self.phero_map[duo_v] = copy.deepcopy(_gdp[2])
        self.start = None
        self.last_pos = None
    def update_gdp(self, g_d_p):
        self.g_d_p = copy.deepcopy(g_d_p)
        for duo_v, _gdp in g_d_p.items():
            self.phero_map[duo_v] = copy.deepcopy(_gdp[2])
    def random_start(self, _unvisted):
        unvisted = _unvisted
        i_rd_start = np.random.randint(0, len(unvisted))
        self.start = copy.deepcopy(unvisted[i_rd_start])
        self.last_pos = copy.deepcopy(self.start)
        unvisted.pop(i_rd_start)
        return unvisted

    def ChoixDestination(self):
        # target = ('destination', 'foba')
        target = ('ville', 0)
        possible_target = {}
        start = self.last_pos
        for duo_v, g_d_ph in self.g_d_p.items():
            if start in duo_v:
                if (duo_v[0] == start and duo_v[1] not in self._chemin) or (duo_v[1] == start and duo_v[0] not in self._chemin):
                    possible_target[duo_v] = g_d_ph
        for duo_v, g_d_ph in possible_target.items():
            # p_den = self.init_p_den(duo_v, possible_target)
            prob = self.calcul_prob(duo_v, possible_target)
            if prob > target[1]:
                if duo_v[0] != start:
                    t = duo_v[0]
                else:
                    t = duo_v[1]
                target = (t, prob)
        self._chemin.append(target[0])
        self.last_pos = target[0]

    def init_p_den(self, duo_v, possible_target):
        p_den = 0
        g_t = possible_target[duo_v][0]
        d_t = possible_target[duo_v][1]
        ph_t = possible_target[duo_v][2]
        p_den += g_t + ((1/d_t)**self._alpha)*(ph_t**self._beta)
        if p_den == 0:
            p_den = 1
        return p_den
      
    def calcul_prob(self, duo_v, possible_target):
        g_t = possible_target[duo_v][0]
        d_t = possible_target[duo_v][1]
        ph_t = possible_target[duo_v][2]
        p_num = g_t + ((1/d_t)**self._alpha)*(ph_t**self._beta)
        sum_g = 0
        for val in possible_target.values():
            sum_g += val[0]
        p_den = sum_g + ((1/d_t)**self._alpha)*(ph_t**self._beta)
        p = p_num/p_den
        return p

    def update_phero(self):
        path_duo_v = []
        duo_v = [self._chemin[0], '']
        for ville in self._chemin[1:]:
            if (duo_v[0], ville) in self.phero_map:
                duo_v[1] = ville
            elif (ville, duo_v[0]) in self.phero_map:
                temp = duo_v[0]
                duo_v[0] = ville
                duo_v[1] = temp
            else:
                pass
            path_duo_v.append(copy.deepcopy(duo_v))
            duo_v = [ville, '']
        path_duo_v = [tuple(duo_v) for duo_v in path_duo_v]
        self.l_k = 0
        for duo_v in path_duo_v:
            self.l_k += self.g_d_p[duo_v][1]
        for duo_v in path_duo_v:
            self.phero_map[duo_v] += self.Q/self.l_k
