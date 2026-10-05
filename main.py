from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
try:from draw import *
except:raise ImportError("draw is require for this version")
x1,y1,x2,y2=0,0,320,225
para={"inter":0,"drap":0,"d_win":0,"sc_1":0,"sc_2":0,"ark":3,"ark_p":0,"adv":0,"nb_mine":15,"v_s":1,"v_p":3,"main":0,"c_txt":0}
sc={"x":0,"o":0,"reload":False}
color={"jaune":[255,181,49],"cyan":[6,150,187],"rouge":[227,35,34],"mauve":[198,35,126],"vert":[147,255,150],"rose":[224,141,172]}
click={"nb_click":0,"cl_s":0,"cl_cl":1,"reborn":0,"t":0}
c=[[255,181,49],[255,255,255],[0,0,0],[200,200,200],[255,0,0],[0,255,0],[0,0,255],[255,255,0],[255,0,255]]

games,set=[],[]
for i in ["morpion","demineur","pong","snake","arkanoid","cookie_clicker","space_invader","course_voiture"]:
  try :
    tryimport=__import__(i,None,None,"load").load()
    if tryimport!=None:set.append(tryimport)
    games.append(i)
    print("load : "+i)
  except Exception as e:print("missing : "+str(e))
del tryimport
games.append("setting")
games.append("leave")
set.append(["Main","colors:",list(color.keys()),"main"])
set.append(["Couleur","",["white on black","black on white"],"c_txt"])

setting = Options(set,65,20,190,180)

def main():
  rect(x1,y1,x2,y2,c[0])
  rect(65,(220//2-len(games)*10)-5,190,20*len(games)+10,c[1])
  menu = Carrousel(games)
  ch = menu.Choisir(c)
  for n in range(0,len(games)-2):
    if ch % len(games) == n:
      game=__import__(games[n],globals(),locals,['launch'])
      game.launch(c=c,para=para,setting=setting,sc=sc,click=click)
      return
  if ch % len(games) == len(games)-2:
    setting.launch(c)
    if setting.find("c_txt") == 0:
      c[1]=[255,255,255]
      c[2]=[0,0,0]
    else :
      c[1]=[0,0,0]
      c[2]=[255,255,255]
    c[0]= color[setting.varSelected("main")]
    return 
  elif ch % len(games) == len(games)-1:
    bye+1

while True:
  main()