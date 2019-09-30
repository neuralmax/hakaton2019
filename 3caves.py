import sys
import pygame as pg
from pygame.locals import *
from cellularcaves import makeGrid,populateGrid,automataIteration
pg.init()
cnx,cny,csx,csy=960,540,10,10#world size Cell Number Axis
#cnx,cny,csx,csy=1920,1080,1,1#laptop res

#world=[[0 for y in range(cnx)] for x in range(cnx)]
world=makeGrid(cnx,cny)
chance=40
world=populateGrid(world,chance)

#to get screen size number of cells is multiplied by cell size
screen=pg.display.set_mode((cnx*csx,cny*csy),0,32)
#screen=pg.display.set_mode((cnx*csx,cny*csy),pg.FULLSCREEN)

running=True
while running:
	for event in pg.event.get():
		if event.type==QUIT:
			running=False
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:running=False
			if event.key == pg.K_1:world=automataIteration(world,5,1)
			if event.key == pg.K_2:world=automataIteration(world,5,0)
			if event.key == pg.K_3:
				world=makeGrid(cnx,cny)
				world=populateGrid(world,chance)

				
	mouseX,mouseY=mouse=pg.mouse.get_pos()
	if pg.mouse.get_pressed()[0]:
		#to get array address screen coordinate is divided by cell size
		world[mouseX//csx][mouseY//csy]+=1
	for y in range(cny):
		for x in range(cnx):
			if world[x][y]==0:
				clr=(0,0,0)
			else:
				clr=(255,255,255)
			#to get rectangle position on screen array coordinate multiplied by cell size
			#rect defition (positionX,positionY,sizeX,sizeY)
			pg.draw.rect(screen,clr,(csx*x,csy*y,csx,csy))
	pg.display.update()
pg.quit()
sys.exit()