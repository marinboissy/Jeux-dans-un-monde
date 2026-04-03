class gravité:
    def __init__(self, zone):
        self.force = 30
        self.vmax = 15
        self.zone = zone

    def calculer(self, x, y):

        sol = None

        # cherche le sol sous le joueur
        for g, d, h, b in self.zone:
            if ((g <= x and x <= d)  or( g <= x+200 and x+200 <= d )) and h <= y:
                if sol is None or h >sol:
                    sol = h

        # chute
        if sol is None:
            y -= self.force
        else:
            y -= self.force
            if y <sol:
                y= sol

        return y