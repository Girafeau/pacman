import tkinter
import random
import numpy as np

from Carte import Carte
from Fantome import Fantome
from PacMan import PacMan

# Création des instances.
carte = Carte()
pacman = PacMan(1, 1, carte)
fantomes = np.array([Fantome(1, 2, carte), Fantome(2, 2, carte), Fantome(3, 2, carte)])

# Création de la fenêtre.
fenetre = tkinter.Tk()
dessin = tkinter.Canvas(fenetre, height=1000, width=1000)

dessin_cases = np.array(carte.cases, copy=True)
def dessiner_carte():
    global dessin
    for x in range(0, len(carte.cases)):
        for y in range(0, len(carte.cases[x])):
            if carte.cases[x][y].type == 'mur':
                dessin_cases[x][y] = dessin.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="red")
            else:
                dessin.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="blue")
                dessin_cases[x][y] = dessin.create_rectangle(x * 50 + 20, y * 50 + 20, x * 50 + 30, y * 50 + 30, fill="green")


dessin_pacman = 0
def dessiner_pacman():
    global dessin
    global dessin_pacman
    global pacman
    dessin_pacman = dessin.create_rectangle(pacman.x * 50 + 20, pacman.y * 50 + 20, pacman.x * 50 + 30,
                                            pacman.y * 50 + 30, fill="yellow")

def effacer_pacman():
    global dessin
    global dessin_pacman
    dessin.delete(dessin_pacman)


dessin_fantomes = np.array([0, 0, 0])
def dessiner_fantomes():
    global dessin
    global dessin_fantomes
    global fantomes
    for i in range(0, len(fantomes)):
        dessin_fantomes[i] = dessin.create_rectangle(fantomes[i].x * 50 + 20, fantomes[i].y * 50 + 20, fantomes[i].x * 50 + 30, fantomes[i].y * 50 + 30,
                                    fill="purple")

def effacer_fantomes():
    global dessin
    global dessin_fantomes
    for dessin_fantome in dessin_fantomes:
        dessin.delete(dessin_fantome)

def rafraichir_case(x, y):
    global dessin_cases
    global dessin
    dessin.delete(dessin_cases[x][y])

def avancer_pacman():
    global pacman
    global direction
    if direction == 'z':
        pacman.avancer_haut()
    if direction == 's':
        pacman.avancer_bas()
    if direction == 'q':
        pacman.avancer_gauche()
    if direction == 'd':
        pacman.avancer_droite()
    pacman.manger_bonbon()
    rafraichir_case(pacman.x, pacman.y)
    effacer_pacman()
    dessiner_pacman()

def avancer_fantomes():
    for fantome in fantomes:
        rand = random.randint(0, 3)
        if(rand == 0):
            fantome.avancer_haut()
        if(rand == 1):
            fantome.avancer_bas()
        if(rand == 2):
            fantome.avancer_droite()
        if(rand == 3):
            fantome.avancer_gauche()

def est_perdu():
    for fantome in fantomes:
        if fantome.x == pacman.x:
            if fantome.y == pacman.y:
                return True
    return False

direction = 'rien'
def direction(event):
    global direction
    direction = event.char

def jeu():
    global fenetre
    global perdu

    frame = 0
    while est_perdu() == False:
        frame = frame + 1
        if frame % 12000 == 0:
            avancer_pacman()

        if frame % 10000 == 0:
            avancer_fantomes()
            effacer_fantomes()
            dessiner_fantomes()

        fenetre.update_idletasks()
        fenetre.update()


dessiner_carte()
dessiner_pacman()
dessiner_fantomes()
dessin.bind('<KeyPress>', direction)
dessin.pack()
dessin.focus_set()
jeu()