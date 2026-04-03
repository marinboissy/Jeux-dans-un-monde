import pygame
# ordre gauche droite haut bas
zone= [[100,100,100,1000,]]
class Text:
    def __init__(self, ecran, banderol, font):
        self.ecran = ecran
        self.banderol = banderol
        self.font = font
        self.txtmessage = ""
        self.tpsmessage = 0

    def text(self, temps):
        if self.txtmessage != "":
            message1 = ""
            i = 0

            while (
                temps / 100 - self.tpsmessage > len(message1)
                and len(message1) < len(self.txtmessage)
            ):
                message1 += self.txtmessage[i]
                i += 1

            self.ecran.blit(self.banderol, (200, 100))
            self.ecran.blit(
                self.font.render(message1, True, (0, 0, 0)),
                (250, 170),
            )

            if temps / 100 - self.tpsmessage > len(message1) + 20:
                self.txtmessage = ""