from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *

c = (255,180,40),(255,255,255),(0,0,0),(200,200,200),(255, 0, 0),(0, 255, 0),(0, 0, 255)
x1,y1,x2,y2 = 0,0,320,225
para = {"inter":0,"adv":0,"nb_mine":15,"drap":0,"d_win":0,"sc_1":0,"sc_2":0,"v_snake":1,"v_pong":3,"main":1,"co_txt":1}
m_adver = ("bot random"),("bot ia"),("2 j")

def morpion():
  global para
  rect(x1,y1,95,y2,c[0])
  rect(95,y1,225,y2,c[1])
  sc = {"x":0,"o":0,"reload":False}
  
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
    ch_x,ch_y= 1,1
    case(ch_x,ch_y)
    j = "x"
    pla = [["-","-","-"],["-","-","-"],["-","-","-"]]
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
      if ke(3):
        ch_y-=1
        if ch_y<0: 
          ch_y=2
        case(ch_x,ch_y)
      elif ke(0):
        ch_y+=1
        if ch_y>2: 
          ch_y=0
        case(ch_x,ch_y)
      if ke(52)and pla[ch_x][ch_y]=="-":
        pla[ch_x][ch_y]=j
        if j == "x":
          draw_x(ch_x,ch_y)
        else:
          draw_o(ch_y*72+135,ch_x*72+40,21)
        win(j)
        if sc["reload"]== True:
          sc["reload"]= False
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
              ch_x,ch_y = 4,4
              play = "x"
              for playeur in range(2):
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

def demineur():
  rect(0,0,x2,y2,c[0])
  rect(60,0,x2-60,y2,c[2])
  
  while True:
    gri = [[],[],[],[],[],[],[],[],[],[],[],[]]
    decouvert = [[],[],[],[],[],[],[],[],[],[],[],[]]
    ### crée maps
    for i in range(12):
      for j in range(10):
        gri[i].append(0)
        decouvert[i].append(False)
        rect(65+i*21,6+j*21,20,20,c[1])
    ### initialiser les mine
    for z in range(para["nb_mine"]):
      while True :
        x,y = randint(0,11),randint(0,9)
        print(z,'\n',x,"\n",y,"\n",gri[x][y])
        if gri[x][y] == 0:
          gri[x][y] = "b"
          break
    ### definir le nb de mine autour
    for i in range(12):
      for j in range(10):
        n = 0
        for x_ in range(3):
          x__=i+1-x_
          for y_ in range(3):
            y__= j+1-y_
            if 0 <=x__<= 11 and 0<= y__ <= 9 :
              if gri[x__][y__] == 'b' :
                n+=1
        if gri[i][j] != 'b':
          gri[i][j] = n
      print(gri[i])
    
    ### enlever tous les 0 autour
    def decouvrir():
      for z in range(2):
        for i in range(12):
          for j in range(10):
            for x_ in range(3):
              x__=i+1-x_
              for y_ in range(3):
                y__= j+1-y_
                if 0 <=x__<= 11 and 0<= y__ <= 9 :
                  if gri[x__][y__] == 0 and decouvert[i][j] == True:
                    decouvert[x__][y__] = True
                    draw_case(x__,y__,"other")
    
    def draw_drap(x,y):
      rect(x,y-4,1,15,c[2])
      for l in range(9):
        for j in range(l):
          sp(x-l+9,y-j+4,c[4])
    
    def draw_case(x,y,c):
      if c =="draw_drap":
        draw_drap(30,10)
        return
      if c == "vide":
        coul = c[1]
      elif c == "other":
        rect(65+x*21,6+y*21,20,20,c[5])
        return
      else:
        coul = c[3]
      rect(65+x*21,6+y*21,20,20,coul)
      if decouvert[x][y] == False:
        return
      elif decouvert[x][y] == "drap" :
        draw_drap(70+x*21,11+y*21)
      else :
        if gri[x][y] == 0 and  c == "vide" :
          rect(65+x*21,6+y*21,20,20,c[5])
        elif gri[x][y] == 1:
          ds("1",65+x*21+5,6+y*21,c[5],coul)
        elif gri[x][y] == 2:
          ds("2",65+x*21+5,6+y*21,c[6],coul)
        elif gri[x][y] == 3:
          ds("3",65+x*21+5,6+y*21,c[0],coul)
        elif gri[x][y] == 4:
          ds("4",65+x*21+5,6+y*21,c[4],coul)
        elif gri[x][y] == 5:
          ds("5",65+x*21+5,6+y*21,c[2],coul)
        elif gri[x][y] == "b":
          rect(65+x*21,6+y*21,20,20,c[4])
    
    def d_win(): 
      drap_bon = 0
      for x in range(12):
        for y in range(10):
          if gri[x][y] == "mine" and decouvert[x][y] == "drap":
            drap_bon += 1
      if para["nb_mine"] == drap_bon:
        para["d_win"] += 1
        return True
      
    ch_x ,ch_y = 0,0
    draw_case(ch_x,ch_y,"select")
    para["drap"]=0
    draw_case(0,0,"draw_drap")
    ds("{} win".format(para["d_win"]),5,40,c[2],c[0])
    while True:
      rect(10,20,50,20,c[0])
      ds("{}/{}".format(para["drap"],para["nb_mine"]),10,20,c[2],c[0])
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
      if ke(3):
        draw_case(ch_x,ch_y,"vide")
        ch_x-=1
        if ch_x<0: 
          ch_x=11
        draw_case(ch_x,ch_y,"select")
      elif ke(0):
        draw_case(ch_x,ch_y,"vide")
        ch_x+=1
        if ch_x>11: 
          ch_x=0
        draw_case(ch_x,ch_y,"select")
      if ke(52) and decouvert[ch_x][ch_y] == False:
        decouvert[ch_x][ch_y] = True
        draw_case(ch_x,ch_y,"select")
        if gri[ch_x][ch_y] == "b":
          for x in range(12):
            for y in range(10):
              decouvert[x][y] = True
              draw_case(x,y,"vide")
          sleep(3)
          break
        elif gri[ch_x][ch_y] == 0:
          decouvrir()
      if ke(4) :
        if decouvert[ch_x][ch_y] == False and para["nb_mine"] > para["drap"]:
          decouvert[ch_x][ch_y] = "drap"
          para["drap"]+=1
        elif decouvert[ch_x][ch_y] == "drap":
          decouvert[ch_x][ch_y] = False
          para["drap"]-=1
        draw_case(ch_x,ch_y,"select")
      if para["nb_mine"] == para["drap"]:
        win = d_win() 
        if win == True :
          break
      if ke(17):
        return

def pong():
  rect(0,0,x2,y2,c[1])
  while True:
    e_y=y =b_y= y2//2
    b_x, = x2//2
    b_x_speed, b_y_speed= randint(3,7),randint(3,7)
    rect(0,0,20,y2,c[1])
    rect(x2-20,0,20,y2,c[1])
    rect(10,y-30,10,60,c[0])
    rect(x2-20,e_y-30,10,60,c[0])
    while True:
      sleep(0.05)
      ds("{} / {}".format(para["sc_1"],para["sc_2"]),x2//2-25,20,c[2],c[1])
      rect(b_x-5,b_y-5,10,10,c[1])
      b_x+=b_x_speed
      b_y+=b_y_speed
      rect(b_x-5,b_y-5,10,10,c[0])
      if ke(1) and y >30:
        rect(10,y-30,10,60,c[1])
        y -= 5
        rect(10,y-30,10,60,c[0])
      elif ke(2)and y<y2-30:
        rect(10,y-30,10,60,c[1])
        y += 5
        rect(10,y-30,10,60,c[0])
      if ke(17):
        return
      if  b_y >= y2-5 :
        b_y_speed-= b_y_speed*2
      elif b_y <= 5 :
        b_y_speed-= b_y_speed*2
      elif y-30<b_y<y+30 and 15<b_x<=25 :
        b_x_speed-= b_x_speed*2
        b_x = 25
      elif e_y-30<b_y<e_y+30 and x2-15> b_x >= x2-25:
        b_x_speed-= b_x_speed*2
        b_x = x2-25
      if x2-5 <= b_x :
        para["sc_1"]+=1
        break
      elif b_x <= 5:
        para["sc_2"]+=1
        break
      if b_x > x2-x2//para["v_pong"]:
        rect(x2-20,e_y-30,10,60,c[1])
        if b_y < e_y-20 and  e_y >30:
          e_y -= 6
        elif b_y > e_y+20 and e_y<y2-30:
          e_y += 6
        rect(x2-20,e_y-30,10,60,c[0])

def snake():
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
      sleep(0.3/para["v_snake"])
      if ke(17):
        return True
      direc=dire
      for i in range(4):
        if ke(1)  and direc!="down":
          dire = "up"
        elif ke(2) and direc!="up":
          dire = "down"
        elif ke(3) and direc!="right":
          dire = "left"
        elif ke(0) and direc!="left":
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
      print(s_y,s_x)
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
            
### modifier les setting
def setting():
  global para,m_adver
  def d_sett_1():
    rect(x1,y1,x2,y2,c[0])
    rect(65,20,190,180,c[1])
    rect(240,25,10,170,(200,200,200))
    rect(240,25,10,85,(100,100,100))
    ds("morpion:",120,25,c[2],c[1])
    ds("demineur:",115,65,c[2],c[1])
    ds("snake:",130,105,c[2],c[1])
    ds("pong:",135,145,c[2],c[1])
    ds("mine :",70,85,c[2],c[1])

  def d_sett_2():
    rect(65,20,190,180,c[1])
    rect(240,25,10,170,(200,200,200))
    rect(240,110,10,85,(100,100,100))
    ds("main colors:",100,25,c[2],c[1])
    ds("black/wite:",105,65,c[2],c[1])

  def draw_sett():
    if para["inter"]%6 < 4:
      d_sett_1()
      rect(70,45,100,18,c[1])
      ds(m_adver[para["adv"]%3],70,45,c[2],c[1])
      ds(str(para["nb_mine"]),130,85,c[2],c[1])
      ds("vitesse * {}".format(para["v_snake"]),70,125,c[2],c[1])
      rect(70,165,170,18,c[1])
      if para["v_pong"] == 4:
        ds("dificulter easy",70,165,c[2],c[1])
      elif para["v_pong"] == 3:
        ds("dificulter normal",70,165,c[2],c[1])
      elif para["v_pong"] == 2:
        ds("dificulter hard",70,165,c[2],c[1])
      if para["inter"]%6 == 0:
        ds(m_adver[para["adv"]%3],70,45,c[2],c[3])
      elif para["inter"]%6 == 1:
        rect(130,85,20,18,c[1])
        ds(str(para["nb_mine"]),130,85,c[2],c[3])
      elif para["inter"]%6 == 2:
        ds("vitesse * {}".format(para["v_snake"]),70,125,c[2],c[3])
      elif para["inter"]%6 == 3:
        if para["v_pong"] == 4:
          ds("dificulter easy",70,165,c[2],c[3])
        elif para["v_pong"] == 3:
          ds("dificulter normal",70,165,c[2],c[3])
        elif para["v_pong"] == 2:
          ds("dificulter hard",70,165,c[2],c[3])
    else:
      d_sett_2()
      if para["inter"]%6 == 4:
        ds(m_adver[para["adv"]%3],70,45,c[2],c[3])
      elif para["inter"]%6 == 5:
        ds(str(para["nb_mine"]),70,85,c[2],c[3])

  while True:
    sleep(0.1)
    if ke(3):
      if para["inter"]%6 == 0:  
        para["adv"]-=1
      elif para["inter"]%6 == 1 and para["nb_mine"]> 1 :  
        para["nb_mine"]-=1
      elif para["inter"]%6 == 2 and para["v_snake"]> 1 :  
        para["v_snake"]-=1
      elif para["inter"]%6 == 3 and para["v_pong"]< 4 :
        para["v_pong"]+=1
      elif para["inter"]%6 == 4:
        para["main"]-=1
      elif para["inter"]%6 == 5 and para["co_txt"] > 1:
        para["co_txt"]-=1
    elif ke(0):
      if para["inter"]%6 == 0: 
        para["adv"]+=1
      elif para["inter"]%6 == 1 and para["nb_mine"]< 30 :  
        para["nb_mine"]+=1
      elif para["inter"]%6 == 2 and para["v_snake"]< 3 :  
        para["v_snake"]+=1
      elif para["inter"]%6 == 3 and para["v_pong"]> 2 :
        para["v_pong"]-=1
      elif para["inter"]%6 == 4:
        para["main"]+=1
      elif para["inter"]%6 == 5 and para["co_txt"] < 2:
        para["co_txt"]+=1
    elif ke(1):
      para["inter"]-=1
    elif ke(2):
      para["inter"]+=1
    elif ke(52):
      return 
    draw_sett()

### interaction de l'interface main
def draw_main(ch):
  ds("morpion",125,35,c[2],c[1])
  ds("demineur",120,55,c[2],c[1])
  ds("pong",140,75,c[2],c[1])
  ds("snake",135,95,c[2],c[1])
  ds("setting",125,115,c[2],c[1])
  ds("credit",130,135,c[2],c[1])
  ds("leave",135,155,c[2],c[1])
  if ch % 7 == 1:
      ds("morpion",125,35,c[2],c[3])
  elif ch % 7 == 2:
      ds("demineur",120,55,c[2],c[3])
  elif ch % 7 == 3:
      ds("pong",140,75,c[2],c[3])
  elif ch % 7 == 4:
     ds("snake",135,95,c[2],c[3])
  elif ch % 7 == 5:
      ds("setting",125,115,c[2],c[3])
  elif ch % 7 == 6:
      ds("credit",130,135,c[2],c[3])
  elif ch % 7 == 0:
      ds("leave",135,155,c[2],c[3])
    
### menu des jeux / setting
def main():
  global para
  rect(x1,y1,x2,y2,c[0])
  rect(65,30,190,160,c[1])
  ch = 1
  draw_main(ch)
  while True :
    sleep(0.1)
    if ke(1):
      ch-=1
      draw_main(ch)
    elif ke(2):
      ch+=1
      draw_main(ch)
    if ke(52):
      if ch % 7 == 1:
        morpion()
        return
      elif ch % 7 == 2:
        demineur()
        return
      elif ch % 7 == 3:
        pong()
        return
      elif ch % 7 == 4:
        fin = False
        while fin != True :
          fin = snake()
        return
      elif ch % 7 == 5:
        setting()
        if para["co_txt"] == 1:
          c[1],c[2]= (255,255,255),(0,0,0)
        else :
          c[1],c[2] = (0,0,0),(255,255,255)
        return 
      elif ch % 7 == 6:
        credit()
        return
      elif ch % 7 == 0:
        return "non"
"""
### credit
def credit():
  rect(x1,y1,x2,y2,c[0])
  rect(x1+33,y1+50,x2-65,y2-90,c[1])
  ds("[EXE]",x2-80,y2-35,c[1],c[0])
  ds("(Credit)",35,55,c[2],c[1])
  for r in range(50):
    for g in range(42):
      sp(r+135,g,(r*5,g*5,160))
  while True :
    sleep(0.1)
    if ke(52):
        return main()
"""
var_credit=main()

while var_credit != "non":
  var_credit=main()
bye+1