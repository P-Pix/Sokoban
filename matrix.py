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
        self.blanc = (255, 255, 255)
        self.affiche = self.level.mape
        self.grille = self.level.mape #correct
        self.pos_player = self.level.player #correct
        self.caisses = self.level.caisse #correct
        self.balise = self.level.balise #correct
        self.num_map = self.level.num_map #correct
        self.elem_precedent = []
        self.correct = 0

    def init_lancement(self, NIVEAU):
        self.level.selection(NIVEAU)
        self.level.update()
        self.grille = self.level.mape #correct
        self.pos_player = self.level.player #correct
        self.caisses = self.level.caisse #correct
        self.balise = self.level.balise #correct
        self.num_map = self.level.num_map #correct
        self.mape_font = copy.deepcopy(self.grille)
        self.victoire = False
        self.level_running = True

    #verification de différents éléments avant de move
    def move(self, coord):
        next = copy.deepcopy(self)
        next.compar[0] = next.pos_player[0] + coord[0]
        next.compar[1] = next.pos_player[1] + coord[1]
        #verifier si il n'y a pas de mur
        if next.grille[next.compar[0]][next.compar[1]] != '#':
            #verifie si il y a une caisse devant
            if next.grille[next.compar[0]][next.compar[1]] == '$':
                #verifie si devant la caisse il n'y a pas d'élément solid
                if next.grille[next.compar[0] + coord[0]][next.compar[1] + coord[1]] != '#':
                    if next.grille[next.compar[0] + coord[0]][next.compar[1] + coord[1]] != '$':
                        #recherche de la caisse
                        compteur = 0
                        for unite in next.caisses:
                            if unite == next.compar:
                                #deplacement de la caisse
                                next.caisses[compteur][0] = next.pos_player[0] + coord[0] + coord[0]
                                next.caisses[compteur][1] = next.pos_player[1] + coord[1] + coord[1]
                            compteur += 1
                    else:
                        print("impossible")
                        self.victory(next)
                        return next
                else:
                    print("impossible")
                    self.victory(next)
                    return next
            #deplacement du personnage et  stockage de sa position précédente pour refaire la matrice
            next.elem_precedent = next.mape_font[next.pos_player[0] + coord[0]][next.pos_player[1] + coord[1]]
            next.grille[next.pos_player[0]][next.pos_player[1]] = self.elem_precedent
            for elem in next.caisses:
                next.grille[elem[0]][elem[1]] = '$'
            next.pos_player[0] += coord[0]
            next.pos_player[1] += coord[1]
            next.grille[next.pos_player[0]][next.pos_player[1]] = '@'
            next.total_dep += 1
            self.victory(next)
            #print(f"la coordonné du perso est = {self.pos_player}")
            return next
        else:
            print("impossible")
            self.victory(next)
            return next
    
    def victory(self, next):
        next.correct = 0
        for caisse in next.caisses:
            for case in next.balise:
                if caisse == case:
                    next.correct += 1
                    if next.correct == len(next.caisses):
                        next.victoire = True
        next.correct -= len(next.caisses)
        next.correct *= -1
        
    
    def texte_screen(self, screen):
        font = pygame.font.SysFont("monospace", 25)
        niveau_txt = font.render(f"Le niveau actuel est le niveau {self.level.num_map}", 1, self.blanc)
        screen.blit(niveau_txt, (20, 340))
        caisse_text = font.render(f"Il y a {self.correct} / {len(self.caisses)} caisse(s) mal placé", 1, self.blanc)
        screen.blit(caisse_text, (20, 360))
        move_txt = font.render(f"Il y a {self.total_dep} deplacement(s) fait", 1, self.blanc)
        screen.blit(move_txt, (20, 380))
        ia_txt = font.render(f"'a' pour activer l'IA", 1, self.blanc)
        screen.blit(ia_txt, (20, 400))

        