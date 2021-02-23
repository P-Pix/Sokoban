import pygame
from matrix import Matrice

class Win():

    def __init__(self):
        self.MATRICE = Matrice()
        self.COLOR = pygame.Color(0)
        self.FONT = pygame.font.SysFont("monospace", 25)
        self.VICTOIRE = self.FONT.render("Bravo tu as gagné", 1, (255, 255, 255))
        self.REJOUER = self.FONT.render("Pour rejouer = 'a'    Pour quitter = 'b'", 1, (255, 255, 255))

    def update(self, screen, running, NIVEAU):
        screen.fill(self.COLOR)
        screen.blit(self.VICTOIRE, (300, 100))
        screen.blit(self.REJOUER, (100, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    running = False
                    pygame.quit()
                elif event.key == pygame.K_a:
                    NIVEAU = 0
                    self.MATRICE.victoire = False
                    self.MATRICE.level_running = True
                    screen.fill(COLOR)
            pygame.display.flip()