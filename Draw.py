from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from time import *

class Draw ():
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        pass

class Rectangle (Draw):
    def __init__(self, x, y, longueur, largeur, c = [0,0,0]):
        super().__init__(x, y, c)
        self.longueur = longueur
        self.largeur = largeur
    
    def DrawRectangle(self):
        print(self.x, self.y, self.longueur, self.largeur, self.c)

class Text (Draw):
    def __init__(self, k, x, y, text, c = [0,0,0], bc = [255,255,255]):
        super().__init__(x, y, c)
        self.key = k
        self.text = text
        self.bc = bc
    
    def toString(self):
        print(self.key,'|', self.text,' ',self.x,' ',self.y,' ',self.c,' ',self.bc)

class Texts (Text):
    def __init__(self, menu):
        self.menu = menu
        self.Texts = [Text(n, 160-(len(menu[n])*5), n*40+25, menu[n]) for n in range(len(menu))]
    
    def AfficherChoix(self, ch):
        for text in self.Texts:
            if ch % len(self.menu) == text.key:
                text.bc = [200,200,200]
                text.toString()
            elif (ch-1) % len(self.menu) == text.key or (ch+1) % len(self.menu) == text.key:
                text.bc = [255,255,255]
                text.toString()

class Carrousel ():
    def __init__(self, menu):
        self.Text_Menu = Texts(menu) 

        self.ch = 0
        self.Text_Menu.AfficherChoix(self.ch)
        self.Choisir()
    
    def Choisir(self):
        while True :
            sleep(0.1)
            if ke(1):
                self.ch-=1
                self.Text_Menu.AfficherChoix(self.ch)
            elif ke(2):
                self.ch+=1
                self.Text_Menu.AfficherChoix(self.ch)
            elif ke(4):
                return self.ch

choixUser = Carrousel(["morpion","demineur","pong","snake","arkanoid","cookie clicker","space invader","setting","leave"])
print(choixUser)