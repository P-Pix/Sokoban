import pygame
import copy
from chose_levels import Chose_level

class Matrice:

    def __init__(self):
        self.level = Chose_level()
        self.stock = [0, 0]
        self.element = ''
        self.compar = [0, 0]
        self.victoire = False
        self.level_running = True
        self.total_dep = 0
        self.font = pygame.font.SysFont("monospace", 25)
        self.blanc = (255, 255, 255)
        self.affiche = self.level.mape
        self.grille = self.level.mape #correct
        self.pos_player = self.level.player #correct
        self.caisses = self.level.caisse #correct
        self.balise = self.level.balise #correct
        self.num_map = self.level.num_map #correct

    def init_lancement(self):
        self.grille = self.level.mape #correct
        self.pos_player = self.level.player #correct
        self.caisses = self.level.caisse #correct
        self.balise = self.level.balise #correct
        self.num_map = self.level.num_map #correct
        self.victoire = False
        self.level_running = True

    #mise à jour de la matrice
    def update(self):
        affiche_1 = []
        fin = False
        affiche_1 = copy.deepcopy(self.grille)
        affiche_1[self.pos_player[0]][self.pos_player[1]] = '@'
        print(f"les caisses sont = {self.caisses}")
        for elem in self.caisses:
            affiche_1[elem[0]][elem[1]] = '$'
        self.affiche = affiche_1
        return Matrice()
    
    #verification de différents éléments avant de move
    def move(self, coord):
        self.compar[0] = self.pos_player[0] + coord[0]
        self.compar[1] = self.pos_player[1] + coord[1]
        #verifier si il n'y a pas de mur
        if self.affiche[self.compar[0]][self.compar[1]] != "#":
            #verifie si il y a une caisse devant
            if self.affiche[self.compar[0]][self.compar[1]] == '$':
                #verifie si devant la caisse il n'y a pas d'élément solid
                if self.affiche[self.compar[0] + coord[0]][self.compar[1] + coord[1]] != '#':
                    if self.affiche[self.compar[0] + coord[0]][self.compar[1] + coord[1]] != '$':
                        #recherche de la caisse
                        compteur = 0
                        for unite in self.caisses:
                            if unite == self.compar:
                                #deplacement de la caisse
                                #print(unite)
                                self.caisses[compteur][0] = self.pos_player[0] + coord[0] + coord[0]
                                self.caisses[compteur][1] = self.pos_player[1] + coord[1] + coord[1]
                            compteur += 1
                    else:
                        print("impossible")
                        return self.update()
                else:
                    print("impossible")
                    return self.update()
            #deplacement du personnage et stockage de sa position précédente pour refaire la matrice
            self.pos_player[0] += coord[0]
            self.pos_player[1] += coord[1]
            self.total_dep += 1
            #print(f"la coordonné du perso est = {self.pos_player}")
            return self.update()
        else:
            print("impossible")
            return self.update()
    
    def victory(self):
        self.correct = 0
        print(f"les caisses sont = {self.caisses}")
        for caisse in self.caisses:
            for case in self.balise:
                if caisse == case:
                    self.correct += 1
                    if self.correct == len(self.caisses):
                        self.victoire = True
    
    def texte_screen(self, screen):
        niveau_txt = self.font.render(f"Le niveau actuel est le niveau {self.level.num_map}", 1, self.blanc)
        screen.blit(niveau_txt, (20, 340))
        caisse_text = self.font.render(f"Il y a {self.correct} / {len(self.caisses)} caisse(s) bien placé", 1, self.blanc)
        screen.blit(caisse_text, (20, 360))
        move_txt = self.font.render(f"Il y a {self.total_dep} deplacement(s) fait", 1, self.blanc)
        screen.blit(move_txt, (20, 380))

    def get_move(self):
        possibility = []
        possibility.append(self.test_move([-1, 0]))
        possibility.append(self.test_move([1, 0]))
        possibility.append(self.test_move([0, -1]))
        possibility.append(self.test_move([0, 1]))
        return possibility

    def test_move(self, direction):
        self.compare[0] = self.pos_bot[0] + direction[0]
        self.compare[1] = self.pos_bot[1] + direction[1]
        if self.affiche[self.compare[0]][self.compare[1]] != "#":
            #verifie si il y a une caisse devant
            if self.affiche[self.compare[0]][self.compare[1]] == '$':
                #verifie si devant la caisse il n'y a pas d'élément solid
                if self.affiche[self.compare[0] + direction[0]][self.compare[1] + direction[1]] != '#':
                    if self.affiche[self.compare[0] + direction[0]][self.compare[1] + direction[1]] != '$':
                        return direction