from kandinsky import *
from math import *
from ion import *
from time import *
from random import *

couleur = (255,180,40),(255,255,255),(0,0,0),(200,200,200),(255, 0, 0),(0, 255, 0),(0, 0, 255)
x1,y1,x2,y2 = 0,0,320,225
paramètre = {"inter":0,"adversaire":0,"nb_mine":10}

def morpion():
  global paramètre
  fill_rect(x1,y1,95,y2,couleur[0])
  fill_rect(95,y1,225,y2,couleur[1])
  score = {"x":0,"o":0,"reload":False}
  
  def draw_x(x,y):
    for i in range(35):
      fill_rect(117+i+y*72,i+x*72+20,4,4,couleur[6])
      fill_rect(117+i+y*72,-i+34+x*72+20,4,4,couleur[6])
  
  def draw_o(x0,y0,r):
    for i in range(4):
      xd=x0-int((r-i)/sqrt(2))
      xf=x0+int((r-i)/sqrt(2))
      for x in range(xd,xf+1):
        x1=x
        y1=y0+int(sqrt((r-i)**2-(x-x0)**2))
        set_pixel(x,y1,couleur[4])
        for j in range(3):
          x2=x0+y1-y0
          y2=y0+x0-x1
          set_pixel(x2,y2,couleur[4])
          x1,y1=x2,y2
  
  def case(x,y):
    for i in range(3):
      for j in range(3):
        fill_rect(117+i*72,j*72+62,38,4,couleur[1])
    fill_rect(117+y*72,x*72+62,38,4,couleur[3])
    
  def win(j): 
    for i in range(3):
      if plateau[i].count(j) == 3:
          score["reload"] = True
      if plateau[0][i] == plateau[1][i] == plateau[2][i] == j:
          score["reload"] = True
      if plateau[2][0] == plateau[1][1] == plateau[0][2] == j:
          score["reload"] = True
      if plateau[0][0] == plateau[1][1] == plateau[2][2] == j:
          score["reload"] = True
      if score["reload"] == True and j != "-" :
        score[j] += 1 
        return
    if j == "x":
      score["reload"] = True
      for i in range(3):
        for j in range(3):
          if plateau[i][j] == "-" :
            score["reload"] = False
            return
      
        
        
  fill_rect(105,y1+10,205,y2-20,couleur[2])
  while True:
    l_un = "x : ",str(score["x"])
    l_trois = "o : ",str(score["o"])
    l_1,l_3 = "",""
    for item in l_un:
      l_1 += item
    for item in l_trois:
      l_3 += item
    l_2 = "_____"
    draw_string(l_1,25,85,couleur[6],couleur[0])
    draw_string(l_2,25,105,couleur[2],couleur[0])
    draw_string(l_3,25,125,couleur[4],couleur[0])
    for i in range(3):
      for j in range(3):
        fill_rect(105+i*72,10+j*72,62,62,couleur[1])
    choix_x,choix_y= 1,1
    case(choix_x,choix_y)
    joueur = "x"
    plateau = [["-","-","-"],["-","-","-"],["-","-","-"]]
    while True:
      sleep(0.1)
      if keydown(KEY_UP):
        choix_x-=1
        if choix_x<0: 
          choix_x=2
        case(choix_x,choix_y)
      elif keydown(KEY_DOWN):
        choix_x+=1
        if choix_x>2: 
          choix_x=0
        case(choix_x,choix_y)
      if keydown(KEY_LEFT):
        choix_y-=1
        if choix_y<0: 
          choix_y=2
        case(choix_x,choix_y)
      elif keydown(KEY_RIGHT):
        choix_y+=1
        if choix_y>2: 
          choix_y=0
        case(choix_x,choix_y)
      if keydown(KEY_EXE)and plateau[choix_x][choix_y]=="-":
        plateau[choix_x][choix_y]=joueur
        if joueur == "x":
          draw_x(choix_x,choix_y)
        else:
          draw_o(choix_y*72+135,choix_x*72+40,21)
        win(joueur)
        if score["reload"]== True:
          score["reload"]= False
          sleep(1)
          break
        else:
          if paramètre["adversaire"]%3 == 0:
            while True:
              choix_y,choix_x = randint(0,2),randint(0,2)
              if plateau[choix_x][choix_y]=="-":
                sleep(1)
                plateau[choix_x][choix_y]="o"
                draw_o(choix_y*72+135,choix_x*72+40,21)
                break
          elif paramètre["adversaire"]%3 == 1:
            while True:
              choix_x,choix_y = 4,4
              play = "x"
              for playeur in range(2):
                  for x in range(3):
                      for y in range(3):
                          grille = [0,1,2]
                          del(grille[y])
                          if plateau[x][grille[0]] == plateau[x][grille[1]] == play and plateau[x][y] == "-":
                            choix_x,choix_y = x,y 
                          if plateau[grille[0]][x] == plateau[grille[1]][x] == play and plateau[y][x] == "-":
                            choix_x,choix_y = y,x 
                          if plateau[grille[0]][grille[0]] == plateau[grille[1]][grille[1]] == play and plateau[y][y] == "-":
                            choix_x,choix_y = y,y 
                  if plateau[1][1] == plateau[0][2] == play and plateau[2][0] == "-":
                    choix_x,choix_y = 2,0 
                  if plateau[1][1] == plateau[2][0] == play and plateau[0][2] == "-":
                    choix_x,choix_y = 0,2 
                  if plateau[2][0] == plateau[0][2] == play and plateau[1][1] == "-":
                    choix_x,choix_y = 1,1
                  play = "o"
              if choix_x == 4 and choix_y == 4:
                while True:
                  choix_y,choix_x = randint(0,2),randint(0,2)
                  if plateau[choix_x][choix_y]=="-":
                    break
              sleep(1)
              plateau[choix_x][choix_y]="o"
              draw_o(choix_y*72+135,choix_x*72+40,21)
              break
          elif paramètre["adversaire"]%3 == 2:
            if joueur == "x":
              joueur = "o"
            else:
              joueur = "x"
          win("o")
          if score["reload"]== True:
            score["reload"]= False
            sleep(1)
            break
      if keydown(5):
        return

def demineur():
  print("demineur")
  fill_rect(0,0,x2,y2,couleur[0])
  fill_rect(60,0,x2-60,y2,couleur[2])
  grille = [[],[],[],[],[],[],[],[],[],[],[],[]]
  decouvert = [[],[],[],[],[],[],[],[],[],[],[],[]]
  ### crée maps
  for i in range(12):
    for j in range(10):
      grille[i].append(0)
      decouvert[i].append(False)
      fill_rect(65+i*21,6+j*21,20,20,couleur[1])
  ### initialiser les mine
  for z in range(paramètre["nb_mine"]):
    while True :
      x,y = randint(0,11),randint(0,9)
      print(z,'\n',x,"\n",y,"\n",grille[x][y])
      if grille[x][y] == 0:
        grille[x][y] = "b"
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
            if grille[x__][y__] == 'b' :
              n+=1
      if grille[i][j] != 'b':
        grille[i][j] = n
    print(grille[i])
  
  def draw_case(x,y,c):
    if c == "vide":
      coul = couleur[1]
    else:
      coul = couleur[3]
    fill_rect(65+x*21,6+y*21,20,20,coul)
    if decouvert[x][y] == False:
      return
    else :
      if grille[x][y] == 0 and  c == "vide" :
        fill_rect(65+x*21,6+y*21,20,20,couleur[5])
      if grille[x][y] == 1:
        draw_string("1",65+x*21+5,6+y*21,couleur[5],coul)
      if grille[x][y] == 2:
        draw_string("2",65+x*21+5,6+y*21,couleur[6],coul)
      if grille[x][y] == 3:
        draw_string("3",65+x*21+5,6+y*21,couleur[4],coul)
      if grille[x][y] == 4:
        draw_string("4",65+x*21+5,6+y*21,couleur[2],coul)
      if grille[x][y] == "b":
        fill_rect(65+x*21,6+y*21,20,20,couleur[4])
      
  choix_x ,choix_y = 0,0
  draw_case(choix_x,choix_y,"select")
  while True:
    sleep(0.1)
    if keydown(KEY_UP):
      draw_case(choix_x,choix_y,"vide")
      choix_y-=1
      if choix_y<0: 
        choix_y=9
      draw_case(choix_x,choix_y,"select")
    elif keydown(KEY_DOWN):
      draw_case(choix_x,choix_y,"vide")
      choix_y+=1
      if choix_y>9: 
        choix_y=0
      draw_case(choix_x,choix_y,"select")
    if keydown(KEY_LEFT):
      draw_case(choix_x,choix_y,"vide")
      choix_x-=1
      if choix_x<0: 
        choix_x=11
      draw_case(choix_x,choix_y,"select")
    elif keydown(KEY_RIGHT):
      draw_case(choix_x,choix_y,"vide")
      choix_x+=1
      if choix_x>11: 
        choix_x=0
      draw_case(choix_x,choix_y,"select")
    if keydown(KEY_EXE):
      decouvert[choix_x][choix_y] = True
      draw_case(choix_x,choix_y,"select")
    if keydown(5):
      return

def pong():
  print("pong")
  return

### modifier les setting
def setting():
  global paramètre
  fill_rect(x1,y1,x2,y2,couleur[0])
  fill_rect(65,30,190,160,couleur[1])
  draw_string("morpion:",120,35,couleur[2],couleur[1])
  draw_string("demineur:",115,75,couleur[2],couleur[1])
  morpion_adver = ("bot random"),("bot ia"),("2 joueur")
  nb_mine = 10
  draw_string("mine :",70,95,couleur[2],couleur[1])
  
  def draw_sett():
    fill_rect(70,55,185,18,couleur[1])
    draw_string(morpion_adver[paramètre["adversaire"]%3],70,55,couleur[2],couleur[1])
    draw_string(str(paramètre["nb_mine"]),130,95,couleur[2],couleur[1])
    if paramètre["inter"]%2 == 0:
      draw_string(morpion_adver[paramètre["adversaire"]%3],70,55,couleur[2],couleur[3])
    elif paramètre["inter"]%2 == 1:
      draw_string(str(paramètre["nb_mine"]),130,95,couleur[2],couleur[3])
  
  while True:
    sleep(0.1)
    if keydown(KEY_LEFT):
      if paramètre["inter"]%2 == 0:  
        paramètre["adversaire"]-=1
      elif paramètre["inter"]%2 == 1 and paramètre["nb_mine"]> 10 :  
        paramètre["nb_mine"]-=1
    elif keydown(KEY_RIGHT):
      if paramètre["inter"]%2 == 0: 
        paramètre["adversaire"]+=1
      elif paramètre["inter"]%2 == 1 and paramètre["nb_mine"]< 20 :  
        paramètre["nb_mine"]+=1
    elif keydown(KEY_UP):
      paramètre["inter"]-=1
    elif keydown(KEY_DOWN):
      paramètre["inter"]+=1
    elif keydown(KEY_EXE):
      return 
    draw_sett()
        
### interaction de l'interface main
def draw_main(choix):
  draw_string("morpion",125,35,couleur[2],couleur[1])
  draw_string("demineur",120,55,couleur[2],couleur[1])
  draw_string("pong",140,75,couleur[2],couleur[1])
  draw_string("setting",125,95,couleur[2],couleur[1])
  draw_string("credit",130,115,couleur[2],couleur[1])
  draw_string("leave",135,135,couleur[2],couleur[1])
  if choix % 6 == 1:
      draw_string("morpion",125,35,couleur[2],couleur[3])
  elif choix % 6 == 2:
      draw_string("demineur",120,55,couleur[2],couleur[3])
  elif choix % 6 == 3:
      draw_string("pong",140,75,couleur[2],couleur[3])
  elif choix % 6 == 4:
      draw_string("setting",125,95,couleur[2],couleur[3])
  elif choix % 6 == 5:
      draw_string("credit",130,115,couleur[2],couleur[3])
  elif choix % 6 == 0:
      draw_string("leave",135,135,couleur[2],couleur[3])
    
### menu des jeux / setting
def main():
  global paramètre
  fill_rect(x1,y1,x2,y2,couleur[0])
  fill_rect(65,30,190,160,couleur[1])
  choix = 1
  draw_main(choix)
  while True :
    sleep(0.1)
    if keydown(KEY_UP):
      choix-=1
      draw_main(choix)
    elif keydown(KEY_DOWN):
      choix+=1
      draw_main(choix)
    if keydown(KEY_EXE):
      if choix % 6 == 1:
        morpion()
        return "main"
      elif choix % 6 == 2:
        demineur()
        return "main"
      elif choix % 6 == 3:
        pong()
        return "main"
      elif choix % 6 == 4:
        setting()
        return "main"
      elif choix % 6 == 5:
        return "ok"
      elif choix % 6 == 0:
        return "non"

### credit
def credit():
  var_credit = ""
  fill_rect(x1,y1,x2,y2,couleur[0])
  fill_rect(x1+33,y1+50,x2-65,y2-90,couleur[1])
  draw_string("[EXE]",x2-80,y2-35,couleur[1],couleur[0])
  draw_string("(Credit)",35,55,couleur[2],couleur[1])
  for r in range(50):
    for g in range(42):
      set_pixel(r+135,g,(r*5,g*5,160))
  while True :
    sleep(0.1)
    if keydown(KEY_EXE):
        return main()

var_credit=credit()

while var_credit != "non":
  if var_credit == "ok":
    var_credit=credit()
  elif var_credit == "main":
    var_credit=main()
bye+1