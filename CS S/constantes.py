from random import*
import pygame
from pygame.locals import*
pygame.init()

"""delay & interval"""
delay = 5
interval = 50


"""contiuer"""
continuer = True
jeu = True

"""tailles des rectangles"""
taille_cible = 10
taille_héro = 10


"""position du héro"""
lead_x = 250
lead_y = 200
lead_x2 = lead_x
lead_y2 = lead_y


"""taille de la fenêtre"""
fontx = 500
fonty = 400

"""coordonées aléatoires"""
rx = randint(taille_cible,fontx - taille_cible)
ry = randint(taille_cible,fonty - taille_cible)

"""couleurs"""
white = (255,255,255)
black = (0,0,0)
grey = (50,50,50)
yellow = (255, 255, 0)

"""scores"""
score1 = 0
score2 = 0
score_total = 0
score_total_obj = 3

"""caractéristiques texte score"""
police=pygame.font.Font('freesansbold.ttf',15)
aff_score1 = ("Score : {}").format(score1)
aff_score2 = ("Score : {}").format(score2)


"""indicage des touches """
z = 119
s = 115
q = 97
d = 100
LEFT = 276
UP = 273
DOWN = 274
RIGHT = 275