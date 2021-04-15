# Créé par ronan, le 05/04/2021 en Python 3.7
import heapq

class fileDePriorite():
   #Définie la file de priorité des données des listes utilisés"""
    def  __init__(self):
        self.Heap = []
        self.Count = 0

    def push(self, liste, item, priority):
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

class Noeud():

    def __init__(self, x, y, heuristic):
        self.x = x
        self.y = y
        self.cout = 0
        self.heuristic = heuristic
