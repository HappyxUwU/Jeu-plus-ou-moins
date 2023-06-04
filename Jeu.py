import sys
from random import randint
from tkinter import *
import pygame
pygame.mixer.init()

essais = 15
nombre = randint(0, 10000)
print(nombre)

def defaite():
    pygame.mixer.music.load("sons/boom.mp3")
    pygame.mixer.music.play(loops=0)

def victoire():
    pygame.mixer.music.load("sons/vic.mp3")
    pygame.mixer.music.play(loops=0)

def boutton_verif():
    pygame.mixer.music.load("sons/select.mp3")
    pygame.mixer.music.play(loops=0)

def boutton_reset():
    pygame.mixer.music.load("sons/reset.mp3")
    pygame.mixer.music.play(loops=0)

def moins():
    pygame.mixer.music.load("sons/c_plus.mp3")
    pygame.mixer.music.play(loops=0)

def plus():
    pygame.mixer.music.load("sons/c_moins.mp3")
    pygame.mixer.music.play(loops=0)
    
def init_jeu():
    boutton_reset()
    global essais, nombre
    essais = 15
    nombre = randint(0, 10000)
    print(nombre)
    Resultat.set("")
    Essais_restants.set("Nombre d'essais restants : " + str(essais))
    Valeur.set("0")

    bouton_rejouer.pack_forget()

def verif():
    exp.pack_forget()
    boutton_verif()
    global essais
    if essais > 0:
        if int(Valeur.get()) > nombre:
            plus()
            Resultat.set("C'est moins")
            essais -= 1
        elif int(Valeur.get()) < nombre:
            moins()
            Resultat.set("C'est plus")
            essais -= 1
        elif int(Valeur.get()) == nombre:
            victoire()
            bouton_rejouer.pack()
            Resultat.set("C'est gagné")
        Essais_restants.set("Nombre d'essais restants : " + str(essais))
    else:
        defaite()
        bouton_rejouer.pack()
        Resultat.set("C'est perdu ! Le chiffre était " + str(nombre))
        

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title("Plus ou moins")

Valeur = StringVar()
Valeur.set("0")

#Titre
T = Text(Mafenetre, height = 5, width = 52)
titre = Label(Mafenetre, text = "PLUS OU MOINS !")
titre.config(font =("Courier", 14))
titre.pack()

#explication regles
ex = Text(Mafenetre, height = 3, width = 10)
exp = Label(Mafenetre, text = "Il faut deviner le chiffre entre 0 et 10,000 vous avez 15 essais !")
exp.config(font =("Courier", 14))
exp.pack()

# Création d'un widget Spinbox
boite = Spinbox(Mafenetre, from_=0, to=10000, increment=1, textvariable=Valeur, width=10, bg='white')
boite.pack(padx=30, pady=10)

# Création d'un widget Label
Resultat = StringVar()
Resultat.set("")
Label(Mafenetre, textvariable=Resultat).pack(padx=200, pady=5)

#affiche des nombres d'essais
Essais_restants = StringVar()
Essais_restants.set("Nombre d'essais restants : " + str(essais))
Label(Mafenetre, textvariable=Essais_restants).pack(padx=5, pady=5)

#bouton pour verifier
button_verif = Button(Mafenetre, text="devinez", command=verif, bg='cyan')
button_verif.pack()

#bouton pour rejouer
bouton_rejouer = Button(Mafenetre, text="Rejouer", command=init_jeu, bg='red')

Mafenetre.mainloop()

