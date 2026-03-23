from kandinsky import fill_rect as rect , get_pixel as gp, draw_string as ds
from ion import keydown as ke
from math import *
from time import *
from random import *

def Spaces_invaders():
  global x_ene, x_ene, px1, px2,px3 , x_b, y_b, sc, n_e
  c = [(255,255,255),(0,0,0),(255, 0, 0),(0, 255, 0)]
  px1=[[0,0,20,15,0],[0,0,7,2,1],[13,0,7,2,1],[0,2,2,2,1],[18,2,2,2,1],[5,5,3,1,1],[12,5,3,1,1],[9,8,2,1,1],[0,8,3,2,1],[17,8,3,2,1],[7,12,6,3,1],[0,13,3,2,1],[17,13,3,2,1],[5,11,3,2,1],[12,11,3,2,1]]
  px2=[[0,4,20,9,0],[3,0,2,2,0],[15,0,2,2,0],[5,2,2,2,0],[13,2,2,2,0],[0,4,3,2,1],[17,4,3,2,1],[0,6,1,1,1],[19,6,1,1,1],[2,8,2,5,1],[16,8,2,5,1],[6,13,3,2,0],[11,13,3,2,0],[6,11,8,2,1],[6,6,2,2,1],[12,6,2,2,1]]
  px3=[[0,0,20,10,0],[0,0,6,2,1],[14,0,6,2,1],[0,2,4,2,1],[16,2,4,2,1],[0,4,2,2,1],[18,4,2,2,1],[2,13,2,2,0],[16,13,2,2,0],[4,11,2,2,0],[14,11,2,2,0],[6,10,2,1,0],[12,10,2,1,0],[8,11,4,2,0],[6,13,2,2,0],[12,13,2,2,0],[6,6,2,2,1],[12,6,2,2,1]]
  x=int(320/2)

  def decor():
    rect(0,0,320,225,c[1])
    rect(0,195,320,2,c[3])
    for n in range(4):
      rect(n*70+35,145,35,25,c[3])
      rect(n*70+35,145,5,5,c[1])
      rect(n*70+65,145,5,5,c[1])
      rect(n*70+45,160,15,10,c[1])

  def player(x):
    rect(x-20,180,35,10,c[1])
    rect(x-10,178,15,3,c[1])
    rect(x-15,180,25,10,c[3])
    rect(x-5,178,5,3,c[3])

  def move_ene():
    rect(0,y_ene-1,320,91,c[1])
    for i in range(12):
      if len(enemies)!=12:
        enemies.append([])
      for j in range(4):
        if len(enemies[i])!=4:
          if j==0:
            enemies[i].append("3")
          elif j==1:
            enemies[i].append("2")
          else:
            enemies[i].append("1")
        x_,y_=i*25+x_ene,j*25+y_ene
        if enemies[i][j]=="1":
          for l in range(len(px1)):
            rect(x_+px1[l][0],y_+px1[l][1],px1[l][2],px1[l][3],c[px1[l][4]])
        elif enemies[i][j]=="2":
          for l in range(len(px2)):
            rect(x_+px2[l][0],y_+px2[l][1],px2[l][2],px2[l][3],c[px2[l][4]])
        elif enemies[i][j]=="3":
          for l in range(len(px3)):
            rect(x_+px3[l][0],y_+px3[l][1],px3[l][2],px3[l][3],c[px3[l][4]])
  
  def vie_graph(vie):
    for i in range(vie):
      rect(i*35+5,205,25,10,c[3])
      rect(i*35+15,203,5,3,c[3])

  while True:
    x_ene,y_ene,x_b,y_b,dec,vittesse,sc,bxe,bye,vie,enemies,n_e=12,30,0,0,10,1,0,[],[],3,[],48
    decor()
    player(x)
    ds("score:{}".format(sc),310-(len("score:{}".format(sc))*10),200,c[0],c[1])
    move_ene()
    vie_graph(vie)
    while vie!=0:
      sleep(0.02)
      if ke(0) and x>20:
        x -=2
        player(x)
      elif ke(3) and x<305:
        x+=2
        player(x)
      if y_b!=0:
        rect(x_b,y_b,3,8,c[1])
        y_b-=1
        if y_b<=0:
          x_b,y_b=0,0
        else:
          rect(x_b,y_b,3,7,c[0])
        if gp(x_b,y_b-1) == c[3]:
          y_b-=1
          rect(x_b,y_b,3,8,c[1])
          x_b,y_b=0,0
        if gp(x_b,y_b-1) == c[0]:
          y_b-=1
          rect(x_b,y_b,3,8,c[1])
          for i in range(12):
            for j in range(4):
              if enemies[i][j]!="0":
                if x_b<i*25+x_ene+20 and x_b>i*25+x_ene and y_b<j*25+y_ene+15 and y_b>j*25+y_ene :
                  if enemies[i][j]=="1":
                    sc+=10
                  elif enemies[i][j]=="2":
                    sc+=20
                  elif enemies[i][j]=="3":
                    sc+=40
                  ds("score:{}".format(sc),310-(len("score:{}".format(sc))*10),200,c[0],c[1])
                  enemies[i][j]="0"
                  n_e-=1
                  if n_e == 0:
                    enemies,x_ene,y_ene,dec,bxe,bye,n_e=[],12,30,10,[],[],48
                    vie+=1
                    vie_graph(vie)
                  move_ene()
                  x_b,y_b=0,0
      elif ke(52) or ke(4):
        x_b,y_b=x-4,170
      n=-1
      for b in range(len(bxe)):
        rect(bxe[n],bye[n],2,7,c[1])
        bye[n]+=1
        if gp(bxe[n]+1,bye[n]+6)==c[3]:
          if (bye[n]+7>170) and (bye[n]+7<190):
            rect((vie-1)*35+5,205,25,10,c[1])
            rect((vie-1)*35+15,203,5,3,c[1])
            vie-=1
          elif bye[n]+7<170 :
            rect(bxe[n],bye[n],2,9,c[1])
          bxe.pop(n)
          bye.pop(n)
        else:
          rect(bxe[n],bye[n],2,7,c[0])
          n-=1

      if dec == 0:
        col= randint(0,11)
        while enemies[col]==["0","0","0","0"]:
          col = randint(0,11)
        for p in range(4):
          if enemies[col][-p-1]!="0":
            bxe.append(col*25+11+x_ene)
            bye.append((3-p)*25+15+y_ene)
            break

        if x_ene%25==0:
          if vittesse>0:
            if enemies[-(x_ene//25)]!=["0","0","0","0"]:
              vittesse-=2
          else :
            if enemies[x_ene//25]!=["0","0","0","0"]:
              vittesse+=2
        x_ene+=vittesse
        dec=20
        move_ene()
      else:
        dec-=1
      if ke(17):
        return True
    rect(0,y_ene-1,320,91,c[1])
    ds("GAME OVER",115,55,c[0],c[1])
    ds("score:{}".format(sc),110,75,c[0],c[1])
    ds("[EXE]",135,95,c[0],c[1])
    while True:
      if ke(52 or 4):
        rect(0,y_ene-1,320,91,c[3])
        break
      if ke(17):
        return True