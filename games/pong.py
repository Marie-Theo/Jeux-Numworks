from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from time import sleep
from random import randint
def load():return ["Pong","niveaux ",["easy","normal","hard"],"v_p",1]

w,h = 320,225

def launch(c,para,setting,sc=None,click=None):
  rect(0,0,w,h,c[2])
  while True:
    e_y=y =b_y= h//2
    b_x = w//2
    b_x_speed, b_y_speed= randint(3,7),randint(3,7)
    rect(0,0,20,h,c[2])
    rect(w-20,0,20,h,c[2])
    rect(10,y-30,10,60,c[0])
    rect(w-20,e_y-30,10,60,c[0])
    while True:
      sleep(0.05)
      ds("{} / {}".format(para["sc_1"],para["sc_2"]),w//2-25,20,c[1],c[2])
      rect(b_x-5,b_y-5,10,10,c[2])
      b_x+=b_x_speed
      b_y+=b_y_speed
      rect(b_x-5,b_y-5,10,10,c[0])
      if ke(1) and y >30:
        rect(10,y-30,10,60,c[2])
        y -= 5
        rect(10,y-30,10,60,c[0])
      elif ke(2)and y<h-30:
        rect(10,y-30,10,60,c[2])
        y += 5
        rect(10,y-30,10,60,c[0])
      if ke(17):
        return
      if  b_y >= h-5 :
        b_y_speed-= b_y_speed*2
      elif b_y <= 5 :
        b_y_speed-= b_y_speed*2
      elif y-30<b_y<y+30 and 15<b_x<=25 :
        b_x_speed-= b_x_speed*2
        b_x = 25
      elif e_y-30<b_y<e_y+30 and w-15> b_x >= w-25:
        b_x_speed-= b_x_speed*2
        b_x = w-25
      if w-5 <= b_x :
        para["sc_1"]+=1
        break
      elif b_x <= 5:
        para["sc_2"]+=1
        break
      if b_x > w-w//int(setting.find("v_p")+1):
        rect(w-20,e_y-30,10,60,c[2])
        if b_x_speed > 0: 
          if b_y < e_y-20 and  e_y >30:
            e_y -= 6
          elif b_y > e_y+20 and e_y<h-30:
            e_y += 6
        rect(w-20,e_y-30,10,60,c[0])