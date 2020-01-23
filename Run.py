from World import Monde
from Fourmis import Fourmis

import copy
import random as rd
rd.seed(42)

def run(nb_ants, nb_epoch):
    ants = [Fourmis() for f in range(nb_ants)]
    w = Monde()
    for ite in range(nb_epoch):
        new_Plan_gam_distance_phero = copy.deepcopy(w.Plan_gam_distance_phero)
        unvisited = w.Villes
        for f in ants:
            start = f.random_start(unvisited)
            while len(w.Villes) - len(f._chemin) > 0:
                start, _ = f.ChoixDestination(start, w.Plan_gam_distance_phero)
                print(start, f._chemin)
            new_Plan_gam_distance_phero = f.update_phero(new_Plan_gam_distance_phero)
        w.Plan_gam_distance_phero = new_Plan_gam_distance_phero
            
nb_ants, nb_epoch = 1, 1
run(nb_ants, nb_epoch)