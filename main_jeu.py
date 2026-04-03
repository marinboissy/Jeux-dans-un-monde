import pygame
from afficheur_de_text import Text
from gravité import gravité 
from dessiner_sol import Dessiner
from control import control
from mort import Mort
# initialisation pygame
pygame.init()
ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
continuer = True
#zone g d h b
zone= [[-1000,16000,20,-100000],[-10000,0,600,-10000],[800,1000,100,-10],[1600,2600,100,-10],[1800,2500,200,-10], [4200,7000,200,-10],[5000,6000,300,-10],[6300,6900,400,0],[7400,8500,200,-10],[8000,8500,400,100],[9500,11000,150,-10],[10000,11000,300,-10],[10100,12000,550,280],[10300,10500,800,300],[10900,11150,800,300],[11700,12000,800,300],[13500,14500,500,0],[13800,14500,1000,0],[14300,14500,1500,0],[15000,15300,500,0],[16000,16800,-200,-50000],[16800,18000,-400,-50000],[18000,19000,-800,-50000],[19000,19200,-200,-50000],[19200,19500,0,-50000],[19500,21000,-800,-50000],[21000,21200,-200,-50000],[19800,20700,-50,-200],[21200,23000,0,-50000],]
#fleur g d b
fleur=[[0,400,10],[1800,2500,200],[4300,5000,200],[5000,6000,300],[7400,8000,200],[8700,9500,0]]
#mort g b n
mortt= [[2600,10,2],[3200,10,2],[6900,10,5],[10500,540,13],[5500,300,2],[14500,0,5],[15300,0,6],[19800,-60,9]] 
# eau g d h b
eau = [[16800, 18200, -200,-500],[18000,19000,-200,-900],[19500,21000,-200,-850]]
#checkpoint g b 
checkpoint = [[500,0],[6800,400],[16700,-200],[21500,0],[30000,0]]
#numéro du dernier valider
valide= 0
#niveau animation
level_animation = 0
# police
font = pygame.font.Font(None, 75)
mouvement = 0 
hauteursaut =99
nbiteration = 0
# images
banderol = pygame.image.load("pixil-frame-0 (15).png")
perso = pygame.image.load("pixil-frame-0 (16).png")
fleur1 =  pygame.image.load("pixil-frame-0 (17).png")
fleur2 =  pygame.image.load("pixil-frame-0 (18).png")
fleur3 =  pygame.image.load("pixil-frame-0 (19).png") 
sapin = pygame.image.load("pixil-frame-0 (21).png")
# position personnage
camerax = 800
cameray = 800
x_start= 0
y_start = 300
x = x_start
y = y_start
# création du gestionnaire de texte
texte = Text(ecran, banderol, font)
texte.txtmessage = "mais que fais-je ici ?"
texte.tpsmessage = pygame.time.get_ticks() / 100
tpseau = 0
g=gravité(zone)
dessiner = Dessiner(zone,mortt,ecran,perso,fleur,fleur1,fleur2,fleur3,sapin,checkpoint,eau)
control = control(zone)
mort = Mort(mortt)
# boucle de jeu 
overlay = pygame.Surface((1920, 1200))  # même taille que l'écran
overlay.fill((255, 0, 0))  

# dans la boucle principale
ecran.blit(overlay, (0, 0))
while continuer:
    clock.tick(40)
    temps = pygame.time.get_ticks()
    #une fois sur 10:
    if nbiteration % 10 == 0:
        # avancement dans les niveaux
        if x > checkpoint [valide + 1] [0]:
            valide += 1  
        # niveau animation
        if level_animation == 0 and x > 2000:
            texte.txtmessage = "quel drole de monde"
            texte.tpsmessage = pygame.time.get_ticks() / 100
            level_animation =1
        if level_animation == 1 and x > 6000:
            texte.txtmessage = "mais rien de très special "
            texte.tpsmessage = pygame.time.get_ticks() / 100
            level_animation =2
        if level_animation == 2 and 11100 <= x <=11300 and y < 250:
            level_animation = 3
            texte.txtmessage = "j'ai toujour revé d'etre un super héro"
            texte.tpsmessage = pygame.time.get_ticks() / 100
            hauteursaut = 90
        if (level_animation == 3 or level_animation == 2 )and x >= 16800:
            level_animation = 4
            texte.txtmessage = "Tien de l'eau"
            texte.tpsmessage = pygame.time.get_ticks() / 100
        if (level_animation == 4 )and x >= 18000:
            level_animation = 5
            texte.txtmessage = "Il faut penser a remonter"
            texte.tpsmessage = pygame.time.get_ticks() / 100
    if level_animation == 3:
        if temps / 100 - texte.tpsmessage <= 50:
            zoom = 1 - (temps  / 100 -texte.tpsmessage) / 100
        else:
            zoom = 0.5
            hauteursaut = 90
    if level_animation == 4:
        if temps / 100 - texte.tpsmessage <= 50:
            zoom = 0.5 + (temps  / 100 -texte.tpsmessage) / 100
        else:
            zoom = 1
   
    #verifie si eau:
    eautouche = False
    for gg, d, h, b in eau:
        if gg <= x and x + 200 <= d and y <= h and b <= y :
            eautouche = True
            break
    if eautouche is not True:
        tpseau = 0
    elif tpseau == 0:
        tpseau = temps 
        
    #gestionnaire du début: 
    if temps <= 5000:
        mouvement = 0
        zoom = (1+ temps)/ 5001
         
    elif level_animation <=2 :
        mouvement = 1
        zoom = 1
        hauteursaut = 78
        
    
    cameray = 800 *(1/zoom)
    cameraxx = camerax // zoom
        
    y = g.calculer(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    ecran.fill((135, 206, 235))
    dessiner.dessiner(x,y,cameraxx,cameray,zoom,valide,level_animation)
    calcul =control.control(mouvement, x,y,hauteursaut,eautouche)
    x = calcul[0]
    y = calcul[1]
    if mort.mort(x,y) == True or (tpseau != 0 and temps-tpseau > 5000):
        x = checkpoint[valide] [0]-300
        y = checkpoint[valide] [1]+100
    #sol.afficher(x,y)
    texte.text(temps)
    #si eau
    if tpseau != 0:
        overlay.set_alpha((temps-tpseau)//50)  # transparence (0 = invisible, 255 = opaque)
        ecran.blit(overlay, (0, 0))
    pygame.display.flip()
    nbiteration +=1