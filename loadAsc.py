import pygame, sys
from random import randint
from pygame.locals import *
pygame.init()

#arr=[]
def loadAsc(fname):
	world=[]
	file=[]
	szx=0
	szy=0
	with open(fname,'r') as f:
		for line in f:
			file.append(line.rstrip())
	for l in file:
		larr=l.split(' ')
		#print(larr)
		if larr[0]=='ncols':szx=int(larr[-1])
		elif larr[0]=='nrows':szy=int(larr[-1])
		elif larr[0]=='xllcorner':pass
		elif larr[0]=='yllcorner':pass
		elif larr[0]=='cellsize':pass
		elif larr[0]=='NODATA_value':pass
		else:world.append([int(v.replace('-','-')) for v in larr])
	return szx,szy,world
szx,szy,streets=loadAsc('road1_santafe.asc')
szx,szy,slope=loadAsc('slope_santafe.asc')
szx,szy,urban=loadAsc('urban_santafe.asc')
szx,szy,landuse=loadAsc('landuse_santafe.asc')
szx,szy,exclude=loadAsc('excluded_santafe.asc')

#world=[[int(x.replace('-','-')) for x in y] for y in world]
screen=pygame.display.set_mode((szx,szy), 0, 32)
pygame.display.set_caption('Hello world!')
screen.fill((0,0,0))
for y in range(szy):
	for x in range(szx):
		if float(slope[y][x])>0:screen.set_at((x,y),(255,0,0))
		if float(landuse[y][x])>0:screen.set_at((x,y),(0,255,0))
		if float(urban[y][x])>0:screen.set_at((x,y),(0,0,255))
		if float(exclude[y][x])>0:screen.set_at((x,y),(0,255,255))
		if float(streets[y][x])>0:screen.set_at((x,y),(255,255,255))

pygame.display.update()


running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:running=False
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	'''
	clr=(randint(0,255),randint(0,255),randint(0,255))
	if pygame.mouse.get_pressed()[0]:
		pygame.draw.circle(screen, clr, mouse, 20, 0)
		
		arr.append(list(mouse))
		
	pygame.display.update()
'''

pygame.quit()
sys.exit()