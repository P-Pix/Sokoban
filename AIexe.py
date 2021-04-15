    # Créé par ronan, le 05/04/2021 en Python 3.7


from sousAI import fileDePriorite, Noeud

class Astar:

    def updating(self, matrice, caisse):
        print(matrice.balise)
        print(set(dict(matrice.balise)))
        # U et V sont mal placée a remplacer par un push dans l'openlist
        u = Noeud(matrice.pos_player[0], matrice.pos_player[1], self.heuristic(matrice))
        v = Noeud(matrice.pos_player[0], matrice.pos_player[1], self.heuristic(matrice))
        closeList = []
        openList = fileDePriorite()
        chemin = []
        #heap.push
        #openlist pas close
        fileDePriorite.push(openList, matrice.pos_player)
        while openList != []:
            #u = openList.pop()
            if u.x == caisse[1] and u.y == caisse[0]:
                if self.compare2Noeuds(u, v) == 1:
                    for elem in closeList:
                        elem += 1
                        chemin.append(closeList[-elem])
                return chemin
            else:
                #Attention boucle sur tout les voisins
                elem = v.cout+ v.heuristic
                if not elem in closeList:
                    if not v.cout in closeList:
                        v.cout = u.cout + 1
                        v.heuristic = (v.cout + (abs(v.x - caisse[1]) + abs(v.y - caisse[0])))
                        #openList.
                        #Comme open file dde preorité pas append mais push
                        closeList.append([v.x, v.y])
            closeList.append([u.x, u.y])
            print(openList)
        return

    def cout(self, actions):
        #Fonction coup d'une action"
        return len([x for x in actions if x.islower()])

    def heuristic(self, matrice):
        complete = 0
        for balise in matrice.balise:
            for caisse in matrice.caisses:
                complete += abs(balise[1] - caisse[1]) + abs(balise[0] - caisse[0])
        return complete

    def compare2Noeuds(self, n1, n2):
        if n1 < n2:
            return 1
        elif n1 == n2:
            return 0 
            return -1







    def update(self, matrice, objectif):
        depart = [matrice.pos_player[0], matrice.pos_player[1], 0, self.heuristic(matrice)]
        closedList = []
        openList = []
        openList.append(depart)
        compteur = 0
        while openList != []:
            print(openList)
            print(compteur)
            u = openList[compteur]
            matrice.victory(matrice)
            if matrice.victoire:
                return inverse(openList)
            differentdir = get_move(matrice)
            print(self.__hash__(matrice))
            print(differentdir)
            #modif sah
            for direct in differentdir:
                u[0] += direct[1]
                u[1] += direct[0]
                vcout = u[2]
                vheuristique = u[3]
                v = [u[1], u[0], vcout, vheuristique]
                for elem in openList:
                    #FOR ET IF SONT PAS BON
                    #v est un etat 
                    if not(v in closedList and (v in openList and self.compare2Noeuds(v[3], elem[3]) != -1)):
                        vcout = u[2] +1 
                        vheuristique = vcout + abs(objectif[1] - matrice.pos_player[1]) + abs(objectif[0] - matrice.pos_player[0])
                openList.append([u[1],u[0], vcout, vheuristique])
            matrice.pos_player[0] = u[0]
            matrice.pos_player[1] = u[1]
            compteur += 1
            closedList.append(u)
        return closedList
    
    def __hash__(self, matrice):
        return str(matrice.grille).__hash__()

def inverse(liste):
    reverse = []
    compteur = 1
    for elem in liste:
        reverse.append(liste[-compteur])
        compteur += 1
    return reverse

def get_move(matrice):
    possibility = []
    liste = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for direc in liste:
        possible = test_move(matrice, direc)
        if possible != None:
            possibility.append(possible)
    return possibility

def test_move(matrice, coord):
    print(matrice.grille)
    compar = [0, 0]
    compar[0] = matrice.pos_player[0] + coord[0]
    compar[1] = matrice.pos_player[1] + coord[1]
    #verifier si il n'y a pas de mur
    if matrice.grille[compar[0]][compar[1]] != '#':
        #verifie si il y a une caisse devant
        if matrice.grille[compar[0]][compar[1]] == '$':
            #verifie si devant la caisse il n'y a pas d'élément solid
            if matrice.grille[compar[0] + coord[0]][compar[1] + coord[1]] != '#':
                if matrice.grille[compar[0] + coord[0]][compar[1] + coord[1]] != '$':
                    #recherche de la caisse
                    return coord
                else:
                    return
            else:
                return
        #deplacement du personnage et  stockage de sa position précédente pour refaire la matrice
        return coord

#pour moi il faut éxécuté A* une fois pour le personnage aille jusqu'a la caisse puis une deuxieme fois pour qu'il amene la caisse a la case
