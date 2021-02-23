import pygame
from matrix import Matrice
from visuel import Visuel
from run_victory import Win
from run import Run
from run_level import Run_Level

#initialisation habituel de pygame
pygame.init()
pygame.display.set_caption("Sokoban")
screen = pygame.display.set_mode((800, 420))
pygame.display.set_icon(pygame.image.load("picture/heros.png"))

#determination d'élément et des class
running = True
VISU = Visuel()
WIN = Win()
RUN = Run()
RUN_LEVEL = Run_Level()
MATRICE = Matrice()
update_screen = False
new_matrice = []
COLOR = pygame.Color(0)
FONT = pygame.font.SysFont("monospace", 25)
tous_les_etats_pour_le_bot = []
NIVEAU = 0
CHOIX_NIVEAU_TXT = FONT.render("Niveau désiré 'a' pour validé", 1, (255, 255, 255))
VICTOIRE = FONT.render("Bravo tu as gagné", 1, (255, 255, 255))
REJOUER = FONT.render("Pour rejouer = 'a'    Pour quitter = 'b'", 1, (255, 255, 255))

#fonction pour afficher la MATRICE agréablement dans le terminale
def affiche(grille):
	for ligne in grille:
		print("\t".join([str(val) for val in ligne]))

#lorsque le jeu s'éxécute
while running:
    #vérifier si le joueur est en fase de jeu ou non
    if MATRICE.level_running:
        #fase de selection du niveau
        update_screen, new_matrice, running, NIVEAU = RUN_LEVEL.update(running, NIVEAU, screen, update_screen)
    elif not MATRICE.level_running and not MATRICE.victoire:
        #fase de jeu
        new_matrice, update_screen, running = RUN.update(running, update_screen)
    elif MATRICE.victoire:
        #fase de demande pour rejouer ou quitter
        WIN.update(screen, running, NIVEAU)
    if update_screen:
        #fase de maj du screen
        tous_les_etats_pour_le_bot.append(new_matrice)
        screen.fill(COLOR)
        #affiche(new_matrice)
        VISU.update(new_matrice, screen)
        MATRICE.victory()
        MATRICE.texte_screen(screen)
        pygame.display.flip()
        update_screen = False

print(f"etat running = {running}")
pygame.quit()