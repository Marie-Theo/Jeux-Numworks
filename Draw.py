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
    def __init__(self, k, x, y, text, c, bc):
        super().__init__(x, y, c)
        self.key = k
        self.text = text
        self.bc = bc
        self.tbc = bc
    def toString(self):
        ds(self.text,self.x,self.y,self.c,self.bc)

class Texts (Text):
    def __init__(self, menu,c,bc):
        self.menu = menu
        self.textes = [Text(n, 160-(len(menu[n])*5), n*20+(220//2-len(menu)*10), menu[n],c,bc) for n in range(len(menu))]

    def Draw(self, ch, r=False):
        for text in self.textes:
            if ch % len(self.menu) == text.key:
                text.bc = [200,200,200]
                text.toString()
            elif (ch-1) % len(self.menu) == text.key or (ch+1) % len(self.menu) == text.key:
                text.bc = text.tbc
                text.toString()
            elif r:
                text.toString()

class Carrousel ():
    def __init__(self, menu, c=[0,0,0], bc = [255,255,255]):
        self.Text_Menu = Texts(menu,c,bc)
        self.ch = 0

    def Choisir(self):
        self.Text_Menu.Draw(self.ch,True)
        while True :
            sleep(0.1)
            if ke(1):
                self.ch-=1
                self.Text_Menu.Draw(self.ch)
            elif ke(2):
                self.ch+=1
                self.Text_Menu.Draw(self.ch)
            elif ke(4):
                return self.ch

class Option(Text):
    def __init__(self, mode, x, y, titre, choix, select=0, c=[0,0,0], bc = [255,255,255]):
        self.mode = Text(0, 160-(len(mode)*5), y, mode, c, bc)
        self.titre = Text(1, x, y+10, titre, c, bc)
        self.choix = choix
        self.select = select

class Options():
    def __init__(self,List):
        self.inter = 0
        self.lists = [Option(List[n][0], 70, List[n][1], List[n][2], List[n][3]) for n in range(len(List))]