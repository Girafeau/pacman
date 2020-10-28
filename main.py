import tkinter
import random
import numpy as np

from Carte import Carte
from Fantome import Fantome
from PacMan import PacMan

# Création des instances.
carte = Carte()
nb_bonbons=carte.nb_bonbons()
pacman = PacMan(1, 1, carte)
fantomes = np.array([Fantome(8, 1, carte), Fantome(9, 1, carte), Fantome(10, 1, carte)])

# Création de la fenêtre.
fenetre = tkinter.Tk()
dessin = tkinter.Canvas(fenetre, height=1000, width=1000)

dessin_cases = np.array(carte.cases, copy=True)
def dessiner_carte():
    global dessin
    for x in range(0, len(carte.cases)):
        for y in range(0, len(carte.cases[x])):
            if carte.cases[x][y].type == 'mur':
                dessin_cases[x][y] = dessin.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="black")
            else:
                dessin.create_rectangle(x * 50, y * 50, x * 50 + 50, y * 50 + 50, fill="grey")
                dessin_cases[x][y] = dessin.create_oval(x * 50 + 20, y * 50 + 20, x * 50 + 30, y * 50 + 30, fill="pink")

dessin_pacman = 0
def dessiner_pacman():
    global dessin
    global dessin_pacman
    global pacman
    dessin_pacman = dessin.create_oval(pacman.x * 50 + 15, pacman.y * 50 + 15, pacman.x * 50 + 35,
                                            pacman.y * 50 + 35, fill="yellow")

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
        dessin_fantomes[i] = dessin.create_rectangle(fantomes[i].x * 50 + 15, fantomes[i].y * 50 + 15, fantomes[i].x * 50 + 35, fantomes[i].y * 50 + 35,
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
    global nb_bonbons
    if direction == 'z':
        pacman.avancer_haut()
    if direction == 's':
        pacman.avancer_bas()
    if direction == 'q':
        pacman.avancer_gauche()
    if direction == 'd':
        pacman.avancer_droite()
    bonbon_present = pacman.manger_bonbon()
    if bonbon_present:
        nb_bonbons=nb_bonbons-1
    rafraichir_case(pacman.x, pacman.y)
    effacer_pacman()
    dessiner_pacman()

def dessiner_fantome(i, couleur):
    global dessin
    global dessin_fantomes
    global fantomes
    dessin_fantomes[i] = dessin.create_rectangle(fantomes[i].x * 50 + 15, fantomes[i].y * 50 + 15, fantomes[i].x * 50 + 35, fantomes[i].y * 50 + 35,
                                    fill=couleur)

def avancer_fantomes():
    global fantomes
    effacer_fantomes()
    for i in range (0, len(fantomes)):
        if voir_pacman(fantomes[i]) == True:
            print("voit")
            suivre_pacman(fantomes[i])
            dessiner_fantome(i, "brown")
        else:
            rand = random.randint(0, 3)
            if(rand == 0):
                fantomes[i].avancer_haut()
            if(rand == 1):
                fantomes[i].avancer_bas()
            if(rand == 2):
                fantomes[i].avancer_droite()
            if(rand == 3):
                fantomes[i].avancer_gauche()
            dessiner_fantome(i, "purple")


def voir_pacman(fantome):
    global fantomes
    global pacman
    global carte
    mur = False
    if pacman.x == fantome.x:
        if pacman.y < fantome.y:
            for i in range(pacman.y, fantome.y):
                if carte.cases[pacman.x][i].type == 'mur':
                    mur = True
            return mur == False
        else:
            for i in range(fantome.y, pacman.y):
                if carte.cases[pacman.x][i].type == 'mur':
                    mur = True
            return mur == False
    if pacman.y == fantome.y:
        if pacman.x < fantome.x:
            for i in range(pacman.x, fantome.x):
                if carte.cases[i][pacman.y].type == 'mur':
                    mur = True
            return mur == False
        else:
            for i in range(fantome.x, pacman.x):
                if carte.cases[i][pacman.y].type == 'mur':
                    mur = True
            return mur == False
    return False

def suivre_pacman(fantome):
    if fantome.y > pacman.y:
        fantome.avancer_haut()
    if fantome.y < pacman.y:
        fantome.avancer_bas()
    if fantome.x > pacman.x:
        fantome.avancer_gauche()
    if fantome.x < pacman.x:
        fantome.avancer_droite()



def est_perdu():
    for fantome in fantomes:
        if fantome.x == pacman.x:
            if fantome.y == pacman.y:
                return True
    return False

def est_gagne():
    return nb_bonbons==0

direction = 'rien'
def direction(event):
    global direction
    direction = event.char

def jeu():
    global fenetre
    global perdu

    frame = 0
    while True:
        frame = frame + 1
        if frame % 12000 == 0:
            if est_perdu() == False | est_gagne() == False:
                avancer_pacman()
            else:
                if est_perdu() == True:
                    dessin.create_text(100, 100, text="Vous avez perdu")
                else:
                    dessin.create_text(100, 100, text="Vous avez gagné")

        if frame % 11000 == 0:
            if est_perdu() == False | est_gagne() == False:
                avancer_fantomes()
            else:
                if est_perdu() == True:
                    dessin.create_text(100, 100, text="Vous avez perdu")
                else:
                    dessin.create_text(100, 100, text="Vous avez gagné")

        fenetre.update_idletasks()
        fenetre.update()


dessiner_carte()
dessiner_pacman()
dessiner_fantomes()
dessin.bind('<KeyPress>', direction)
dessin.pack()
dessin.focus_set()
jeu()