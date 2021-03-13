import pygame
from matrix import Matrice

class Win():

    def __init__(self):
        self.COLOR = pygame.Color(0)
        self.FONT = pygame.font.SysFont("monospace", 25)
        self.VICTOIRE = self.FONT.render("Bravo tu as gagné", 1, (255, 255, 255))
        self.REJOUER = self.FONT.render("Pour rejouer = 'a'    Pour quitter = 'b'", 1, (255, 255, 255))

    def update(self, MATRICE, screen, running, NIVEAU):
        screen.fill(self.COLOR)
        screen.blit(self.VICTOIRE, (300, 100))
        screen.blit(self.REJOUER, (100, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    running = False
                elif event.key == pygame.K_a:
                    MATRICE = Matrice()
                    screen.fill(self.COLOR)
            pygame.display.flip()
        return running, NIVEAU, MATRICE