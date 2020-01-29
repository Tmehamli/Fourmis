import numpy as np
import math as m
class Fourmi:
    def __init__(self, iden, stat_pos):
        self.identity = iden
        self.start_pos = stat_pos
        self.memory = None
        self.current_pos = None
        self.l_k = None
        self.LK = None
        # self.t = 0
        # self.initialize()

    def initialize(self):
        self.l_k = 0
        self.LK = []
        self.memory = []
        self.current_pos = self.start_pos
        self.memory.append(self.current_pos)

    def make_choice(self, i_v, phero_map, dist_m, alpha, beta):
        # array of probabilities
        nb_dest = len(dist_m[0])
        p = np.zeros(nb_dest)
        if len(self.memory) < nb_dest:
            # index of destination 
            j_v_L = np.arange(nb_dest)
            for j_v in j_v_L:
                den = 0
                num = 0
                if j_v not in self.memory:
                    for j, d in enumerate(dist_m[i_v]):
                        # for each destination
                        if j != i_v:
                            den_to_add = m.pow(phero_map[i_v, j], alpha) * m.pow(1/d, beta)
                            if j == j_v:
                                num = den_to_add
                            den += den_to_add
                        else : pass
                    p[j_v] = num / den
        # ending the path with start pos
        else:
            p[self.start_pos] = 1
        print(self.identity)
        print(dist_m)
        choice = np.argmax(p)
        print([i_v, choice])
        self.l_k += dist_m[i_v, choice]
        self.LK.append(self.l_k)
        return choice

    def apply_choice(self, new_pos):
        self.current_pos = new_pos
        self.memory.append(new_pos)
        pass

