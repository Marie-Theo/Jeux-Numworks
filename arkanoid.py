from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *
from draw import *

x1,y1,x2,y2 = 0,0,320,225
 

def arkanoid(c,para):
  def maps():
    for i in range(5):
      cible.append([])
      for j in range(10):
        cible[i].append(4-i)
        rect(12+30*j,10+20*i,25,15,c[4+i])

  def vie():
    rect(5,y2-8,x2-10,5,c[2])
    for i in range(para["ark"]):
      rect(5+i*15,y2-8,10,5,c[1])
  
  def win():
    for i in range(5):
      if 0 in cible[i] or 1 in cible[i] or 2 in cible[i] or 3 in cible[i] or 4 in cible[i]:
        return False
    para["ark"]+=2
    return True

  
  para["ark_p"]=0
  para["ark"]=3
  while True:
    rect(0,0,x2,y2,c[2])
    cible = []
    b_y,b_x,bar_x,bar_y = x2//2-40,y2//2+50,x2//2,y2-20
    b_y_s=randint(4,5)
    if 1== randint(1,2):
      b_x_s = randint(3,5)
    else:
      b_x_s= randint(-5,-3)
    para["ark"]-=1
    n1,n2 = True,True
  
    maps()
    vie()

    rect(b_x-5,b_y-5,10,10,c[1])
    rect(bar_x-25,bar_y,50,10,c[0])
    while True:
      sleep(0.05)
      rect(b_x-5,b_y-5,10,10,c[2])
      rect(bar_x-25,bar_y,50,5,c[0])
      b_x+=b_x_s
      b_y+=b_y_s
      rect(b_x-5,b_y-5,10,10,c[1])
      for y in range(5):
        for x in range(10):
          if cible[y][x]!=5:
            if  10+20*y-5 <= b_y <= 10+20*y+20 :
              if  12+30*x-5 <= b_x <= 12+30*x+30 :
                if (10+20*y >= b_y or b_y>= 10+20*y+15) and n1 != False:
                  b_y_s-= b_y_s*2
                  n1 = False
                elif (12+30*x >= b_x or b_x>= 12+30*x+25) and n2 != False:
                  b_x_s-= b_x_s*2
                  n2 = False
                para["ark_p"]+= (cible[y][x]+1)*10
                cible[y][x]=5
                rect(12+30*x,10+20*y,25,15,c[2])
                break
      n1,n2 = True,True
      if win():
        break
      if ke(0) and bar_x-25>5:
        rect(bar_x+20,bar_y,5,10,c[2])
        rect(bar_x-30,bar_y,5,10,c[0])
        bar_x-=5
      elif ke(3) and bar_x+25<x2-5:
        rect(bar_x-25,bar_y,5,10,c[2])
        rect(bar_x+25,bar_y,5,10,c[0])
        bar_x+=5
      if  bar_y-5 < b_y < y2-5 and b_y > 0:
        if  6 > b_x or x2-6 < b_x :
          b_x_s-= b_x_s*2
        if  bar_x-29 < b_x < bar_x+29 :
          b_y_s-= b_y_s*2
          rect(bar_x-25,bar_y,50,5,c[0])
      elif  6 > b_x or x2-6 < b_x :
        b_x_s-= b_x_s*2
      elif  6 > b_y :
        b_y_s-= b_y_s*2
      elif y2-5 < b_y :
        rect(b_x-5,b_y-5,10,10,c[4])
        if para["ark"] != 0:
          para["ark"]-=1
          sleep(0.2)
          rect(b_x-5,b_y-5,10,10,c[2])
          vie()
          rect(bar_x-25,bar_y,50,10,c[2])
          b_y,b_x,bar_x,bar_y = y2//2,x2//2,x2//2,y2-20
          rect(bar_x-25,bar_y,50,10,c[0])
          b_y_s=randint(4,5)
          if 1== randint(1,2):
            b_x_s = randint(3,5)
          else:
            b_x_s= randint(-5,-3)
        else:
          sleep(0.5)
          para["ark"]=3
          ch = 0
          rect(x2//2-60,y2//2-25,120,47,c[0])
          menu = Carrousel(["recommencer","leave"])
          ch = menu.Choisir()
          if ch % 2 ==0:
            para["ark_p"]=0
            break
          if ch % 2 ==1:
            return
      if ke(17):
        return