import pygame,sys
from pygame.locals import *
pygame.init()
cnx=80#world size Cell Number Axis
cny=60
csx=10#Cell Size Axis
csy=10
world=[[0 for y in range(cnx)] for x in range(cnx)]
#to get screen size number of cells is multiplied by cell size
screen=pygame.display.set_mode((cnx*csx,cny*csy), 0, 32)
running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:
			running=False
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	if pygame.mouse.get_pressed()[0]:
		#to get array address screen coordinate is divided by cell size
		world[mouseX//csx][mouseY//csy]+=1
	for y in range(cny):
		for x in range(cnx):
			if world[x][y]==0:
				clr=(x%255,y*10%255,x*10%255)
			else:
				clr=(world[x][y]%255,y%255,x%255)
			#to get rectangle position on screen array coordinate multiplied by cell size
			#rect defition (positionX,positionY,sizeX,sizeY)
			pygame.draw.rect(screen,clr,(csx*x,csy*y,csx,csy))
	pygame.display.update()
pygame.quit()
sys.exit()