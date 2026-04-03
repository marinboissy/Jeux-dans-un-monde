import pygame
class Fleur:
    def __init__(self, ecran, pos_fleur, fleur1, fleur2, fleur3):
        self.pos_fleur = pos_fleur
        self.fleur1= fleur1
        self.fleur2= fleur2
        self.fleur3= fleur3
        self.ecran = ecran
    
    def fleur(self, x, y, zoom):
        fleur1= pygame.transform.scale_by(self.fleur1, zoom)
        fleur2= pygame.transform.scale_by(self.fleur2, zoom)
        fleur3= pygame.transform.scale_by(self.fleur3, zoom)
        for g, d, b in self.pos_fleur:
            if not( 20 >= (d - x) * zoom  or (g -x) * zoom > 1900):
                n = (d - g)//100
                fleur1= pygame.transform.scale_by(self.fleur1, zoom)
                fleur2= pygame.transform.scale_by(self.fleur2, zoom)
                fleur3= pygame.transform.scale_by(self.fleur3, zoom)
           
                for loop in range(n):
                    aa = ((g + loop*100 - x)*zoom, (y - (b + 60) )*zoom)
                    bb = ((g + loop*100 - x+ 33)*zoom, (y - (b + 60) )*zoom)
                    cc = ((g + loop*100 - x+ 67)*zoom, (y - (b + 60) )*zoom)
                    self.ecran.blit(fleur1, aa)
                    self.ecran.blit(fleur2, bb)
                    self.ecran.blit(fleur3, cc)
        