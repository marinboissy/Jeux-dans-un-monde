import pygame
class Perso:
    def __init__(self, ecran, perso):
       self.ecran = ecran
       self.perso = perso
    
    def des_perso(self, camerax, cameray, zoom):
        perso= pygame.transform.scale_by(self.perso, zoom)       
        self.ecran.blit(perso, ((camerax)*zoom, (cameray-200)*zoom))
        
        