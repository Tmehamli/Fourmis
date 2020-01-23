import copy
import random as rd
import numpy as np

class Fourmis():
    Q = rd.uniform(0,1) 
    def __init__(self):
        self._chemin = []
        self._alpha = rd.uniform(0,1) 
        self._beta = rd.uniform(0,1)

    def ChoixDestination(self, start, Plan_gam_distance_phero):
        # target = ('destination', 'proba')
        target = ('ville', 0)
        possible_target = {}
        for duo_v, g_d_ph in Plan_gam_distance_phero.items():
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
        return target

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

    def random_start(self, univisted):
        i_rd_start = np.random.randint(0, len(univisted))
        start = univisted[i_rd_start]
        # univisted.pop(i_rd_start)
        return start

    def update_phero(self, Plan_gam_distance_phero):
        path_duo_v = []
        duo_v = [self._chemin[0], '']
        for ville in self._chemin[1:]:
            if (duo_v[0], ville) in Plan_gam_distance_phero:
                duo_v[1] = ville
            elif (ville, duo_v[0]) in Plan_gam_distance_phero:
                temp = duo_v[0]
                duo_v[0] = ville
                duo_v[1] = temp
            else:
                pass
            path_duo_v.append(copy.deepcopy(duo_v))
            duo_v = [ville, '']
        print(path_duo_v)
        Plan_gam_distance_phero[duo_v][2] += self.Q/len(self._chemin)

    def AjouterChoix(self, destination):
        self._chemin.append(destination)