#importation des classes fonctions et modules 

import random
from copy import deepcopy
from core import Color
from faronona.faronona_player import FarononaPlayer
from faronona.faronona_rules import FarononaRules
from faronona.faronona_action import FarononaAction
from faronona.faronona_action import FarononaActionType

#Classe principale du jeu
class AI(FarononaPlayer): 

    #nom de l'équipe
    name = "MAGISTER_AI"

    def __init__(self, color):
        super(AI, self).__init__(self.name, color)
        self.position = color.value

    def play(self, state, remain_time):
       
        """ prend le plus possible en prenant en compte remove et approach /si plusieurs possibles departaage par la priorposition/priorités respectés dans la deuxième phase avec fnction de fuite de danger """

        def importanceposition(i):
            
            """fonction qui prend une coordonnée d'intersection i , lui attribue un score en fonction de son importance et retourne ce score"""
            
            #type d'intersection avec coordonnees
            lakaA= [(2,4)]
            lakaB=[(2,2), (2,6)]
            lakaC=[(1, 1), (1, 3), (1, 5), (1, 7), (3, 1), (3, 3), (3, 5), (3, 7)]
            foinaD=[(2, 1), (2, 3), (2, 5), (2, 7)]
            foinaE=[(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6)]
            lohalakaF=[(0, 2), (0, 4), (0, 6), (4, 2), (4, 4), (4, 6)]
            lohalakaG=[(2,0),(2,8)]
            lohafoinaH=[(0, 1), (0, 3), (0, 5), (0, 7), (4, 1), (4, 3), (4, 5), (4, 7)]
            lohafoinaI=[(1, 0), (1, 8), (3, 0), (3, 8)]
            sommet= [(0, 0), (0, 8), (4, 0), (4, 8)]
            
            #initialisation de la variable d'importance
            Danger=0
            
            #attribution d'un score à chaque intersection
            if i in lakaA:
                Danger=10
            if i in lakaB:
                Danger=9
            if i in lakaC:
                Danger=8    
            if i in foinaD:
                Danger=7
            if i in foinaE:
                Danger=6
            if i in lohalakaF:
                Danger=5
            if i in lohalakaG:
                Danger=4                  
            if i in lohafoinaH:
                Danger=3
            if i in lohafoinaI:
                Danger=2
            if i in sommet:
                Danger=1
            
            #retourne le score d'importance
            return Danger

        def verifierdeplacement (a,b):
            
            """fonction pour identifier deux coordonnees a et b et renvoyer le type et les zones de danger et la priorité du déplacement de a à b"""
           
            
            #première fonction pour identifier la coordonnée et les dangers
            def identifiercoordonneesetdanger(i):
            
                """fonction qui prend une coordonnée i l'identifie détermine les zonnes dangereuses satellites et renvoie le type de coordonnée et les zones dangereuses"""

                #type d'intersection avec coordonnees 
                lakaA= [(2,4)]
                lakaB=[(2,2), (2,6)]
                lakaC=[(1, 1), (1, 3), (1, 5), (1, 7), (3, 1), (3, 3), (3, 5), (3, 7)]
                foinaD=[(2, 1), (2, 3), (2, 5), (2, 7)]
                foinaE=[(1, 2), (1, 4), (1, 6), (3, 2), (3, 4), (3, 6)]
                lohalakaF=[(0, 2), (0, 4), (0, 6), (4, 2), (4, 4), (4, 6)]
                lohalakaG=[(2,0),(2,8)]
                lohafoinaH=[(0, 1), (0, 3), (0, 5), (0, 7), (4, 1), (4, 3), (4, 5), (4, 7)]
                lohafoinaI=[(1, 0), (1, 8), (3, 0), (3, 8)]
                sommet= [(0, 0), (0, 8), (4, 0), (4, 8)]
                
                #initialisation des variables
                Identification='aucun'
                Danger=[]
                a,b=i

                # Le coeur de la fonction Identification de chaue position avec détermiation des zones de danger
                if i in lakaA:
                    Identification='lakaA'
        
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ((j==0 and k%2==0 and k!=b+1 and k!= b-1 )or (j==4 and k%2==0 and k!=b+1 and k!= b-1 ) or (k==0 and j!=a+1 and j!= a-1 and j%2==0 ) or (k==8 and j%2==0 and j!=a+1 and j!= a-1 ) ) or((j<4 and j>0 and k<8 and k>0) and ((j!=a and j%2==k%2) or (j==a and k!=b)or (j!=a and k==b))):
                                Danger.append((j,k))    
    
                if i in lakaB:
                    Identification='lakaB'
                    
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ((j==0 and k%2==0 and k!=b+1 and k!= b-1 )or (j==4 and k%2==0 and k!=b+1 and k!= b-1 ) or (k==0 and j!=a+1 and j!= a-1 and j%2==0 ) or (k==8 and j%2==0 and j!=a+1 and j!= a-1 ) ) or((j<4 and j>0 and k<8 and k>0) and ((j!=a and j%2==k%2) or (j==a and k!=b)or (j!=a and k==b))):
                                Danger.append((j,k))

                if i in lakaC:
                    Identification='lakaC'
                   
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ((j==0 and k%2==0 and k!=b+1 and k!= b-1 )or (j==4 and k%2==0 and k!=b+1 and k!= b-1 ) or (k==0 and j!=a+1 and j!= a-1 and j%2==0 ) or (k==8 and j%2==0 and j!=a+1 and j!= a-1 ) ) or((j<4 and j>0 and k<8 and k>0) and ((j!=a and j%2==k%2) or (j==a and k!=b)or (j!=a and k==b))):
                                Danger.append((j,k))

                if i in foinaD:
                    Identification='foinaD'
                    
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ( (j<4 and j>0 and k<8 and k>0 or ((j==0 and j!= a-1 )or (j==4 and j!=a+1  ) or (k==0 and k!=b-1   ) or (k==8  and k!=b+1 ) )) and (j==a or k==b) and ((j==a and k!=b)or (j!=a and k==b))  ):
                                Danger.append((j,k))

                if i in foinaE:
                    Identification='foinaE'
                    
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ( (j<4 and j>0 and k<8 and k>0 or ((j==0 and j!= a-1 )or (j==4 and j!=a+1  ) or (k==0 and k!=b-1   ) or (k==8  and k!=b+1 ) )) and (j==a or k==b) and ((j==a and k!=b)or (j!=a and k==b))  ):
                                Danger.append((j,k))

                if i in lohalakaF:
                    Identification='lohalakaF'
                    
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ((j<=4 and j>=0 and k<=8 and k>=0 and (j,k)!=(a,b)) and ((j==0 and k%2==0 and k!=b+1 and k!= b-1 )or (j==4 and k%2==0 and k!=b+1 and k!= b-1 ) or (k==0 and j!=a+1 and j!= a-1 and j%2==0 ) or (k==8 and j%2==0 and j!=a+1 and j!= a-1 ) ) or((j<4 and j>0 and k<8 and k>0) and ((j!=a and j%2==k%2) or (j==a and k!=b)or (j!=a and k==b)) or (j==a and k!=b))):
                                Danger.append((j,k))

                if i in lohalakaG:
                    Identification='lohalakaG'
                    
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ((j<=4 and j>=0 and k<=8 and k>=0 and (j,k)!=(a,b)) and ((j==0 and k%2==0 and k!=b+1 and k!= b-1 )or (j==4 and k%2==0 and k!=b+1 and k!= b-1 ) or (k==0 and j!=a+1 and j!= a-1 and j%2==0 ) or (k==8 and j%2==0 and j!=a+1 and j!= a-1 ) ) or((j<4 and j>0 and k<8 and k>0) and ((j!=a and j%2==k%2) or (j==a and k!=b)or (j!=a and k==b)) or (j!=a and k==b))):
                                Danger.append((j,k))

                if i in lohafoinaH:
                    Identification='lohafoinaH'
                   
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if (( j<=4 and j>=0 and k<8 and k>0) and ( (j<4 and j>0 and k<8 and k>0 or ((j==0 and j!= a-1 )or (j==4 and j!=a+1  ) or (k==0 and k!=b-1   ) or (k==8  and k!=b+1 ) )) and (j==a or k==b) and ((j==a and k!=b)or (j!=a and k==b))  )):
                                Danger.append((j,k))

                if i in lohafoinaI:
                    Identification='lohafoinaI'
                   
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if (( j<4 and j>0 and k<=8 and k>=0) and ( (j<4 and j>0 and k<8 and k>0 or ((j==0 and j!= a-1 )or (j==4 and j!=a+1  ) or (k==0 and k!=b-1   ) or (k==8  and k!=b+1 ) )) and (j==a or k==b) and ((j==a and k!=b)or (j!=a and k==b))  )):
                                Danger.append((j,k))

                if i in sommet:
                    Identification='sommet'
                   
                    for j in range (a-2, a+3 ):
                        for k in range (b-2, b+3 ):
                            if ((((j<=4 and j>=0 and k<=8 and k>=0 and (j,k)!=(a,b))) and (((j==0 and k%2==0 and k!=b+1 and k!= b-1 )or (j==4 and k%2==0 and k!=b+1 and k!= b-1 ) or (k==0 and j!=a+1 and j!= a-1 and j%2==0 ) or (k==8 and j%2==0 and j!=a+1 and j!= a-1 ) ) or((j<4 and j>0 and k<8 and k>0) and ((j!=a and j%2==k%2) or (j==a and k!=b)or (j!=a and k==b)) or (j==a and k!=b) or (j!=a and k==b))))):
                                Danger.append((j,k))

                #retourne l'identification ainsi que les zones de danger
                return [Identification,Danger]

            #initialisation et identification des coordonnées et des zonnes de danger de a et b
            priorite=0
            identificationA=identifiercoordonneesetdanger(a)[0]
            identificationsB=identifiercoordonneesetdanger(b)
            identificationB=identificationsB[0]
            Danger=identificationsB[1]
            
            #coeur de la fonction, identification du niveau de priorité du déplacement
            if identificationB=='lakaA':
                
                if identificationA=='foinaE':
                    priorite=1
                if identificationA=='foinaD':
                    priorite=2
                if identificationA=='lakaC':
                    priorite=3
                           
            if identificationB=='lakaB':
                
                if identificationA=='foinaE':
                    priorite=4
                if identificationA=='foinaD':
                    priorite=5
                if identificationA=='lakaC':
                    priorite=6
                
            if identificationB=='lakaC':

                if identificationA=='sommet':
                    priorite=7
                if identificationA=='lohafoinaI':
                    priorite=8
                if identificationA=='lohafoinaH':
                    priorite=9
                if identificationA=='lohalakaG':
                    priorite=10
                if identificationA=='lohalakaF':
                    priorite=11
                if identificationA=='foinaE':
                    priorite=12
                if identificationA=='foinaD':
                    priorite=13
                if identificationA=='lakaB':
                    priorite=16
                if identificationA=='lakaA':
                    priorite=17

            if identificationB=='foinaD':

                if identificationA=='lohalakaG':
                    priorite=14
                if identificationA=='lakaC':
                    priorite=18
                if identificationA=='lakaB':
                    priorite=19
                if identificationA=='lakaA':
                    priorite=20
                
            if identificationB=='foinaE':

                if identificationA=='lohalakaF':
                    priorite=15
                if identificationA=='lakaC':
                    priorite=21
                if identificationA=='lakaB':
                    priorite=22
                if identificationA=='lakaA':
                    priorite=23

            if identificationB=='lohalakaF':

                if identificationA=='lohafoinaH':
                    priorite=24
                if identificationA=='foinaE':
                    priorite=31
                if identificationA=='lakaC':
                    priorite=32
                                
            if identificationB=='lohalakaG':

                if identificationA=='lohafoinaI':
                    priorite=25
                if identificationA=='foinaD':
                    priorite=33
                if identificationA=='lakaC':
                    priorite=34
                
            if identificationB=='lohafoinaH':

                if identificationA=='sommet':
                    priorite=26
                if identificationA=='lohalakaF':
                    priorite=30
                if identificationA=='lakaC':
                    priorite=35
                
            if identificationB=='lohafoinaI':

                if identificationA=='sommet':
                    priorite=27
                if identificationA=='lohalakaG':
                    priorite=31
                if identificationA=='lakaC':
                    priorite=36
                
            if identificationB=='sommet':
                
                if identificationA=='lohafoinaI':
                    priorite=28
                if identificationA=='lohafoinaH':
                    priorite=29
                if identificationA=='lakaC':
                    priorite=37
            
                
            #retourne une liste contenant la priorité et les danger de a,b
            return [priorite,Danger]
            
        def meilleurprise(State,d,player):
            
            ''' prends un state , un mouvement et un joueur. retourne la ou les   prises possibles pour ce mouvvement et le nombre de pion prenable '''
            
            STATE= deepcopy(State)
            choix =0
            at,to=d
            recapitulatif=[]
            winpar=''
            
            #si prise par approach possible
            if  FarononaRules.is_win_approach_move(at,to,STATE,player) is not None and len(FarononaRules.is_win_approach_move(at,to,STATE,player))> 0:
                choix= len(FarononaRules.is_win_approach_move(at,to,STATE,player))
                winpar='APPROACH'
                recapitulatif.append([choix,winpar])
            
            #si prise par remote possible    
            if  FarononaRules.is_win_remote_move(at,to,STATE,player) is not None and len(FarononaRules.is_win_remote_move(at,to,STATE,player))> 0:
                choix= len(FarononaRules.is_win_remote_move(at, to, state, player))
                winpar='REMOTE'
                recapitulatif.append([choix,winpar])
            
            #retourne les prises possibles ainsi les modes
            return recapitulatif

        def creerstate(State,mouvement,joueur):
            
            '''prends un state un fanoraaction et un joueur et retourne un nouveau state virtuel'''

            STATE=deepcopy(State)
            Nouveaustate =FarononaRules.make_move(STATE,mouvement,joueur) 
            return Nouveaustate[0]
        
        def creerstate2(State,mouvement,joueur):
            
            '''prends un state un mouvement et un joueur et retourne un nouveau state virtuel'''
            
            STATE=deepcopy(State)
            actionenvoyee=FarononaAction(action_type=FarononaActionType.MOVE, win_by='REMOTE', at=mouvement[0], to=mouvement[1])
            Nouveaustate =FarononaRules.make_move(STATE,actionenvoyee,joueur) 
            return Nouveaustate[0]

        def meilleurcoupsuccesif( State,mouvement,joueur):
            
            ''' fonction qui prend en argument  un state un muvement et un joueur , et renvoie le meilleur chemin de prises possibles maximal en effectuant des coups successifs '''
            
            at, to= mouvement
            #création d'une copie du state pour ne pas modifier l'originale et initialisation des variables 
            STATE0=deepcopy(State)
            cheminmeilleurprise=[at] 
            meilleurprisei0=0
            meilleurpriseT=0
            meilleurpriseG=0
            meilleurprise0=0
            meilleurprise1=0
            meilleurprise2=0
            meilleurprise3=0
            meilleurprise4=0
            meilleurprise5=0
            meilleurprise6=0
            meilleurprise7=0
            meilleurprise8=0
            

            for i0 in meilleurprise(STATE0,(at,to),joueur):
                
                meilleurprisei0=i0[0]
                actionenvoyee=FarononaAction(action_type=FarononaActionType.MOVE, win_by=i0[1], at=at, to=to)
                STATE=creerstate(STATE0,actionenvoyee,joueur)
                mouvementpossible0=FarononaRules.get_effective_cell_moves(STATE,to)
                meilleurpriseG=(meilleurprisei0)
        
                if meilleurpriseT<meilleurpriseG:

                    meilleurpriseT=meilleurpriseG
                    cheminmeilleurprise=[at,to]
                    winparinit=i0[1]
            
                if len(mouvementpossible0)>0  :
                    for z in mouvementpossible0: 

                        if z not in cheminmeilleurprise and z != to:
                            for ii in meilleurprise(STATE,(to,z),joueur):
                                meilleurprise0=ii[0]
                                actionenvoyee=FarononaAction(action_type=FarononaActionType.MOVE, win_by=ii[1], at=to, to=z)
                                STATE1=creerstate(STATE,actionenvoyee,joueur)
                                mouvementpossible01=FarononaRules.get_effective_cell_moves(STATE1,z)
                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)
        
                                if meilleurpriseT<meilleurpriseG:
                                    meilleurpriseT=meilleurpriseG
                                    cheminmeilleurprise=[at,to,z]
                                    winparinit=i0[1]
                
                                if len(mouvementpossible01) >0 and meilleurprise0>0:
                                    for y in mouvementpossible01:
                                        if y not in cheminmeilleurprise and y != to:
                                            for iii in meilleurprise(STATE1,(z,y),joueur):
                                                meilleurprise1=iii[0]
                                                actionenvoyee=FarononaAction( action_type=FarononaActionType.MOVE, win_by=iii[1], at=z, to=y)
                                                STATE2=creerstate(STATE1,actionenvoyee,joueur)
                                                mouvementpossible02=FarononaRules.get_effective_cell_moves(STATE2,y)
                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)
                            
                                                if meilleurpriseT<meilleurpriseG:
                                                    meilleurpriseT=meilleurpriseG
                                                    cheminmeilleurprise=[at,to,z,y]
                                                    winparinit=i0[1]
                        
                                                if len(mouvementpossible02)>0 and meilleurprise1>0:
                                                    for u in mouvementpossible02:
                                                        if u not in cheminmeilleurprise and u!= to:
                                                            for iiii in meilleurprise(STATE2,(y,u),joueur):
                                                                meilleurprise2=iiii[0]
                                                                actionenvoyee=FarononaAction( action_type=FarononaActionType.MOVE, win_by=iiii[1], at=y, to=u)
                                                                STATE3=creerstate(STATE2,actionenvoyee,joueur)
                                                                mouvementpossible03=FarononaRules.get_effective_cell_moves(STATE3,u)
                                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)+(meilleurprise2)
                                    
                                                                if meilleurpriseT<meilleurpriseG:
                                                                    meilleurpriseT=meilleurpriseG
                                                                    cheminmeilleurprise=[at,to,z,y,u]
                                                                    winparinit=i0[1]
                        
                                                                if len(mouvementpossible03) >0 and meilleurprise2>0:
                                                                    for t in mouvementpossible03:
                                                                        if t not in cheminmeilleurprise and t!= to:
                                                                            for i2 in meilleurprise(STATE3,(u,t),joueur):
                                                                                meilleurprise3=i2[0]
                                                                                actionenvoyee=FarononaAction( action_type=FarononaActionType.MOVE, win_by=i2[1], at=u, to=t)
                                                                                STATE4=creerstate(STATE3,actionenvoyee,joueur)
                                                                                mouvementpossible04=FarononaRules.get_effective_cell_moves(STATE4,t)
                                                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)+(meilleurprise2)+(meilleurprise3)
                                            
                                                                                if meilleurpriseT<meilleurpriseG:
                                                                                    meilleurpriseT=meilleurpriseG
                                                                                    cheminmeilleurprise=[at,to,z,y,u,t]
                                                                                    winparinit=i0[1]
                                            
                            
                                                                                if len(mouvementpossible04)>0 and meilleurprise3>0:
                                                                                    for s in mouvementpossible04:
                                                                                        if s not in cheminmeilleurprise and s!= to:
                                                                                            for i3 in meilleurprise(STATE4,(t,s),joueur):
                                                                                                meilleurprise4=i3[0]
                                                                                                actionenvoyee=FarononaAction( action_type=FarononaActionType.MOVE, win_by=i3[1], at=t, to=s)
                                                                                                STATE5=creerstate(STATE4,actionenvoyee,joueur)

                                                                                                mouvementpossible05=FarononaRules.get_effective_cell_moves(STATE5,s)
                                                                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)+(meilleurprise2)+(meilleurprise3)+(meilleurprise4)

                                                                                                if meilleurpriseT<meilleurpriseG:
                                                                                                    meilleurpriseT=meilleurpriseG
                                                                                                    cheminmeilleurprise=[at,to,z,y,u,t,s]
                                                                                                    winparinit=i0[1]

                                                                                                if len(mouvementpossible05)>0 and meilleurprise4>0:
                                                                                                    for r in mouvementpossible05:
                                                                                                        if r not in cheminmeilleurprise and r!= to:
                                                                                                            for i4 in meilleurprise(STATE5,(s,r),joueur):
                                                                                                                meilleurprise5=i4[0]
                                                                                                                actionenvoyee=FarononaAction( action_type=FarononaActionType.MOVE, win_by=i4[1], at=s, to=r)

                                                                                                                STATE6=creerstate(STATE5,actionenvoyee,joueur)
                                                                                                                mouvementpossible06=FarononaRules.get_effective_cell_moves(STATE6,r)
                                                                                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)+(meilleurprise2)+(meilleurprise3)+(meilleurprise4)+(meilleurprise5)
                                                            
                                                                                                                if meilleurpriseT<meilleurpriseG:
                                                                                                                    meilleurpriseT=meilleurpriseG
                                                                                                                    cheminmeilleurprise=[at,to,z,y,u,t,s,r]
                                                                                                                    winparinit=i0[1]
                                                            
                                                                                                                if len(mouvementpossible06)>0  and meilleurprise5>0:
                                                                                                                    for q in mouvementpossible06:
                                                                                                                        if  q not in cheminmeilleurprise and q!= to:
                                                                                                                            for i5 in meilleurprise(STATE6,(r,q),joueur):
                                                                                                                                meilleurprise6=i5[0]
                                                                                                                                actionenvoyee=FarononaAction( action_type=FarononaActionType.MOVE, win_by=i5[1], at=r, to=q)
                                                                                                                                STATE7=creerstate(STATE6,actionenvoyee,joueur)
                                                                                                                                mouvementpossible07=FarononaRules.get_effective_cell_moves(STATE7,q)
                                                                                                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)+(meilleurprise2)+(meilleurprise3)+(meilleurprise4)+(meilleurprise5)+(meilleurprise6)

                                                                                                                                if meilleurpriseT<meilleurpriseG:
                                                                                                                                    meilleurpriseT=meilleurpriseG
                                                                                                                                    cheminmeilleurprise=[at,to,z,y,u,t,s,r,q]
                                                                                                                                    winparinit=i0[1]

                                                                                                                                if len(mouvementpossible07)>0 and meilleurprise6>0:
                                                                                                                                    for p in mouvementpossible07:
                                                                                                                                        if p not in cheminmeilleurprise and p!= to:
                                                                                                                                            for i6 in meilleurprise(STATE7,(q,p),joueur):
                                                                                                                                                meilleurprise7=i6[0]
                                                                                                                                                actionenvoyee=FarononaAction( action_type=FarononaActionType.MOVE, win_by=i6[1], at=q, to=p)
                                                                                                                                                STATE8=creerstate(STATE7,actionenvoyee,joueur)
                                                                                                                                                mouvementpossible08=FarononaRules.get_effective_cell_moves(STATE8,p)
                                                                                                                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)+(meilleurprise2)+(meilleurprise3)+(meilleurprise4)+(meilleurprise5)+(meilleurprise6)+(meilleurprise7)

                                                                                                                                                if meilleurpriseT<meilleurpriseG:
                                                                                                                                                    meilleurpriseT=meilleurpriseG
                                                                                                                                                    cheminmeilleurprise=[at,to,z,y,u,t,s,r,q,p]
                                                                                                                                                    winparinit=i0[1]
                                                                            
                                                                                                                                                if len(mouvementpossible08)>0 and meilleurprise7>0:
                                                                                                                                                    for o in mouvementpossible08:
                                                                                                                                                        if o not in cheminmeilleurprise and o!= to:
                                                                                                                                                            for i7 in meilleurprise(STATE8,(p,o),joueur):
                                                                                                                                                                meilleurprise8=i7[0]
                                                                                                                                                                
                                                                                                                                                                meilleurpriseG=(meilleurprisei0)+(meilleurprise0)+(meilleurprise1)+(meilleurprise2)+(meilleurprise3)+(meilleurprise4)+(meilleurprise5)+(meilleurprise6)+(meilleurprise7)+(meilleurprise8)
                                                                                    
                                                                                                                                                                if meilleurpriseT<meilleurpriseG:
                                                                                                                                                                    meilleurpriseT=meilleurpriseG
                                                                                                                                                                    cheminmeilleurprise=[at,to,z,y,u,t,s,r,q,p,o]
                                                                                                                                                                    winparinit=i0[1]
                 
            return [cheminmeilleurprise,meilleurpriseT,winparinit]

        #récupére l'enplacement des pièces de l'adversaire
        board = state.get_board()
        latestplayer= state.get_next_player()*-1
        opponent_pieces = board.get_player_pieces_on_board(Color(latestplayer))
        
        #initialisation des variables à utiliser avant d'entrer dzns la boucle
        x=0
        PrioriteG=500
        choix=0
        choixarrivee=0

        #affiche le nombre d'actions  possibles ainsi que leur liste ensuite les mélange de faco aléatoire
        touslescoups=sorted(FarononaRules.get_player_actions(state, self.position),key=lambda k: random.random())
        
        #boucle pour vérifier chaque coup et faire le meilleur choix le coeur de la fonction play
        while x < len(touslescoups) :

            #Jouer ce coup sans réflexion si on est le premier joueur
            if state.get_latest_player() is None:
                action = FarononaAction(action_type=FarononaActionType.MOVE, win_by='APPROACH', at=(1,5), to=(2,4))
                break
            
            #recupere les positions de départ et d'arrivée de l'action à vérifier
            actionDict = touslescoups [x-1].get_action_as_dict()
            at=actionDict['action']['at']
            to =actionDict['action']['to']   
                   
            #Algorithme si des prises sont possibles , prendre le plus possible
            if ((FarononaRules.is_win_approach_move(at, to, state, self.position) is not None and len(FarononaRules.is_win_approach_move(at, to, state, self.position)) != 0) or (FarononaRules.is_win_remote_move(at, to, state, self.position) is not None and len(FarononaRules.is_win_remote_move(at, to, state, self.position)) != 0)): 

                #récupère à partir de la position d'arrivée le plus grand nombre de prise successif possible et le chemin pour y arriver
                prisetotalepossiblecoupetchemin = meilleurcoupsuccesif(state,(at,to),self.position)
                
                #nombre totale de prise à espérer avec ce déplacement
                prisetotalepossible=prisetotalepossiblecoupetchemin[1]

                #qualité de la position d'arrivée
                arrivee=importanceposition(prisetotalepossiblecoupetchemin[0][-1])
                                    
                #si le nombre de prise maximale possible supérieur aux précédents
                if prisetotalepossible> choix:
                    
                    #le retenir et le mettre comme nouveau standard
                    atdefinitive= at
                    todefinitive= to
                    winbydefinitive=prisetotalepossiblecoupetchemin[2]
                    choix= prisetotalepossible
                    choixarrivee=arrivee

                if prisetotalepossible == choix and at!=atdefinitive:
                    
                    #départage par la qualité de la position d'arrivée
                    
                    #si la case d'arrivée a une meilleur priorité
                    if arrivee>choixarrivee:

                        #le retenir et le mettre comme nouveau standard
                        atdefinitive= at
                        todefinitive= to
                        winbydefinitive=prisetotalepossiblecoupetchemin[2]
                        choix= prisetotalepossible
                        choixarrivee=arrivee
                    
            #Algorithme Si aucune prise n'est possible
            if (choix==0 ):
                
                #initialisation variable de tests
                mauvais=0
                endanger=0
                tueur=0
                winbydefinitive='APPROACH'
                
                #récupère la priorité du deplacemment et les position dangereuses en rapport
                Verification= verifierdeplacement(at,to)
                Priorite= Verification[0]  
                Danger=Verification[1]        
               
                
                #créer le nouveau state à tester après ce déplacement
                stateapresmouvement=creerstate2(state,(at,to),self.position)
                
                #vérifier si le pion sera en danger après le déplacement
                for o in Danger:
                    if o in opponent_pieces and mauvais==0:
                        mouvementadversaire=FarononaRules.get_effective_cell_moves(stateapresmouvement,o)
                        for s in mouvementadversaire:    
                            #si la piece adverse peut le prendre après le déplacement
                            if mauvais==0 and (FarononaRules.is_win_approach_move(o,s,stateapresmouvement,self.position*-1) is not None and to in FarononaRules.is_win_approach_move(o,s,stateapresmouvement,self.position*-1)) or(FarononaRules.is_win_remote_move(o,s,stateapresmouvement,self.position*-1) is not None and to in FarononaRules.is_win_remote_move(o,s,stateapresmouvement,self.position*-1)):
                                mauvais=1
                
                #vérifier si le pion est en danger 
                if mauvais==0:
                    for a in opponent_pieces:
                        if endanger==0:
                            mouvementadversaire=FarononaRules.get_effective_cell_moves(state,a)
                            for b in mouvementadversaire:
                                #si la piece adverse peut le prendre au prochain tour
                                if endanger==0 and ((FarononaRules.is_win_approach_move(a,b,state,self.position*-1) is not None and at in FarononaRules.is_win_approach_move(a,b,state,self.position*-1)) or(FarononaRules.is_win_remote_move(a,b,state,self.position*-1) is not None and  at in FarononaRules.is_win_remote_move(a,b,state,self.position*-1))):
                                    endanger=1
                
                if mauvais==0 :
                    mespieces=stateapresmouvement.get_board().get_player_pieces_on_board(Color(stateapresmouvement.get_next_player()*-1))
                    for y in mespieces:
                        if tueur==0:
                            mouvementpropre=FarononaRules.get_effective_cell_moves(stateapresmouvement,y)
                            for m in mouvementpropre:    
                            #si  ma piece peut prendre une piece adverse apres après le déplacement
                                if tueur==0 and ((FarononaRules.is_win_approach_move(y,m,stateapresmouvement,self.position) is not None) or(FarononaRules.is_win_remote_move(y,m,stateapresmouvement,self.position) is not None)):  
                                    tueur=1
                
                #si ce mouvement permet de prendre un pion au prochain coup
                if tueur==1:
                    Priorite=Priorite-50

                # Pion en danger Priorité de déplacer le pion s'il est en danger vers un endroit safe       
                if endanger==1:
                    Priorite=Priorite-100
                
                #Pion pas en danger et déplacement dangereux, ne pas toucher au pion
                if mauvais==1:
                    Priorite=Priorite+100

                #retenir le meilleur déplacement par le jeu des priorité
                if Priorite< PrioriteG:
                    atdefinitive= at
                    todefinitive= to
                    PrioriteG=Priorite
            
            #Action choisi par l'algorithme au final
            action = FarononaAction(action_type=FarononaActionType.MOVE, win_by=winbydefinitive, at=atdefinitive, to=todefinitive)
            x+=1

        #retourner l'action finale
        return action 