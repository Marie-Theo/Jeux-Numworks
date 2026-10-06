from kandinsky import fill_rect as rect , draw_string as ds,set_pixel as sp
from ion import keydown as ke
from time import sleep, monotonic
from random import randint as rng
def load():return ["Course voiture","vitesse * ",["1","2","3"],"car_racing"]
if __name__ == "__main__":print("require main and draw from https://my.numworks.com/python/tmarie")
bordure = 0
## couleur
color={"vert":[39, 140, 0],"jaune":[255, 255, 0],"blanc":[255, 255, 255],"cyan":[0, 255, 255],"rouge":[255, 0, 0],"bleu" :[0, 152, 255],"gris":[50,50,60],"noir":[0,0,0]}

def launch(c,setting,click=None,para=None,sc=None):
	tempcol=list(color.values())
	tempcol=tempcol[:4]
	tempcol.insert(0,c[0])

	## voiture enemie
	def enemie(piste):
		for i in range(3,-1,-1):
			for j in range(3,-1,-1):
				if piste[i][j] != 1 and piste[i][j] != 0 :
					if i != 3:
						piste[i+1][j] = piste[i][j]
					piste[i][j]=0
		if 2 not in (piste[0][:3] or piste[1][:3]):
			piste[0][rng(0,4)] =rng(2,len(tempcol))
		course(piste)

	## graphisme
	def course(piste):
		for i in range(4):
			for j in range(4):
				if piste[i][j] == 0:
					if i == 0 :
						rect(85+38*j,50, 40, 40,color["bleu"])
						rect(85+38*j,90, 30, 10,color["gris"])
					else: 
						rect(85+38*j,55+40*i, 30, 40,color["gris"])
				for ncol in range(1,len(tempcol)+1):
					if piste[i][j] == ncol:
						rect(85+38*j,55+40*i, 30, 40,tempcol[ncol-1])
						break

	## animation
	def anime():
			global bordure
			for pos in (60,240):
				rect(pos,70, 20, 160,color['blanc'])
				rect(pos,100+1*bordure, 20, 30,color['rouge'])
				rect(pos,160+1*bordure, 20, 30,color['rouge'])
			if 0 <= bordure <= 30 :
				rect(60,70, 20, 0+1*bordure,color['rouge'])
				rect(240,70, 20, 0+1*bordure,color['rouge'])
			elif 30 <= bordure <= 60:
				rect(60,40+1*bordure, 20, 30,color['rouge'])
				rect(240,40+1*bordure, 20, 30,color['rouge'])
			bordure=(bordure+1)%60

	def tourner(direc,piste):
		for i in range(4):
			if 0<=i+direc<=3 and piste[3][i+direc] == 0 and 1 == piste[3][i] :
				piste[3][i]=0
				piste[3][i+direc]=1
				course(piste)
				sleep(0.1)
				return

	while True:
		piste=[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0]
		score = 0
		rect(0,0, 320, 240,color["bleu"])
		rect(0,90, 320, 240,color["vert"])
		rect(80,90, 160, 140,color["gris"])
		anime()
		course(piste)
		while True:
			score =int(score)+1
			text_score = "score: "+str(score)
			ds(text_score,10,10,color["noir"],color["bleu"])
			debut=monotonic()
			while (monotonic() - debut) < 0.6 / int(setting.find("car_racing")+1):
				if ke(17):return
				elif ke(0):
					tourner(-1,piste)
				elif ke(3):
					tourner(1,piste)
				sleep(0.05)
				anime()
			enemie(piste)
			if 1 not in piste[3] :
				break
		## GAME OVER
		rect(50,40, 220, 140,c[2])
		ds("GAME OVER",110,80,c[1],c[2])
		text_score = "score : "+str(score)
		ds(text_score,110,120,c[1],c[2])
		while not ke(4) and not ke(52):
			if ke(17):return