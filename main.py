from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *
from draw import *

x1,y1,x2,y2 = 0,0,320,225
c = [[255,181,49],[255,255,255],[0,0,0],[200,200,200],[255, 0, 0],[0, 255, 0],[0, 0, 255],[255,255,0],[255,0,255]]
para = {"inter":0,"drap":0,"d_win":0,"sc_1":0,"sc_2":0,"ark":3,"ark_p":0,"adv":0,"nb_mine":15,"v_s":1,"v_p":3,"main":0,"c_txt":0}
sc= {"x":0,"o":0,"reload":False}
m_col = [[255,181,49],[6,150,187],[227,35,34],[198,35,126],[147,255,150],[224,141,172]]
click = {"nb_click":0,"cl_s":0,"cl_cl":1,"reborn":0,"t":0}

setting = Options([["Morpion","adver:",["bot random","bot ia","2 j"],"adv"],["Demineur","mine:",[str(n) for n in range(5,36)],"nb_mine"],["Snake","vitesse * ",["1","2","3"],"v_s"],["Pong","niveaux ",["easy","normal","hard"],"v_p"],["Main","colors:",["jaune","cyan","rouge","mauve","vert","rose"],"main"],["Couleur","",["white on black","black on white"],"c_txt"]],65,20,190,180)
    
### menu des jeux
def main():
  global para, setting
  rect(x1,y1,x2,y2,c[0])
  rect(65,10,190,200,c[1])
  menu = Carrousel(["morpion","demineur","pong","snake","arkanoid","cookie clicker","space invader","setting","leave"])
  ch = menu.Choisir(c)
  if ch % 9 == 0:
    from morpion import *
    morpion(c,para,sc)
    return
  elif ch % 9 == 1:
    from demineur import *
    demineur(c,para)
    return
  elif ch % 9 == 2:
    from pong import *
    pong(c,para)
    return
  elif ch % 9 == 3:
    fin = False
    while fin != True :
      from snake import *
      fin = snake(c,para)
    return
  elif ch % 9 == 4:
    from arkanoid import *
    arkanoid(c,para)
    return
  elif ch % 9 == 5:
    from cookie_clicker import *
    cookie_clicker(c,click)
    return
  elif ch % 9 == 6:
    from space_invader import *
    Spaces_invaders()
    return
  elif ch % 9 == 7:
    setting.launch(c)
    if setting.find("c_txt") == 0:
      c[1]=[255,255,255]
      c[2]=[0,0,0]
    else :
      c[1]=[0,0,0]
      c[2]=[255,255,255]
    c[0]= m_col[setting.find("main")]
    return 
  elif ch % 9 == 8:
    bye+1

while True:
  main()