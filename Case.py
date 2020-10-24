class Case:

    def __init__(self, type):
        self.type = type
        if type == 'mur':
            self.bonbon = False
        else:
            self.bonbon = True
