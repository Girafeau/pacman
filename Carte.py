import numpy as np

from Case import Case


class Carte:

    def __init__(self):
        self.cases = np.array([[Case('mur'), Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur')],
                              [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
                               [Case('mur'), Case('vide'),Case('vide'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('mur'),Case('vide'),Case('mur')],
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