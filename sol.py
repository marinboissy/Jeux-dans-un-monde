import pygame
class Sol:
    def __init__(self,ecran,sol):
        self.ecran = ecran
        self.sol = sol
        
    def afficher(self,x,y):
        xx = x % 2000
        self.ecran.blit(self.sol,(xx-2000,y))
        self.ecran.blit(self.sol,(xx,y))