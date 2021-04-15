""" 
Créé par ronan, le 30/03/2021 en Python 3.7
Lien entre notion état est classe matrice , Methode utilisé déjà présente dans la classe matrice,
Methode action possible dans la classe matrie , Renvoie nouvelle matrice que on pourra traité.
""""

import heapq



def heuristic(posPlayer, posCaisses):
	distance = 0
    complete = []
    for i in range len(matrice.balise):
        autreListe = []
        for x in range len(matrice.caisses):
            balise = matrice.balise[i]
            caisse = matrice.caisses[x]
            ydistance = balise[0] - caisse[0] 
            xdistance = balise[1] - caisse[1]
            totalDistance = xdistance * xdistance + ydistance * ydistance
            totalDistance = sqrt(totalDistance)
            autreListe.append(totalDistance)
        complete.append(autreListe)
    return complete
        	
def breadthFirstSearch(matrice):
    beginBox = matrice.caisses
    beginPlayer = matrice.pos_player
    
    debutEtat = (beginPlayer,beginBox)
    frontiere = posMur(matrice)
    actions = actionPossible(matrice)
    while 

def posCaisses(matrice):
    return matrice.caisses

def posMur(matrice):
  stock = []
  for y in range matrice.grille:
    for x in range y:
      if(x == '#'):
        stock.extend([y, x])
  return stock

def posPlayer(matrice):
    return matrice.pos_player

class fileDePriorite:
   #Définie la file de priorité des données des listes utilisés"""
    def  __init__(self):
        self.Heap = []
        self.Count = 0

    def push(self, item, priority):
        #Ajoute un item dans la queu de priorité"
        entry = (priority, self.Count, item)
        heapq.heappush(self.Heap, entry)
        #Tas, Entry c'est lévenement"
        self.Count += 1

    def pop(self):
        #Retire un item qui est le plus intéressant
        (_, _, item) = heapq.heappop(self.Heap)
        #heapq return 3 valeur, et on utilise que la dernière"
        return item

    def vide(self):
        #queu vide"
        return len(self.Heap) == 0

def astar(matrice):
    closeList = []
    openList = fileDePriorite()
    openList.push(matrice.pos_player)
    while openList != []:
        u = openList.
        if u[1] == matrice.balise[1] and u[0] == matrice.balise[0]:
            



def Cout(actions):
    #Fonction coup d'une action"
    return len([x for x in actions if x.islower()])



def actionPossible(matrice):
    #liste des possibilités de mouvement du personnage#
    return matrice.get_move()

