class Personnage:

    def __init__(self, x, y, carte):
        self.x = x
        self.y = y
        self.carte = carte

    def avancer_haut(self):
        if self.carte.cases[self.x][self.y - 1].type != 'mur':
            self.y = self.y - 1

    def avancer_bas(self):
        if self.carte.cases[self.x][self.y + 1].type != 'mur':
            self.y = self.y + 1

    def avancer_gauche(self):
        if self.carte.cases[self.x - 1][self.y].type != 'mur':
            self.x = self.x - 1

    def avancer_droite(self):
        if self.carte.cases[self.x + 1][self.y].type != 'mur':
            self.x = self.x + 1