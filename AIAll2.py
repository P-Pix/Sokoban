# nouveau style de noeud

from matrix import Matrice
from chose_levels import Chose_level
import heapq as hq
import copy

"""
    pour un simple test, voir les lignes 151,166,185 (saisies manuelles)
    (petit) bug en attente: (heuristique + coût) donne un écart de quelques unités en + ???
"""


# stratégie ? pour éviter les couloirs

''' début du programme .... à transférer en mode graphique '''

# utilitaires .....


#plateau de jeu
def extract(grille): # vers un plateau 
    res=[]
    haut=0

    grille[haut]
    while grille[haut]:
        res.append(grille[haut])
        haut+=1
        
    return res

def aff_plateau(grille):
    for ligne in grille:
        print(" ".join([str(val) for val in ligne]))

# Noeud // modif depuis w3.py
class Noeud():
    def __init__(self,player,caisses,balises):
        self.player=player
        self.caisses=caisses
        self.balises=balises
        # cout et heurist ne sont pas stockés ici

    def visu(self,entete=''):
        pass
        #print(f' --Noeud-- {entete}')
        #print(f' player  {self.player} :')
        #print(f' caisses {self.caisses} ')
        #print(f' balises {self.balises} ')

    def test_arret(self):
#        message(f' Arrêt ? -- toutes les classes sont-elles placées ? {x}')
        for x in self.caisses:
            if not x in self.balises:
                return False
        return True
    
    def  nbplacees(self):
        k=0
        for x in self.caisses:
            if x in self.balises:
                k+=1
        return k

    def egal(self,autre): # compare les champs de 2 noeuds
        if not self.player==autre.player:
            return False

        self.caisses.sort()
        autre.caisses.sort()
        if not self.caisses==autre.caisses:
           return False

        self.balises.sort()
        autre.balises.sort()
        if not self.balises==autre.balises:
           return False

        return True

    def present(self,Liste): # teste la presence d'un noeud dans une liste de noeuds (Closelist)
         for x in Liste:
            if self.egal(x):
               return True
         return False

        
#Heap -- affichages
def visuHeap(hq, entete=''):
     print(f' --Heap-- {entete}')
     #for (h,cpt,n,p) in hq:
         #print(f' {n.player}: h={h} compt={cpt} \n \t caisses {n.caisses} \n \t balises {n.balises} \n \t{p}')

#deplacements potentiels
class Dep:
   def __init__(self, direct, dl, dc): # nom de la direction (points cardinaux), dep lig, dep col
      self.direct=direct
      self.dl=dl
      self.dc=dc

   def visu(self, entete=''):
       pass
      #print(f'(  -- mouvement envisagé -- :  {self.direct})')

class Player():
    def __init__(self,y,x):
        self.y=y
        self.x=x
      
    def visu(self, entete=''):
        print(f' lig={self.x} col={self.y}')
      
    def test_vide(self,plateau):
        message(f' test_vide({self.x} {self.y}')
        return plateau[self.x][self.y]=='0'

# heuristique ?
def dMana(P1,P2):
        return abs(P1[0]-P2[0]) + abs(P1[1]-P2[1])

def heur(N1): # 1 noeud

        #print(f' ? heuristique ')
        N1.visu()
        
        res=0
        for n1 in N1.caisses:
                res+=dMana(N1.player,n1)
                for n2 in N1.balises:
                        res+=dMana(n1,n2)
 
        #print(f' res = {res}')
       
        return res



# tests de présence...
def test_mur(player,plateau):
   return plateau[player.x][player.y]=='#'
      
def test_caisse(player,plateau,caisses):
   #message(f' test_caisse({player.x} {player.y} {caisses}')
   return [player.x,player.y] in caisses

      
# affichages divers
def message(m):
   print(f' !! {m}')

def visuClosedList(L,message=''):
   print(f'  -- Visu closedList -- {message}')
   [print(f' {ligne.player} {ligne.caisses} {ligne.balises} ') for ligne in L]
   

class ExeAI():

    def update(self, matrice):

        # extraction de la matrice à partir du fichier source

        message("initialisation")
        plateau=extract(matrice.level.mape)
        aff_plateau(plateau)

        closedList=[]   #global -- états(=noeud) déja visités [Player,Caisses,Balises]
        heurist=0       #local  -- recalculé à chaque fois (présent dans le heap
        compteur=0      #global -- incrémental, pour différencier ds le Heap
        cout=0          #local  -- utilisé ds le heap , calculé à partir du parcours
        parcours=[]     #local  -- suite des deplacements, (présent ds le heapsort

        testPlayer=matrice.pos_player # <------ choix manuel de la case de début
        noeudInitial=Noeud(testPlayer,         # matrice.level.player,
                            matrice.caisses,
                            matrice.balise)
        #noeudInitial.visu('initial')

        openList=[]     #global -- noeud  restant à visiter
        hq.heappush(openList, (cout+heurist,compteur,noeudInitial, parcours))
        #visuHeap(openList)

        #creation des déplacements ponctuels de player Nord Est Sud West
        depN=Dep('n',0,-1)
        depE=Dep('e',1,0)
        depS=Dep('s',0,1)
        depW=Dep('w',-1,0)
        Ldep=[depN,depE,depS,depW]
        
        

        k=0 # <------ choix manuel du nombre de noeuds traités (pour les tests)
        (_,_,noeud,parcours)=hq.heappop(openList)
        nParcours = []
        #message(f"   {kessais} boucles pour essayer !)")
        while not noeud.test_arret():
        #for k in range(0,kessais):
            k += 1
            #message(f' =============== boucle no {k} ==========================')
            if k != 1:
                (_,_,noeud,parcours)=hq.heappop(openList)
            elif k >= 5000:
                #print("soit le calcul trop long soit le jeu est interminable")
                return []
            #noeud.visu("  == pop ==")
            #visuHeap(openList)
            
            ## test d'arret à faire
            """
            message(f'Solution trouvée?')
            if noeud.test_arret():

                message(f' OUF -- TERMINE avec SUCCES') # pas courant comme message !
                return nParcours
                # return à ajouter qd ce sera installé dans une fonction
            else:
                message(f' non,... on continue')
            """

            closedList.append(noeud)
            #visuClosedList(closedList)

            
            for dep in Ldep:
                #dep.visu()
                Nplayer=Player(noeud.player[1]+dep.dl,noeud.player[0]+dep.dc)
                #Nplayer.visu()
                
                # tests visuels
                test_plateau=copy.deepcopy(plateau)
                test_plateau[Nplayer.x][Nplayer.y]=dep.direct
                #aff_plateau(test_plateau)

                #tests de possibilités...

                if test_mur(Nplayer,plateau):
                    pass
                    #message(f'[{Nplayer.x,Nplayer.y}] **BING** sur le mur')
                    
                elif test_caisse(Nplayer,plateau,noeud.caisses):
                    #message(f' [{Nplayer.x,Nplayer.y}] **BOUM** la tete dans la Caisse')
                    # de la place au delà ?
                    derrP=Player(Nplayer.y+dep.dl,Nplayer.x+dep.dc)
                    #message(f' derriere ? {derrP.x} {derrP.y}')
                    if not test_caisse(derrP,plateau,noeud.caisses):
                        #message(f' une place est disponible --> ON POUSSE !')
                        # on modifie la place de la caisse "dans caisses"
                    
                        nouvNoeud=copy.deepcopy(noeud)
                        nouvNoeud.player=[Nplayer.x,Nplayer.y]
                        nouvNoeud.caisses.remove([Nplayer.x,Nplayer.y])
                        nouvNoeud.caisses.append([derrP.x,derrP.y])
                        #nouvNoeud.visu('nouveau noeud créé')

                        
                        nParcours=parcours.copy()
                        nParcours.append(dep.direct.upper()) # deplacement "qui pousse"
                        cout=len(nParcours)
                        heurist=heur(nouvNoeud)
                        compteur+=1

                        # ajout dans le heap
                        if not nouvNoeud.present(closedList): # attention BUG ?? --corrigé
                            hq.heappush(openList, (cout+heurist,compteur,nouvNoeud, nParcours))
                        #visuHeap(openList)             
                        
                else: # la case est vide: on y place le player
                        nouvNoeud=copy.deepcopy(noeud)
                        nouvNoeud.player=[Nplayer.x,Nplayer.y]
                        #nouvNoeud.visu('nouveau noeud créé')

                        nParcours=parcours.copy()
                        nParcours.append(dep.direct) # direction (minuscule)
                        cout=len(nParcours)
                        heurist=heur(nouvNoeud)
                        compteur+=1

                        # ajout dans le heap
                        if not nouvNoeud.present(closedList): # attention BUG ?? --corrigé
                            hq.heappush(openList, (cout+heurist,compteur,nouvNoeud, nParcours))
                        #visuHeap(openList)
        #message(f' =================FIN DE BOUCLE========================')

        #visuClosedList(closedList)
        #visuHeap(openList)
        #message(f'     {noeud.nbplacees()}  caisses sont placées !')
        #noeud.visu()
        #message(f' OUF -- TERMINE avec SUCCES') # pas courant comme message !
        return nParcours