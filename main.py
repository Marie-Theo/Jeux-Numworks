from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *
from draw import *

x1,y1,x2,y2 = 0,0,320,225
c = [[255,181,49],[255,255,255],[0,0,0],[200,200,200],[255, 0, 0],[0, 255, 0],[0, 0, 255],[255,255,0],[255,0,255]]
para = {"inter":0,"adv":0,"nb_mine":15,"drap":0,"d_win":0,"sc_1":0,"sc_2":0,"v_s":1,"v_p":3,"main":0,"c_txt":0,"ark":3,"ark_p":0}
sc= {"x":0,"o":0,"reload":False}
m_col = [[255,181,49],[6,150,187],[227,35,34],[198,35,126],[147,255,150],[224,141,172]]
click = {"nb_click":0,"cl_s":0,"cl_cl":1,"reborn":0,"t":0}

setting = Options([["morpion:","adver:",["bot random","bot ia","2 j"]],["demineur:","mine:",[str(n) for n in range(5,36)]],["snake:","vitesse * ",["1","2","3"]],["pong:","dificulter ",["easy","normal","hard"]],["main:","colors:",["jaune","cyan","rouge","mauve","vert","rose"]],["couleur:","",["black on white","white on black"]]])

### modifier les setting
def main():
  global para, setting

  # def d_sett_1():
  #   rect(x1,y1,x2,y2,c[0])
  #   rect(65,20,190,180,c[1])
  #   rect(240,25,10,170,(200,200,200))
  #   rect(240,25,10,85,(100,100,100))
  #   ds("morpion:",120,25,c[2],c[1])
  #   ds("demineur:",115,65,c[2],c[1])
  #   ds("snake:",130,105,c[2],c[1])
  #   ds("pong:",135,145,c[2],c[1])
  #   ds("mine :",70,85,c[2],c[1])

  # def d_sett_2():
  #   rect(65,20,190,180,c[1])
  #   rect(240,25,10,170,(200,200,200))
  #   rect(240,110,10,85,(100,100,100))
  #   ds("main colors:",100,25,c[2],c[1])
  #   ds("black/wite:",105,65,c[2],c[1])

  # def draw_sett():
  #   if para["inter"]%6 < 4:
  #     d_sett_1()
  #     rect(70,45,100,18,c[1])
  #     ds(m_adver[para["adv"]%3],70,45,c[2],c[1])
  #     ds(str(para["nb_mine"]),130,85,c[2],c[1])
  #     ds("vitesse * {}".format(para["v_s"]),70,125,c[2],c[1])
  #     rect(70,165,170,18,c[1])
  #     ds("dificulter {}".format(dif[para["v_p"]%3-2]),70,165,c[2],c[1])
  #     if para["inter"]%6 == 0:
  #       ds(m_adver[para["adv"]%3],70,45,c[2],c[3])
  #     elif para["inter"]%6 == 1:
  #       rect(130,85,20,18,c[1])
  #       ds(str(para["nb_mine"]),130,85,c[2],c[3])
  #     elif para["inter"]%6 == 2:
  #       ds("vitesse * {}".format(para["v_s"]),70,125,c[2],c[3])
  #     elif para["inter"]%6 == 3:
  #       ds("{}".format(dif[para["v_p"]%3-2]),180,165,c[2],c[3])
  #   else:
  #     d_sett_2()
  #     ds("{}".format(main_c[para["main"]]),70,45,c[2],c[1])
  #     ds("{}".format(bg[para["c_txt"]]),70,85,c[2],c[1])
  #     if para["inter"]%6 == 4:
  #       ds("{}".format(main_c[para["main"]]),70,45,c[2],c[3])
  #     elif para["inter"]%6 == 5:
  #       ds("{}".format(bg[para["c_txt"]]),70,85,c[2],c[3])

  # draw_sett()
  # while True:
  #   sleep(0.2)
  #   if ke(0):
  #     if para["inter"]%6 == 0:  
  #       para["adv"]-=1
  #     elif para["inter"]%6 == 1 and para["nb_mine"]> 1 :
  #       para["nb_mine"]-=1
  #     elif para["inter"]%6 == 2 and para["v_s"]> 1 :
  #       para["v_s"]-=1
  #     elif para["inter"]%6 == 3 and para["v_p"]> 2 :
  #       para["v_p"]-=1
  #     elif para["inter"]%6 == 4 and para["main"] > 0:
  #       para["main"]-=1
  #     elif para["inter"]%6 == 5 and para["c_txt"] > 0:
  #       para["c_txt"]-=1
  #     draw_sett()
  #   elif ke(3):
  #     if para["inter"]%6 == 0: 
  #       para["adv"]+=1
  #     elif para["inter"]%6 == 1 and para["nb_mine"]< 30 :
  #       para["nb_mine"]+=1
  #     elif para["inter"]%6 == 2 and para["v_s"]< 3 :
  #       para["v_s"]+=1
  #     elif para["inter"]%6 == 3 and para["v_p"]< 4 :
  #       para["v_p"]+=1
  #     elif para["inter"]%6 == 4 and para["main"] < 5:
  #       para["main"]+=1
  #     elif para["inter"]%6 == 5 and para["c_txt"] < 1:
  #       para["c_txt"]+=1
  #     draw_sett()
  #   elif ke(1):
  #     para["inter"]-=1
  #     draw_sett()
  #   elif ke(2):
  #     para["inter"]+=1
  #     draw_sett()
  #   elif ke(4):
  #     return 
    
### menu des jeux / setting
def main():
  global para
  rect(x1,y1,x2,y2,c[0])
  rect(65,10,190,200,c[1])
  menu = Carrousel(["morpion","demineur","pong","snake","arkanoid","cookie clicker","space invader","setting","leave"])
  ch = menu.Choisir()
  if ch % 9 == 0:
    from morpion import *
    morpion(c,para,m_adver,sc)
    return
  elif ch % 9 == 1:
    from demineur import *
    demineur(c,para)
    return
  elif ch % 9 == 2:
    from pong import *
    pong(c,para,dif)
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
    setting.write(c)
    # setting()
    # if para["c_txt"] == 0:
    #   c[1]=[255,255,255]
    #   c[2]=[0,0,0]
    # else :
    #   c[1]=[0,0,0]
    #   c[2]=[255,255,255]
    # c[0]= m_col[para["main"]]
    return 
  elif ch % 9 == 8:
    bye+1

while True:
  main()