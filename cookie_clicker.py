from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
x1,y1,x2,y2 = 0,0,320,225
cookie = [[0,0,0,1,1,1,0,0,0],[0,1,1,1,2,1,1,1,0],[0,1,1,1,1,1,1,2,0],[1,2,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,2,1],[0,2,1,2,1,1,1,1,0],[0,1,1,1,1,1,2,1,0],[0,0,0,1,1,1,0,0,0],(228,141,74),(105,30,0)]

def cookie_clicker(c,click):
  global t1,pt1

  def loop():
    n = 100000
    while True:
      if click["nb_click"]>=t1*n:
        click["nb_click"]-=t1*n
        click["cl_s"]+=pt1*n
      elif n != 1:
        n/=10
      else:
        rect(0,y2-20,x2//3,20,c[0])
        ds("{}".format(num(int(click["nb_click"]))),5,y2-20,c[2],c[0])
        ds("+{}/s".format(num(click["cl_s"])),x2//3+5,y2-20,c[2],c[1])
        break
    
  def num(n):
    d_n = ["k","m","M","T"]
    for x in range(4,0,-1):
      if n >= int("1"+'000'*x):
        return str(round(n/int("1"+'000'*x),2))+d_n[x-1]
    return n

  def graf():
    rect(0,0,x2,y2,c[0])
    rect(x2//3,0,(x2//3)*2+1,y2,c[1])
    ds("clicker",10,10,c[2],c[0])
    ds("buy",10,30,c[2],c[0])
    ds("reborn",10,50,c[2],c[0])
    ds("stats",10,70,c[2],c[0])
    ds("{}".format(num(click["nb_click"])),5,y2-20,c[2],c[0])
    ds("+{}/s".format(num(click["cl_s"])),x2//3+5,y2-20,c[2],c[1])
    d_main()

  def d_buy(ch):
    ds("cookie par seconde:",x2//3,5,c[2],c[1])
    ds("cookie par click:",x2//3,145,c[2],c[1])
    ds("{} --> {}+1".format(15*((1+click["reborn"])*click["cl_cl"]),click["cl_cl"]),x2//3,165,c[2],c[1])
    ds("{} --> {}+10".format(150*((1+click["reborn"])*click["cl_cl"]),click["cl_cl"]),x2//3,185,c[2],c[1])
    for i in range(6):
      ds("{} --> {} /s".format(num(t1*int("1"+'0'*i)),num(pt1*int("1"+'0'*i))),x2//3,25+20*i,c[2],c[1])
    ds("return",x2-60,y2-20,c[2],c[1])
    if ch != "no":
      for j in range(6):
        if ch % 9 == j+1:
          ds("{} --> {} /s".format(num(t1*int("1"+'0'*j)),num(pt1*int("1"+'0'*j))),x2//3,25+20*j,c[2],c[3])
      if ch % 9 == 7:
        ds("{} --> {}+1".format(15*((1+click["reborn"])*click["cl_cl"]),click["cl_cl"]),x2//3,165,c[2],c[3])
      elif ch % 9 == 8:
        ds("{} --> {}+10".format(150*((1+click["reborn"])*click["cl_cl"]),click["cl_cl"]),x2//3,185,c[2],c[3])
      elif ch % 9 == 0:
        ds("return",x2-60,y2-20,c[2],c[3])
  
  def d_reborn(ch):
    ds("cost:",x2//3+5,5,c[2],c[1])
    ds("{}".format(num(1000000*int("1"+click["reborn"]*"0"))),x2//3+5,25,c[2],c[1])
    ds("reset",x2//3+5,45,c[2],c[1])
    ds("for:",x2//3+5,70,c[2],c[1])
    ds("{}+1 reborn".format(click["reborn"]),x2//3+5,90,c[2],c[1])
    ds("return",x2-60,y2-20,c[2],c[1])
    if ch != "no":
      if ch % 2 == 1:
        ds("{}".format(num(1000000*int("1"+click["reborn"]*"0"))),x2//3+5,25,c[2],c[3])
        ds("reset",x2//3+5,45,c[2],c[3])
        ds("{}+1 reborn".format(click["reborn"]),x2//3+5,90,c[2],c[3])
      elif ch % 2 == 0:
        ds("return",x2-60,y2-20,c[2],c[3])
  
  def buy():
    ch=0
    d_buy(ch)
    while True:
      if ke(1):
        ch-=1
        d_buy(ch)
        while ke(1) :
          continue
      elif ke(2):
        ch+=1
        d_buy(ch)
        while ke(2) :
          continue
      elif ke(48):
        loop()
      if ke(4) :
        sleep(0.15)
        if ch%9==0:
          return False
        d_n = 1
        for i in range(6):
          if ch%9== i+1 and click["nb_click"]>=t1*d_n:
            click["nb_click"]-=t1*d_n
            click["cl_s"]+=pt1*d_n
          elif d_n != 1000000:
            d_n*=10
          else:
            break
        for j in range(2):
          if ch%9==7+j and click["nb_click"]>=int('1'+'0'*j)*15*((1+click["reborn"])*click["cl_cl"]):
            click["nb_click"]-=int('1'+'0'*j)*15*((1+click["reborn"])*click["cl_cl"])
            click["cl_cl"]+=int('1'+'0'*j)*1
            ds("{} --> {}+{}".format(num(int('1'+'0'*j)*15*((1+click["reborn"])*click["cl_cl"])),num(click["cl_cl"]),1*(10*j)),x2//3,165+20*j,c[2],c[3])
        rect(0,y2-20,x2//3,20,c[0])
        ds("{}".format(num(int(click["nb_click"]))),5,y2-20,c[2],c[0])
        ds("+{}/s".format(num(click["cl_s"])),x2//3+5,y2-20,c[2],c[1])
        d_buy(ch)
      if ke(17):
        return True

  def reborn():
    global t1,pt1
    ch = 0
    ds("return",x2-60,y2-20,c[2],c[3])
    while True:
      if ke(1):
        ch-=1
        d_reborn(ch)
        while ke(1) :
          continue
      elif ke(2):
        ch+=1
        d_reborn(ch)
        while ke(2) :
          continue
      if ke(4) :
        if ch%2==0:
          return False
        if ch%2==1:
          if click["nb_click"]>=1000000*int("1"+click["reborn"]*"0"):
            click["nb_click"]=0
            click["cl_s"]=0
            click["cl_cl"]=1
            click["reborn"]+=1
            t1 = 10*(1+click["reborn"]*0.5)
            pt1= 0.5*(click["reborn"]+1)
            ch= 2
            graf()
      if ke(17):
        return True

  def d_main():
    if ch % 4 == 0:
      ds("clicker",10,10,c[2],c[3])
      ds("+{} *{}(reborn)".format(num(click["cl_cl"]),1+click["reborn"]),x2//3*2-75,30,c[2],c[1])
      for x in range(9):
        for y in range(9):
          if cookie[x][y] == 0:
            continue
          elif cookie[x][y] == 1:
            rect(x*15+145,y*15+65,15,15,cookie[9])
          elif cookie[x][y] == 2:
            rect(x*15+145,y*15+65,15,15,cookie[10])
    elif ch % 4 == 1:
      ds("buy",10,30,c[2],c[3])
      d_buy("no")
    elif ch % 4 == 2:
      ds("reborn",10,50,c[2],c[3])
      d_reborn("no")
    elif ch % 4 == 3:
      ds("stats",10,70,c[2],c[3])
      if click["cl_s"] != 0:
        ds("for buy :",x2//3,5,c[2],c[1])
        for i in range(6):
          ds("t{} {} /s".format(i+1,round(1/(int("1"+"0"*(i+1))*(1+click["reborn"]*0.5)/click["cl_s"]),2)),x2//3,25+20*i,c[2],c[1])
      else:
        ds("stats non visionable",x2//3,y2//2-30,c[2],c[1])
        ds("pour le moment",x2//3,y2//2-10,c[2],c[1])

  ####### main
  ch = 0
  graf()
  t1 = 10*(1+click["reborn"]*0.5)
  pt1= 0.5*(1+click["reborn"])

  while True:
    sleep(0.05)
    if (int(monotonic())-int(click["t"])) >= 1:
      click["nb_click"]+=round(click["cl_s"]*round(monotonic()-click["t"]),2)
      click["t"] = monotonic()
      round(click["nb_click"],2)
      rect(0,y2-20,x2//3,20,c[0])
      if int(click["nb_click"]) == click["nb_click"]-0.5:
        ds("{}".format(num(round(click["nb_click"],2))),5,y2-20,c[2],c[0])
      else:
        ds("{}".format(num(int(click["nb_click"]))),5,y2-20,c[2],c[0])
    if ke(1):
      ch-=1
      graf()
      while ke(1) :
        continue
    elif ke(2):
      ch+=1
      graf()
      while ke(2) :
        continue
    if ke(4) :
      while ke(4) :
        continue
      if ch % 4==0:
        click["nb_click"]+=click["cl_cl"]*(1+click["reborn"])
        if int(click["nb_click"]) == click["nb_click"]-0.5:
          ds("{}".format(num(round(click["nb_click"],2))),5,y2-20,c[2],c[0])
        else:
          ds("{}".format(num(int(click["nb_click"]))),5,y2-20,c[2],c[0])
      elif ch % 4==1:
        r = buy()
        if r == True:
          return
        graf()
      elif ch % 4==2:
        r =reborn()
        if r == True:
          return
        graf()
      while ke(4) :
        continue
    if ke(17):
      return