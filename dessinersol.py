import pygame
class Sol:
    def __init__(self,ecran,zone):
        self.ecran= ecran
        self.zone = zone
        
    def sol(self, x, y, zoom,camerax):
        for g, d, h, b in self.zone:
            if not( 20 >= (d - x) * zoom  or (g -x) * zoom > 1900):
                if h >=400:
                    if b <= 0:
                        limita = h
                        limitb = 350
                        limitc = 0
                        hauteura = h - 350
                        hauteurb = 350
                        hauteurc = 0 - b
                    else:
                        if b <= 400:
                            limita = h
                            limitb = 350
                            limitc = 0
                            hauteura = h - 350
                            hauteurb = 350 - b
                            hauteurc = 0
                        else:
                            limita = h
                            limitb = 0
                            limitc = 0
                            hauteura = h - b
                            hauteurb = 0
                            hauteurc = 0
                else:
                    if b <= 0:
                        if h>= 0:
                            limita = 0
                            limitb = h
                            limitc = 0
                            hauteura = 0
                            hauteurb = h
                            hauteurc = 0 - b
                        else:
                            limita = 0
                            limitb = 0
                            limitc = h
                            hauteura = 0
                            hauteurb = 0
                            hauteurc = h-b
                    else:
                        limita = 0
                        limitb = h
                        limitc = 0
                        hauteura = 0
                        hauteurb = h-b
                        hauteurc = 0 
                  
                
                if hauteura!= 0:
                    pygame.draw.rect(
                        self.ecran,
                        (50,200,50),
                        ((g - x) * zoom, (y -limita) * zoom, (d - g)*zoom, hauteura * zoom)
                        )
                if hauteurb != 0:        
                    pygame.draw.rect(
                        self.ecran,
                        (0,150,0),
                        ((g - x) * zoom, (y - limitb) * zoom, (d - g)*zoom, hauteurb * zoom)
                        )
                if hauteurc != 0:
                    pygame.draw.rect(
                        self.ecran,
                        (140,80,40),
                        ((g - x) * zoom, (y -limitc) * zoom, (d - g )*zoom, hauteurc * zoom)
                        )
                        
                if hauteura != 0:
                    color = (100,100,100)
                else:
                    color = (0,250,0)
                
                pygame.draw.rect(
                    self.ecran,
                    color,
                    ((g - x)* zoom, (-h +y)*zoom, (d - g)*zoom, 20*zoom))
                        
