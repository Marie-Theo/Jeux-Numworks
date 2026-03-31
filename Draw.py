from kandinsky import fill_rect as rect ,draw_string as ds,set_pixel as sp
from ion import keydown as ke
from time import *

class Draw ():
    def __init__(self,x,y,c):
        self.x,self.y,self.c=x,y,c

class Rectangle (Draw):
    def __init__(self,x,y,longueur,largeur,c=[0,0,0]):
        super().__init__(x,y,c)
        self.longueur=longueur
        self.largeur=largeur
    
    def DrawRectangle(self):
        print(self.x,self.y,self.longueur,self.largeur,self.c)

class Text (Draw):
    def __init__(self,k,x,y,text,c,bc):
        super().__init__(x,y,c)
        self.key=k
        self.text=text
        self.bc=bc
        self.tbc=bc
    def write(self):
        ds(self.text,self.x,self.y,self.c,self.bc)
    def clear(self):
        this=self.choix[self.select]
        rect(this.x+10,this.y,155-len(self.titre.text)*10,18,[255,255,255])

class Texts (Text):
    def __init__(self,menu,c,bc):
        self.menu=menu
        self.textes=[Text(n,160-(len(menu[n])*5),n*20+(220//2-len(menu)*10),menu[n],c,bc)for n in range(len(menu))]

    def Draw(self,ch,r=False):
        for text in self.textes:
            if ch%len(self.menu)==text.key:
                text.bc=[200,200,200]
                text.write()
            elif(ch-1)%len(self.menu)==text.key or(ch+1)%len(self.menu)==text.key:
                text.bc=text.tbc
                text.write()
            elif r:
                text.write()

class Carrousel ():
    def __init__(self,menu,c=[0,0,0],bc=[255,255,255]):
        self.Text_Menu=Texts(menu,c,bc)
        self.ch=0

    def Choisir(self):
        self.Text_Menu.Draw(self.ch,True)
        while ke(4):sleep(0.1)
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
    def __init__(self,scroll,mode,x,y,titre,choix,select=0,c=[0,0,0],bc=[255,255,255]):
        self.scroll=scroll//4
        self.mode=Text(0,160-(len(mode)*5),y,mode,c,bc)
        self.titre=Text(1,x,y+20,titre,c,bc)
        self.choix=[Text(2,len(titre)*10+x,y+20,ch,c,bc)for ch in choix]
        self.select=select
    def draw(self):
        self.mode.write()
        self.titre.write()
    def drawChoix(self,bc=[255,255,255]):
        self.choix[self.select].bc=bc
        self.choix[self.select].write()

class Options():
    def __init__(self,List,x1,y1,x2,y2,c,bg_C):
        self.inter,self.tmp=0,0
        self.bg_C,self.c=bg_C,c
        self.x1,self.x2,self.y1,self.y2=x1,x2,y1,y2
        self.lists=[Option(n,List[n][0],70,26+40*(n%4),List[n][1],List[n][2])for n in range(len(List))]
    def setChoix(self,z):
        self.tmp=self.inter
        self.lists[self.inter].select=(self.lists[self.inter].select+z)%len(self.lists[self.inter].choix)
    def setInter(self,z):
        self.tmp=self.inter
        self.inter=(self.inter+z)%len(self.lists)
    def refresh(self):
        i,t=self.inter,self.tmp
        if (i%4==0)and((t)%4==3)or(i%4==3)and((t)%4==0)or((i==len(self.lists)-1)and t==0)or((t==len(self.lists)-1)and i==0):
            self.drawBG()
        for n in range(len(self.lists)):
            if self.lists[n].scroll==i//4:
                self.lists[n].draw()
                bc=[255,255,255]
                if i%len(self.lists)==n:
                    bc=[200,200,200]
                    self.lists[n].clear()
                self.lists[n].drawChoix(bc)
    def drawBG(self):
        rect(self.x1,self.y1,self.x2,self.y2,self.bg_C)
        x,y1,y2,lenList=self.x1+self.x2-20,self.y1,self.y2,self.y2//(len(self.lists)//4+1)
        rect(x,y1,20,y2,self.c[3])
        rect(x+2,y1+lenList*((self.inter//4)%4)+2,16,lenList-4,[100,100,100])
    def launch(self):
        rect(0,0,320,225,self.c[0])
        self.drawBG()
        self.refresh()
        while ke(4):sleep(0.1)
        while True:
            if ke(0)or ke(1)or ke(2)or ke(3):sleep(0.2)
            sleep(0.1)
            if ke(4)or ke(17):
                return
            if ke(1):
                self.setInter(-1)
            elif ke(2):
                self.setInter(1)
            elif ke(0):
                self.setChoix(-1)
            elif ke(3):
                self.setChoix(1)
            else:
                continue
            self.refresh()