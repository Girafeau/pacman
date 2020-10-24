from Personnage import Personnage


class PacMan(Personnage):

    pass

    def manger_bonbon(self):
        if self.carte.cases[self.x][self.y].bonbon == True:
            self.carte.cases[self.x][self.y].bonbon = False