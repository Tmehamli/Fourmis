from World import Monde
from Fourmis import Fourmis

import copy
import random as rd
import numpy as np
rd.seed(42)

def run(nb_ants, nb_epoch):
    w = Monde()
    ants = [Fourmis(w.Plan_gam_distance_phero) for f in range(nb_ants)]
    phero_map = np.asarray(list(w.Plan_gam_distance_phero.values()))[:,2]
    unvisited = copy.deepcopy(w.Villes)
    for f in ants:
        unvisited = f.random_start(unvisited)
    all_f_path_past = []
    nb_ite = 0
    for ite in range(nb_epoch):
        f._chemin = []
        L_K = []
        all_f_path = []
        f.update_gdp(w.Plan_gam_distance_phero)
        f.last_pos = f.start
        for f in ants:
            while len(w.Villes) - len(f._chemin) > 0:
                f.ChoixDestination()
            f.update_phero()
            L_K.append(f.l_k)
            all_f_path.append(f._chemin)
        i_best = np.argmin(L_K)
        print(i_best)
        phero_map = ants[0].RHO * phero_map + np.asarray(list(ants[i_best].phero_map.values()))
        for i, (duo_v, g_d_p) in enumerate(w.Plan_gam_distance_phero.items()):
            w.Plan_gam_distance_phero[duo_v][2] = phero_map[i]
        nb_ite = ite
        print(ite-1, all_f_path_past)
        print(ite, all_f_path)
        print(ite, L_K)
        print('\n')
        # if all_f_path_past == all_f_path:
        #     break
        all_f_path_past = copy.deepcopy(all_f_path)
        all_f_path = []
    return w, ants[i_best], nb_ite
nb_ants, nb_epoch = 2, 3
w, f_best, nb_ite = run(nb_ants, nb_epoch)
print(f_best._chemin)
print(nb_ite)
for duo_v, g_d_p in w.Plan_gam_distance_phero.items():
    print(duo_v, g_d_p)
