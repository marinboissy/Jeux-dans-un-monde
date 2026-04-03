import pygame
from dessinersol import Sol
from dessinerfleur import Fleur
from dessiner_perso import Perso
from pick import Pick
from dessinercheckpoint import Check
from dessinerpotion import Potion
from dessinereau import Eau
class Dessiner:
    def __init__(self, zone,mort, ecran,perso,pos_fleur,fleur1,fleur2,fleur3,sapin,checkpoint,zoneeau):
        self.ecran = ecran
        self.sapin = sapin
        self.zoom_avant = 0
        self.sapin_avant = sapin
        
        self.sol = Sol(self.ecran,zone)
        self.fleur = Fleur(ecran, pos_fleur, fleur1, fleur2, fleur3)
        self.des_perso = Perso(ecran,perso)
        self.pick = Pick(ecran,mort)
        self.check = Check(checkpoint,ecran)
        self.potion = Potion(ecran)
        self.eau = Eau(ecran,zoneeau)
    def dessiner(self, x, y, camerax, cameray, zoom, valide,level_animation):
        xxx = -camerax+ x
        yyy = cameray +y
        if zoom == self.zoom_avant:
            sapin = self.sapin_avant
        else:
            sapin= pygame.transform.scale_by(self.sapin, zoom)
        self.zoom_avant = zoom
        début = (-1000 -x % 800+ camerax)*zoom 
        fin = 2000
        pas = 800*zoom
        b = (cameray - (- y+ 1000) )*zoom
        
        while début <= fin:
                p =(début, b)
                #self.ecran.blit(sapin, p)
                début += pas
           
        self.check.check(xxx,yyy,zoom,valide)    
        self.pick.pick(xxx,yyy,zoom)   
               
        self.sol.sol(xxx, yyy, zoom, camerax)
        self.eau.eau(xxx, yyy,zoom)    
        self.des_perso.des_perso(camerax,cameray,zoom)
        if level_animation == 2:
            self.potion.potion(xxx,yyy,zoom)
        self.fleur.fleur(xxx,yyy,zoom)        