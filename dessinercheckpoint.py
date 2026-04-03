import pygame
class Check:
    def __init__(self,checkpoint,ecran):
        self.ecran = ecran
        self.checkpoint = checkpoint
        self.passer =  pygame.image.load("pixil-frame-0 (22).png")
        self.encore =  pygame.image.load("pixil-frame-0 (23).png")
    def check(self, x, y, zoom,valide):
        n = 0
        for g, b in self.checkpoint:
            if not( 20 >= (g - x) * zoom  or (g -60 -x) * zoom > 1900):
                if valide >= n:
                    passer = pygame.transform.scale_by(self.passer, zoom)
                    self.ecran.blit(passer, ((g  - x)*zoom, (y - (b + 120) )*zoom))
                else:
                    encore= pygame.transform.scale_by(self.encore, zoom)
                    self.ecran.blit(encore, ((g  - x)*zoom, (y - (b + 120) )*zoom))
            n += 1 