import pygame
from matrix import Matrice
from visuel import Visuel
from run_victory import Win
from run import Run
from run_level import Run_Level
from AIAll2 import ExeAI

#initialisation habituel de pygame
pygame.init()
pygame.display.set_caption("Sokoban")
screen = pygame.display.set_mode((800, 440))
pygame.display.set_icon(pygame.image.load("picture/heros.png"))

#determination d'élément et des class
running = True
execution = True
activeBot = False
VISU = Visuel()
ExeAI = ExeAI()
WIN = Win()
RUN = Run()
RUN_LEVEL = Run_Level()
Matrice = Matrice()
update_screen = False
COLOR = pygame.Color(0)
FONT = pygame.font.SysFont("monospace", 25)
NIVEAU = 0
VICTOIRE = FONT.render("Bravo tu as gagné", 1, (255, 255, 255))
REJOUER = FONT.render("Pour rejouer = 'a'    Pour quitter = 'b'", 1, (255, 255, 255))

#fonction pour afficher la MATRICE agréablement dans le terminale
def affiche(grille):
	for ligne in grille:
		print(" ".join([str(val) for val in ligne]))

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
        move, running, activeBot = RUN.update()
        if move is not None and not activeBot:
            Matrice = Matrice.move(move)
            update_screen = True
        if activeBot:
            nParcours = ExeAI.update(Matrice)
            print(nParcours)
            for movement in nParcours:
                if movement == "n" or movement == "N":
                    Matrice = Matrice.move([-1, 0])
                elif movement == "s" or movement == "S":
                    Matrice = Matrice.move([1, 0])
                elif movement == "e" or movement == "E":
                    Matrice = Matrice.move([0, 1])
                elif movement == "w" or movement == "W":
                    Matrice = Matrice.move([0, -1])
                screen.fill(COLOR)
                VISU.update(Matrice, screen)
                Matrice.texte_screen(screen)
                pygame.display.flip()
                pygame.time.delay(500)
            update_screen = True
            activeBot = False
    elif Matrice.victoire:
        activeBot =  False
        #fase de demande pour rejouer ou quitter
        running, NIVEAU, Matrice = WIN.update(Matrice, screen, running, NIVEAU)
        execution = True
    if update_screen:
        affiche(Matrice.grille)
        screen.fill(COLOR)
        VISU.update(Matrice, screen)
        Matrice.texte_screen(screen)
        pygame.display.flip()
        update_screen = False

print(f"etat running = {running}")
pygame.quit()