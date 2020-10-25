import numpy as np

from Case import Case


class Carte:

    def __init__(self):
        self.cases = np.array([[Case('mur'), Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur')],
                              [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                                [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                                [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                                [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                                [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur')],
                                [Case('mur'), Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur')]])

    def nb_bonbons(self):
         compteur = 0
         for t in self.cases:
          for case in t:
           if case.bonbon == True:
            compteur = compteur + 1
         return compteur