import pygame

#determination et création des elements pour le visuel de l'utilisateur
class Visuel:

    def __init__(self):
        self.img_herbe = self.open_img("weed.png")
        self.img_perso = self.open_img("heros.png")
        self.img_mur = self.open_img("mur.png")
        self.img_caisse = self.open_img("caisse.png")
        self.img_cible = self.open_img("ciblage_tro-oof.png")

    #ce que vas devoir faire la class à chaque fois qu'elle est appeler
    def update(self, MATRICE, screen):
        tableau = MATRICE.grille
        pos_y = 0
        for ligne in tableau:
            pos_x = 0
            for tile in ligne:
                if tile == 'p':
                    return
                self.condition_tile(tile, pos_x, pos_y, screen)
                pos_x += 1
            pos_y += 1

    #appel des tuiles pour les mettrent en code
    def open_img(self, nom):
        return pygame.image.load(f"picture/{nom}")

    #choisir la tuile à ajouter sur l'écran pygame
    def condition_tile(self, tile, x, y, screen):
        if tile == '0':
            self.ajout_image(x, y, self.img_herbe, screen)
        elif tile == '#':
            self.ajout_image(x, y, self.img_mur, screen)
        elif tile == '$':
            self.ajout_image(x, y, self.img_caisse, screen)
        elif tile == '.':
            self.ajout_image(x, y, self.img_cible, screen)
        elif tile == '@':
            self.ajout_image(x, y, self.img_perso, screen)

    #ajouter la tuile sur l'écran de pygame avec ses coordonées
    def ajout_image(self, x, y, name, screen):
        screen.blit(name, (x * 32, y * 32))