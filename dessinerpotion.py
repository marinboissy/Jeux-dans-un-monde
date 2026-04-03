import pygame
class Potion:
    def __init__(self,ecran):
        self.ecran = ecran
        self.image =  pygame.image.load("pixil-frame-0 (20).png")
    def potion(self, x, y, zoom):
        n = 0
        if not( 20 >= (11200 - x) * zoom  or (11200 -60 -x) * zoom > 1900):
            image = pygame.transform.scale_by(self.image, zoom)
            self.ecran.blit(image, ((11200  - x)*zoom, (y -125 )*zoom))