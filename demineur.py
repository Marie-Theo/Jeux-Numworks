from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *

x1,y1,x2,y2 = 0,0,320,225

def demineur(c,para,setting):
  co = [c[5],c[6],c[0],c[4],c[2],c[8],c[8],c[8]]
  rect(0,0,x2,y2,c[0])
  rect(60,0,x2-60,y2,c[2])

  while True:
    start = True
    gri = [[],[],[],[],[],[],[],[],[],[],[],[]]
    dec = [[],[],[],[],[],[],[],[],[],[],[],[]]
    ### crée maps
    for i in range(12):
      for j in range(10):
        gri[i].append(0)
        dec[i].append(False)
        rect(65+i*21,6+j*21,20,20,c[1])
    def create_maps(ch_x,ch_y):
      ### initialiser les mine
      for z in range(int(setting.varSelected("nb_mine"))):
        while True :
          x,y = randint(0,11),randint(0,9)
          if gri[x][y] == 0 and x != ch_x and y != ch_y:
            gri[x][y] = "b"
            break
      ### definir le nb de mine autour
      for i in range(12):
        for j in range(10):
          if gri[i][j] != 'b':
            n = 0
            for x_ in range(3):
              x__=i+1-x_
              for y_ in range(3):
                y__= j+1-y_
                if 0 <=x__<= 11 and 0<= y__ <= 9 :
                  if gri[x__][y__] == 'b' :
                    n+=1
            gri[i][j] = n

    ### enlever tous les 0 autour
    def decouvrir():
      n= (-1,1)
      refresh = True
      while refresh == True:
        refresh = False
        for z in range(2):
          for i in range(12):
            for j in range(10):
              for x_ in n:
                x__=i+x_
                for y_ in n:
                  y__= j+y_
                  if 0 <=x__<= 11 and 0<= y__ <= 9 and dec[i][j] == True and gri[i][j] == 0:
                    if gri[x__][j] == 0 and dec[x__][j] != True:
                      if dec[x__][j] == "drap":
                        para["drap"]-=1
                      refresh = True
                      dec[x__][j] = True
                      draw_case(x__,j,"other")
                    elif gri[i][y__] == 0 and dec[i][y__] != True:
                      if dec[i][y__] == "drap" :
                        para["drap"]-=1
                      refresh = True
                      dec[i][y__] = True
                      draw_case(i,y__,"other")

    def draw_drap(x,y):
      rect(x,y-4,1,15,c[2])
      for l in range(9):
        for j in range(l):
          sp(x-l+9,y-j+4,c[4])

    def draw_case(x,y,ch):
      if ch =="draw_drap":
        draw_drap(30,10)
        return
      if ch== "vide":
        coul = c[1]
      elif ch== "other":
        rect(65+x*21,6+y*21,20,20,c[5])
        return
      else:
        coul = c[3]
      rect(65+x*21,6+y*21,20,20,coul)
      if dec[x][y] == False:
        return
      elif dec[x][y] == "drap" :
        draw_drap(70+x*21,11+y*21)
      else :
        if gri[x][y] == 0 and  ch== "vide" :
          rect(65+x*21,6+y*21,20,20,c[5])
        elif gri[x][y] == "b":
          rect(65+x*21,6+y*21,20,20,c[4])
        for i in range(1,9):
          if gri[x][y] == i:
            ds(str(i),65+x*21+5,6+y*21,co[i-1],coul)
    
    def d_win(): 
      drap_bon = 0
      for x in range(12):
        for y in range(10):
          if gri[x][y] == "b" and dec[x][y] == "drap":
            drap_bon += 1
      if int(setting.varSelected("nb_mine")) == drap_bon:
        para["d_win"] += 1
        return True
      
    ch_x ,ch_y = 0,0
    draw_case(ch_x,ch_y,"select")
    para["drap"]=0
    draw_case(0,0,"draw_drap")
    rect(10,20,50,20,c[0])
    ds("{}/{}".format(para["drap"],int(setting.varSelected("nb_mine"))),10,20,c[2],c[0])
    ds("win:",5,40,c[2],c[0])
    ds("{}".format(para["d_win"]),5,60,c[2],c[0])

    while True:
      sleep(0.1)
      if ke(1):
        draw_case(ch_x,ch_y,"vide")
        ch_y-=1
        if ch_y<0: 
          ch_y=9
        draw_case(ch_x,ch_y,"select")
      elif ke(2):
        draw_case(ch_x,ch_y,"vide")
        ch_y+=1
        if ch_y>9: 
          ch_y=0
        draw_case(ch_x,ch_y,"select")
      if ke(0):
        draw_case(ch_x,ch_y,"vide")
        ch_x-=1
        if ch_x<0: 
          ch_x=11
        draw_case(ch_x,ch_y,"select")
      elif ke(3):
        draw_case(ch_x,ch_y,"vide")
        ch_x+=1
        if ch_x>11: 
          ch_x=0
        draw_case(ch_x,ch_y,"select")
      if ke(52) and dec[ch_x][ch_y] == False:
        if start == True :
          start = False
          create_maps(ch_x,ch_y)
        dec[ch_x][ch_y] = True
        draw_case(ch_x,ch_y,"select")
        if gri[ch_x][ch_y] == "b":
          for x in range(12):
            for y in range(10):
              dec[x][y] = True
              draw_case(x,y,"vide")
          rect(10,20,50,20,c[0])
          ds("{}/{}".format(para["drap"],int(setting.varSelected("nb_mine"))),10,20,c[2],c[0])
          sleep(3)
          break
        elif gri[ch_x][ch_y] == 0:
          decouvrir()
          rect(10,20,50,20,c[0])
          ds("{}/{}".format(para["drap"],int(setting.varSelected("nb_mine"))),10,20,c[2],c[0])
      if ke(4) :
        if dec[ch_x][ch_y] == False and int(setting.varSelected("nb_mine")) > para["drap"]:
          dec[ch_x][ch_y] = "drap"
          para["drap"]+=1
        elif dec[ch_x][ch_y] == "drap":
          dec[ch_x][ch_y] = False
          para["drap"]-=1
        draw_case(ch_x,ch_y,"select")
        rect(10,20,50,20,c[0])
        ds("{}/{}".format(para["drap"],int(setting.varSelected("nb_mine"))),10,20,c[2],c[0])
        if int(setting.varSelected("nb_mine")) == para["drap"]:
          win = d_win() 
          if win == True :
            sleep(2)
            break
      if ke(17):
        return
