import numpy as np
import math as m
class Fourmi:
    def __init__(self, iden, stat_pos):
        self.identity = iden
        self.memory = []
        self.start_position = stat_pos
        self.t = 0
        # self.initialize()

    def initialize(self):
        pass

    def make_choice(self, i_v, phero_map, visibility_m, alpha, beta):
        # array of probabilities
        p = np.zeros(len(visibility_m[0]))
        # index of destination 
        j_v_L = np.arange(len(visibility_m[0]))
        for j_v in j_v_L:
            den = 0
            for j, n in enumerate(visibility_m[i_v]):
                # for each destination
                if j != i_v:
                    den_to_add = m.pow(phero_map[i_v, j], alpha) * m.pow(n, beta)
                    if j == j_v:
                        num = den_to_add
                    den += den_to_add
                else : pass
            p[j_v] = num / den
        print(p)
        return np.max(p)

    def apply_choice(self):
        pass

