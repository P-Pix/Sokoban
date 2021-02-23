import pygame
from matrix import Matrice

class Run():

    def __init__(self):
        self.MATRICE = Matrice()
        self.new_matrice = []

    def update(self, running, update_screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #recupération des touches appuyer et faire les deplacement
                if event.key == pygame.K_RIGHT:
                    self.new_matrice = self.MATRICE.move([0, 1])
                elif event.key == pygame.K_LEFT:
                    self.new_matrice = self.MATRICE.move([0, -1])
                elif event.key == pygame.K_UP:
                    self.new_matrice = self.MATRICE.move([-1, 0])
                elif event.key == pygame.K_DOWN:
                    self.new_matrice = self.MATRICE.move([1, 0])
                #une fois le deplacement fais mettre à jour l'écran pour eviter de sur charger l'ordi en rechargeant constament
                update_screen = True
                return self.new_matrice, update_screen, running