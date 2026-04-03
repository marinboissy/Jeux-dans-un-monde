import pygame
class Eau:
    def __init__(self,ecran,zoneeau):
        self.ecran= ecran
        self.zone = zoneeau
        
    def eau(self, x, y,zoom):
        for g, d, h, b in self.zone:
            if not( 20 >= (d - x) * zoom  or (g -x) * zoom > 1900): 
                largeur = (d - g) * zoom
                hauteur = (h - b) * zoom
                pygame.draw.rect(self.ecran, (50, 50, 250), ((g - x)* zoom, (-h +y)*zoom, largeur, hauteur))