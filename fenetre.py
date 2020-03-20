# importation du module complet :
import pygame

# importation des constantes :
from pygame.locals import *

# initialisation du module pygame :
pygame.init()

# création et initialisation de la variable fenêtre :
fenetre = pygame.display.set_mode((640, 480))

# chargement de l'image de fond et conversion au bon format :
fond = pygame.image.load("background.jpg").convert()

# rendre transparent le blanc de l'image de fond grâce à la méthode set_colorkey() de l'objet surface :
#fond.set_colorkey((0, 0, 0))

# collage de l'image de fond grâce à la fonction blit de l'objet fenêtre en haut à gauche :
fenetre.blit(fond, (0, 0))

# chargement de l'image du personnage et conversion au bon format avec gestion de la transparence :
perso = pygame.image.load("perso.png").convert_alpha()

# stockage de la position du personnage dans la variable position_perso grâce à la methode get_rect() de l'objet \
# surface. la méthode get_rect() permet de stocker les coordonnées du personnage :
position_perso = perso.get_rect()

# collage de l'image du personnage sur le fond grâce à la fonction blit de l'objet fenêtre :
#fenetre.blit(perso, (200, 300))
fenetre.blit(perso, position_perso)

# Rafraîchissement de l'écran qui permet d'afficher toutes les modifications demandées :
pygame.display.flip()

# création et initialisation de la variable affiche qui servira pour faire une boucle infinie :
affiche = True

# boucle qui permet à la fenetre de rester affichée :
while affiche:
    # boucle qui parcours tous les évènements utilisateurs :
    for event in pygame.event.get():
        # si le type de l'évènement est de quitter la fenetre :
        if event.type == QUIT:
            # on interrompt l'affichage :
            affiche = False
        # si le type de l'évènement est d'enfoncer une touche du clavier :
        if event.type == KEYDOWN:
            # si la touche préssée est la barre d'espace :
            if event.key == K_SPACE:
                print("espace")
            # si la touche préssée est la touche entrée :
            if event.key == K_RETURN:
                print("entrée")
            # si la touche préssée est la flèche du bas :
            if event.key == K_DOWN:
                #position_perso.move(0, 3)
                print("bas")
            # si la touche préssée est la flèche droite :
            if event.key == K_RIGHT:
                position_perso.move(3, 0)
            # si la touche préssée est la flèche du haut :
            if event.key == K_UP:
                position_perso.move(0, -3)
            # si la touche préssée est la flèche gauche :
            if event.key == K_LEFT:
                position_perso.move(-3, 0)

    # recollage des personnages et du fond :
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)

    # rafraichissement de l'écran pour prendre en compte les modifications apportées :
    pygame.display.flip()
