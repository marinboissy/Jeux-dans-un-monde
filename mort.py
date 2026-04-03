class Mort:
    def __init__(self,mortt):
         self.zone= mortt
    def mort(self,x,y):
         touche = False
         for g, b, n in self.zone:
             if ((g <= x+20 and x+20 <= g + n * 100)  or( g <= x+180 and x+180 <= g + n * 100 )) and ( b <=y <= b + 75 or b <= y + 200 <= b+75):
                 touche = True
                 break
         return touche