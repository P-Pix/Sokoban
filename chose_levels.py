from random import randint

class Chose_level:

    def __init__(self):
        self.caisse = []
        self.balise = []
        self.player = []
        self.mape = []
        self.num_map = 1

    def selection(self, NIVEAU):
        print(f"le niv choisi est {NIVEAU}")
        if NIVEAU >= 1 and NIVEAU <= 18:
            self.num_map = NIVEAU
        else:
            self.num_map = randint(1, 18)

    #ce qui s'execute lors de l'appel du code
    def update(self):
        chargement = open(f"levels/sokoban{self.num_map}.xsb")
        print(f"le niveau choisi est = {self.num_map}")
        read = chargement.read()
        chargement.close
        read = read.split('\n')
        self.mape = []
        for lignes in read:
            self.mape.append(list(lignes))

        #créer les matrices des différents élément qui suivent la matrice dans le xsb
        #note : je vais reduire le code lors du prochain cour ;)
        y = 0
        self.player = []
        self.caisse = []
        self.balise = []
        val_caisse = True
        val_perso = True
        caisse_suiv = 0
        num_caisse = 0
        les_caisses = []
        for ligne in self.mape:
            x = 0
            for elem2 in ligne:
                if elem2 == '.':
                    self.balise.append([y, x])
                elif elem2 == 'p':
                    for elem3 in ligne:
                        if elem3 != ' ':
                            if elem3 != 'p':
                                if val_perso:
                                    spawn_1 = int(elem3)
                                    val_perso = False
                                else:
                                    spawn_2 = int(elem3)
                                    val_perso = True
                        else:
                            spawn = (spawn_1 * 10) + spawn_2
                            self.player.append(spawn)
                elif elem2 == 'c':
                    for elem3 in ligne:
                        if elem3 != ' ':
                            if elem3 != 'c':
                                if val_caisse:
                                    spawn_caisse_1 = int(elem3)
                                    val_caisse = False
                                else:
                                    spawn_caisse_2 = int(elem3)
                                    val_caisse = True
                        else:
                            if caisse_suiv == 2:
                                num_caisse += 1
                                caisse_suiv = 0
                            else:
                                caisse_suiv += 1
                            spawn_caisse = (spawn_caisse_1 * 10) + spawn_caisse_2
                            les_caisses.append(spawn_caisse)
                x += 1
            y += 1
        decompte = True
        for place in les_caisses:
            if decompte:
                place_1 = place
                decompte = False
            else:
                self.caisse.append([place_1, place])
                decompte = True