from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *

x1,y1,x2,y2 = 0,0,320,225

def snake(c,para,setting):
  def death():
    for x in range(16):
      for y in range(11):
        if gri[y][x]!= "b":
          if gri[y][x]!= 0 :
            rect(x*20,y*20,20,20,c[4])
    sleep(2)

  while True: 
    taille = 1
    s_x,s_y=5,5
    rect(0,0,x2,y2,c[2])
    rect(s_x*20,s_y*20,20,20,c[5])
    dire =  "right"
    gri = []
    sleep(0.5)
    for i in range(11):
      gri.append([])
      for j in range(16):
        gri[i].append(0)
    gri[s_y][s_x] = 1
    b_y,b_x = 5,10
    gri[b_y][b_x] = "b"
    rect(b_x*20+2,b_y*20+2,16,16,c[4])
    
    while True :
      sleep(0.3/int(setting.find("v_s"))+1)
      if ke(17):
        return True
      direc=dire
      for i in range(4):
        if ke(1)  and direc!="down":
          dire = "up"
        elif ke(2) and direc!="up":
          dire = "down"
        elif ke(0) and direc!="right":
          dire = "left"
        elif ke(3) and direc!="left":
          dire = "right"
      if dire=="up" :
        s_y-=1
      elif dire=="down" :
        s_y+=1
      elif dire=="left" :
        s_x-=1
      elif dire=="right" :
        s_x+=1
      rect(s_x*20,s_y*20,20,20,c[5])
      if s_y > 10 or s_y < 0:
        death()
        return False
      elif s_x > 15 or s_x <0 : 
        death()
        return False
      elif gri[s_y][s_x] != 0 and gri[s_y][s_x] != "b":
        death()
        return False
      if s_x == b_x and s_y == b_y :
        taille += 1
        while True:
          b_y,b_x= randint(0,10),randint(0,15)
          if gri[b_y][b_x] == 0:
            break
        rect(b_x*20+2,b_y*20+2,16,16,c[4])
        gri[b_y][b_x] = "b"
      for x in range(16):
        for y in range(11):
          if gri[y][x]!= "b":
            if gri[y][x]!= 0 :
              gri[y][x] +=1
            if gri[y][x] > taille :
              rect(x*20,y*20,20,20,c[2])
              gri[y][x] = 0
      gri[s_y][s_x] = 1
      sc_txt = ["sc","or","e:","{}".format(taille)]
      for i in range(4):
        if gri[0][6+i]== 0:
          col_txt = 2
        elif gri[0][6+i]== "b":
          col_txt = 4
        else:
          col_txt = 5
        ds(sc_txt[i],120+i*20,0,c[1],c[col_txt])
 