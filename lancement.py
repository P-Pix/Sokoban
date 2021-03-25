import pygame
from matrix import Matrice
from visuel import Visuel
from run_victory import Win
from run import Run
from run_level import Run_Level
"""
from AI import Etats
from AI import Heuristic
"""
#initialisation habituel de pygame
pygame.init()
pygame.display.set_caption("Sokoban")
screen = pygame.display.set_mode((800, 420))
pygame.display.set_icon(pygame.image.load("picture/heros.png"))

#determination d'élément et des class
running = True
execution = True
VISU = Visuel()
WIN = Win()
RUN = Run()
#Heuri = Heuristic() 
RUN_LEVEL = Run_Level()
Matrice = Matrice()
#Etat = Etats()
update_screen = False
COLOR = pygame.Color(0)
FONT = pygame.font.SysFont("monospace", 25)
tous_les_etats_pour_le_bot = []
NIVEAU = 0
VICTOIRE = FONT.render("Bravo tu as gagné", 1, (255, 255, 255))
REJOUER = FONT.render("Pour rejouer = 'a'    Pour quitter = 'b'", 1, (255, 255, 255))

#fonction pour afficher la MATRICE agréablement dans le terminale
def affiche(grille):
	for ligne in grille:
		print("\t".join([str(val) for val in ligne]))

#lorsque le jeu s'éxécute
while running:
    #vérifier si le joueur est en fase de jeu ou non
    if Matrice.level_running:
        #fase de selection du niveau
        NIVEAU, Matrice.level_running, Matrice.victoire, running = RUN_LEVEL.update(NIVEAU, screen)
    elif not Matrice.level_running and not Matrice.victoire:
        #fase de jeu
        if execution:
            Matrice.init_lancement(NIVEAU)
            execution = False
            Matrice = Matrice.move([0, 0])
            update_screen = True
        move, running = RUN.update() 
        if move is not None:
            Matrice = Matrice.move(move)
            update_screen = True
    elif Matrice.victoire:
        #fase de demande pour rejouer ou quitter
        running, NIVEAU, Matrice = WIN.update(Matrice, screen, running, NIVEAU)
        execution = True
    if update_screen:
        affiche(Matrice.grille)
        #Etat.receveMap(Matrice.grille)
        #Heuri.boxMalPlacer(Matrice.correct)
        #fase de maj du screen
        tous_les_etats_pour_le_bot.append(Matrice)
        screen.fill(COLOR)
        #affiche(new_matrice)
        VISU.update(Matrice, screen)
        Matrice.texte_screen(screen)
        pygame.display.flip()
        update_screen = False

print(f"etat running = {running}")
pygame.quit()