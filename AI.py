# code de l'ia
import 

class IA:
	
	def __init__(self,Matrice):
		
		self.open = Matrice
		self.mouvement = 0
		self.father = None
		self.Etatfinal = self.correct  #à retravailler !!!
		
	def move (self,coord):
		
		
		while open != None:
			
			
		
# coding: utf8

#Sodoban
# 1- dessin du plateau
# 3- affichage d'un état


# source: etat.py #########################################"

class Etat(object):
    """ les états du graphe """

    #structure des données

    # position du personnage X,Y
    pers=[None, None]
    
    # liste des positions des caisses X,Y, bool: disponible (reste à déplacer)
    # liste de taille variable
    cais=[[None,None, True],
          [None,None, True]]

    # liste des places où ranger les caisses X,Y, bool: disponible (zone vide)
    #  nbre de places >= nbre de caisses ;)
    dest=[[None,None, True],
          [None,None, True]]

    def __init__(self,pers=[1,1],cais=[[2,5,True]],dest=[[5,10,True]]):
        self.pers=pers
        self.cais=cais
        self.dest=dest
        
init=Etat(pers=[3,4],
          cais=[[1,5,True],[2,7,False]],
          dest=[[5,6,True],[2,7,False]])

	

# source: plateau.py #########################################"

class Plateau(object):
    """ support de jeu """

    # caractères utilisables pour chacune des cases
    c_mur='#'
    c_vide='.'
    c_pers='@'
    c_dispo='?'        # disponible pour placer une caisse
    c_caiss='!'
    c_occup='X'        # place occupée par une caisse
    
    def __init__(self,larg=15,haut=12,etat=init):
        self.larg=larg
        self.haut=haut
        
        # modèle de ligne vide et de mur haut & bas
        hb=[] # haut bas
        for i in range(0,larg):
            hb.append(self.c_mur)

        lv=[self.c_mur]
        for i in range(0+1,larg-1):
           lv.append(self.c_vide)
        lv.append(self.c_mur)
        
        # construction du dessin
        self.dessin=[hb[:]]
        for i in range(1,self.haut-1):
            self.dessin.append(lv[:])
        self.dessin.append(hb[:])
        
        # ajout de l'état
        #personnage
        self.dessin[init.pers[0]][init.pers[1]]=self.c_pers

        # caisses
        for x in init.cais:
            if x[2]:
                self.dessin[x[0]][x[1]]=self.c_caiss
            else:
                self.dessin[x[0]][x[1]]=self.c_occup

        # places à utiliser
        for x in init.dest:
            if x[2]:
                self.dessin[x[0]][x[1]]=self.c_dispo
            else:
                self.dessin[x[0]][x[1]]=self.c_occup #redondance!#

       
            
    def dessine(self):
        for i in range(0,self.haut):
            for j in range(0,self.larg):
                print(f"{self.dessin[i][j]} ",end="")
            print()
    
        
if __name__== '__main__' :
    plateau().dessine()

""" exemple d'exécution
# # # # # # # # # # # # # # # 
# . . . . ! . . . . . . . . # 
# . . . . . . X . . . . . . # 
# . . . @ . . . . . . . . . # 
# . . . . . . . . . . . . . # 
# . . . . . ? . . . . . . . # 
# . . . . . . . . . . . . . # 
# . . . . . . . . . . . . . # 
# . . . . . . . . . . . . . # 
# . . . . . . . . . . . . . # 
# . . . . . . . . . . . . . # 
# # # # # # # # # # # # # # # 

"""
#Lien entre notion état est classe matrice , Methode utilisé déjà présente dans la classe matrice, 
#Methode action possible dans la classe matrie , Renvoie nouvelle matrice que on pourra traité.#
def affiche(grille):
	for ligne in grille:
		print("\t".join([str(val) for val in ligne]))
        
class Astar:
	
	
class Etats:

	def receveMap(self, mape):
        pass
	
class Heuristic:
	
	def boxMalPlacer(self,correct):
	
	#nombre de caisse qu'il reste a mettre#
	pass

