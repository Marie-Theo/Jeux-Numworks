from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from math import *
from time import *
from random import *

x1,y1,x2,y2 = 0,0,320,225

def pong(c,para):
  rect(0,0,x2,y2,c[1])
  while True:
    e_y=y =b_y= y2//2
    b_x = x2//2
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
      if b_x > x2-x2//para["v_p"]:
        rect(x2-20,e_y-30,10,60,c[1])
        if b_x_speed > 0: 
          if b_y < e_y-20 and  e_y >30:
            e_y -= 6
          elif b_y > e_y+20 and e_y<y2-30:
            e_y += 6
        rect(x2-20,e_y-30,10,60,c[0])