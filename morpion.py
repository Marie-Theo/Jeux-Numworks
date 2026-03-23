from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *

x1,y1,x2,y2 = 0,0,320,225

def morpion(c,para,m_adver,sc):
  rect(x1,y1,95,y2,c[0])
  rect(95,y1,225,y2,c[1])

  def draw_x(x,y):
    for i in range(35):
      rect(117+i+y*72,i+x*72+20,4,4,c[6])
      rect(117+i+y*72,-i+34+x*72+20,4,4,c[6])

  def draw_o(x0,y0,r):
    for i in range(4):
      xd=x0-int((r-i)/sqrt(2))
      xf=x0+int((r-i)/sqrt(2))
      for x in range(xd,xf+1):
        x1=x
        y1=y0+int(sqrt((r-i)**2-(x-x0)**2))
        sp(x,y1,c[4])
        for j in range(3):
          x2=x0+y1-y0
          y2=y0+x0-x1
          sp(x2,y2,c[4])
          x1,y1=x2,y2

  def case(x,y):
    for i in range(3):
      for j in range(3):
        rect(117+i*72,j*72+62,38,4,c[1])
    rect(117+y*72,x*72+62,38,4,c[3])

  def win(j): 
    for i in range(3):
      if pla[i].count(j) == 3:
          sc["reload"] = True
      if pla[0][i] == pla[1][i] == pla[2][i] == j:
          sc["reload"] = True
      if pla[2][0] == pla[1][1] == pla[0][2] == j:
          sc["reload"] = True
      if pla[0][0] == pla[1][1] == pla[2][2] == j:
          sc["reload"] = True
      if sc["reload"] == True and j != "-" :
        sc[j] += 1 
        return
    if j == "x":
      sc["reload"] = True
      for i in range(3):
        for j in range(3):
          if pla[i][j] == "-" :
            sc["reload"] = False
            return
        
  rect(105,y1+10,205,y2-20,c[2])
  while True:
    l_un = "x : ",str(sc["x"])
    l_trois = "o : ",str(sc["o"])
    l_1,l_3 = "",""
    for it in l_un:
      l_1 += it
    for it in l_trois:
      l_3 += it
    l_2 = "_____"
    ds(l_1,25,85,c[6],c[0])
    ds(l_2,25,105,c[2],c[0])
    ds(l_3,25,125,c[4],c[0])
    for i in range(3):
      for j in range(3):
        rect(105+i*72,10+j*72,62,62,c[1])
    ch_x,ch_y,j,pla= 1,1,"x",[["-","-","-"],["-","-","-"],["-","-","-"]]
    case(ch_x,ch_y)
    while True:
      sleep(0.1)
      if ke(1):
        ch_x-=1
        if ch_x<0: 
          ch_x=2
        case(ch_x,ch_y)
      elif ke(2):
        ch_x+=1
        if ch_x>2: 
          ch_x=0
        case(ch_x,ch_y)
      if ke(0):
        ch_y-=1
        if ch_y<0: 
          ch_y=2
        case(ch_x,ch_y)
      elif ke(3):
        ch_y+=1
        if ch_y>2: 
          ch_y=0
        case(ch_x,ch_y)
      if ke(4)and pla[ch_x][ch_y]=="-":
        pla[ch_x][ch_y]=j
        if j == "x":
          draw_x(ch_x,ch_y)
        else:
          draw_o(ch_y*72+135,ch_x*72+40,21)
        win(j)
        if sc["reload"]==True:
          sc["reload"]=False
          sleep(1)
          break
        else:
          if para["adv"]%3 == 0:
            while True:
              ch_y,ch_x = randint(0,2),randint(0,2)
              if pla[ch_x][ch_y]=="-":
                sleep(1)
                pla[ch_x][ch_y]="o"
                draw_o(ch_y*72+135,ch_x*72+40,21)
                break
          elif para["adv"]%3 == 1:
            while True:
              ch_x,ch_y,play = 4,4,"x"
              for p in range(2):
                  for x in range(3):
                      for y in range(3):
                          gri = [0,1,2]
                          del(gri[y])
                          if pla[x][gri[0]] == pla[x][gri[1]] == play and pla[x][y] == "-":
                            ch_x,ch_y = x,y 
                          if pla[gri[0]][x] == pla[gri[1]][x] == play and pla[y][x] == "-":
                            ch_x,ch_y = y,x 
                          if pla[gri[0]][gri[0]] == pla[gri[1]][gri[1]] == play and pla[y][y] == "-":
                            ch_x,ch_y = y,y 
                  if pla[1][1] == pla[0][2] == play and pla[2][0] == "-":
                    ch_x,ch_y = 2,0 
                  if pla[1][1] == pla[2][0] == play and pla[0][2] == "-":
                    ch_x,ch_y = 0,2 
                  if pla[2][0] == pla[0][2] == play and pla[1][1] == "-":
                    ch_x,ch_y = 1,1
                  play = "o"
              if ch_x == 4 and ch_y == 4:
                while True:
                  ch_y,ch_x = randint(0,2),randint(0,2)
                  if pla[ch_x][ch_y]=="-":
                    break
              sleep(1)
              pla[ch_x][ch_y]="o"
              draw_o(ch_y*72+135,ch_x*72+40,21)
              break
          elif para["adv"]%3 == 2:
            if j == "x":
              j = "o"
            else:
              j = "x"
          win("o")
          if sc["reload"]== True:
            sc["reload"]= False
            sleep(1)
            break
      if ke(17):
        return