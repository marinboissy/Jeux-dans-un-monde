import pygame

class control:
    def __init__(self, zone):
        self.haut = pygame.K_UP
        self.bas = pygame.K_DOWN
        self.droite = pygame.K_RIGHT
        self.gauche = pygame.K_LEFT
        self.zone = zone
        self.inertie = 0
        self.vmax = 15
        self.saut = 0
    def control(self, controle, x, y,hauteursaut,eautouche):
        libre=True 
        saut_possible = False
                
        clavier = pygame.key.get_pressed()
        if self.inertie > 0:
            self.inertie -=1
        elif self.inertie <0:
            self.inertie+=1
        else:
            self.inertie = 0 
               
        if controle== 1 : 
             if clavier[self.droite] and self.inertie < self.vmax:
                 self.inertie += 2
             if clavier[self.gauche] and self.inertie > -self.vmax :
                 self.inertie -= 2
                 
             
        for g, d, h, b in self.zone:
            if ((g <= x+ self.inertie + 200 <=d) or (g<=x+self.inertie <= d)) and ( b < y +200< h or  b < y < h) :
                libre = False
                break
                    
         
        if libre == True:
            x =x + self.inertie
        else:
            self.inertie = 0
        libre = True
        
        
        if eautouche is False:
            for g, d, h, b in self.zone:
                if ((g <= x+  200 <=d) or (g <= x <= d)) and y== h :
                    saut_possible = True
                
            if controle == 1:
                if clavier[self.haut] and saut_possible == True:
                    self.saut = hauteursaut
                 
            for g, d, h, b in self.zone:
                if ((g < x + 200 <d) or (g < x < d)) and b < y + self.saut+200< h :
                    libre = False
                    break
            if libre == True and self.saut > 1:
                y += self.saut
                self.saut -= 3
            else:
                self.saut = 0
        else:
            if controle == 1:
                if clavier[self.haut]:
                    self.saut = 44
                 
            for g, d, h, b in self.zone:
                if ((g < x + 200 <d) or (g < x < d)) and b < y + self.saut+200< h :
                    libre = False
                    break
            if libre == True and self.saut > 1:
                y += self.saut
                self.saut -= 2
            else:
                self.saut = 0
           
        return [x,y]    