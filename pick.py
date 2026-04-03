import pygame
class Pick:
    def __init__(self, ecran,mort):
       self.ecran = ecran
       self.mort= mort
    
    def pick(self, x, y, zoom):
        for g, b, n in self.mort:
            for loop in range(n):
                aa = ((g + loop*100-x)*zoom, (y - b )*zoom)
                bb = ((g + loop*100 + 50-x)*zoom, (y - (b +75 ) )*zoom)
                cc = ((g + loop*100 +100-x)*zoom, (y - b )*zoom)
                pygame.draw.line(self.ecran,(250,0,0),aa,bb ,int(20*zoom)) 
                pygame.draw.line(self.ecran,(250,0,0),bb,cc ,int(20* zoom))
                pygame.draw.line(self.ecran,(250,0,0),cc,aa ,int(20 * zoom))
        
        