import random as rd
import numpy as np
rd.seed(42)

class Monde():
    def __init__(self):
        rd.seed(42)
        GAMMA = rd.uniform(0,1)
        self.Villes = ['A', 'B', 'C','D', 'E', 'F']
        self.Plan_gam_distance_phero = {
            (self.Villes[0],self.Villes[1]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[0],self.Villes[2]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[0],self.Villes[3]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[0],self.Villes[4]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[0],self.Villes[5]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[1],self.Villes[2]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[1],self.Villes[3]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[1],self.Villes[4]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[1],self.Villes[5]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[2],self.Villes[3]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[2],self.Villes[4]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[2],self.Villes[5]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[3],self.Villes[4]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[3],self.Villes[5]): np.asarray([GAMMA, rd.uniform(1, 20),.01]),
            (self.Villes[4],self.Villes[5]): np.asarray([GAMMA, rd.uniform(1, 20),.01])
        }