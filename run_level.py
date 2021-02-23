import pygame
from matrix import Matrice
from chose_levels import Chose_level

class Run_Level():

    def __init__(self):
        self.MATRICE = Matrice()
        self.LEVEL = Chose_level()
        self.FONT = pygame.font.SysFont("monospace", 25)
        self.COLOR = pygame.Color(0)
        self.CHOIX_NIVEAU_TXT = self.FONT.render("Niveau désiré 'a' pour validé", 1, (255, 255, 255))
        self.new_matrice = []

    def update(self, running, NIVEAU, screen, update_screen):
        screen.blit(self.CHOIX_NIVEAU_TXT, (200, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    NIVEAU += 1
                    screen.fill(self.COLOR)
                elif event.key == pygame.K_LEFT:
                    NIVEAU -= 1
                    screen.fill(self.COLOR)
                elif event.key == pygame.K_a:
                    print(Matrice())
                    print(self.MATRICE)
                    niveau_selectionne = NIVEAU % 19
                    self.lancement_niveau(niveau_selectionne)
                    self.MATRICE.level.update()
                    self.MATRICE.init_lancement()
                    self.new_matrice = self.MATRICE.update()
                    update_screen = True
        if NIVEAU % 19 != 0:
            choix_niveau = self.FONT.render(f"{NIVEAU % 19}", 1, (255, 255, 255))
        else:
            choix_niveau = self.FONT.render("Aleatoire", 1, (255, 255, 255))
        screen.blit(choix_niveau, (350, 200))
        pygame.display.flip()
        return update_screen, self.new_matrice, running, NIVEAU

    def lancement_niveau(self, NIVEAU):
        self.LEVEL.selection(NIVEAU)
        self.MATRICE.victoire = False
        self.MATRICE.level_running = False
        self.MATRICE.total_dep = 0
        self.MATRICE.level = self.LEVEL