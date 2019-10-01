import pygame, sys
from random import randint,random
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
def checkSuitabity():
	maxSlope=max([max(l)for l in slope])
	#buildProp=[[0 for x in szx] for y in szy]
	buildProp=[]
	suitable=[[0 for x in szx] for y in szy]
	for i in range(criticalSlope):
		val=(criticalSlope-1)/criticalSlope
		buildProp.append(val**(slopeCoof/200))
	for j in range(maxSlope-criticalSlope):
		buildProp.append(0)
	for y in range(szy):
		for x in range(szx):
			if random()<buildProp[slope[y][x]]:
				suitable[y][x]=1

def sponGrowth(iter):
	for i in range(iter):
		x=randin(0,szx-1)
		y=randin(0,szy-1)
		if world[y][x]:pass	

slopeCoof=50
criticalSlope=25
szx,szy,streets=loadAsc('road1_santafe.asc')
szx,szy,slope=loadAsc('slope_santafe.asc')
szx,szy,urban=loadAsc('urban_santafe.asc')
szx,szy,landuse=loadAsc('landuse_santafe.asc')
szx,szy,exclude=loadAsc('excluded_santafe.asc')
print(szx,szy)
#world=[[int(x.replace('-','-')) for x in y] for y in world]
csx=csy=16#world size Cell Number Axis

screen=pygame.display.set_mode((szx*csx,szy*csy), 0, 32)
pygame.display.set_caption(str(szx*csx)+' '+str(szy*csy))
screen.fill((0,0,0))


basicFont = pygame.font.SysFont(None, 24)


#textRect=text.get_rect()
#textRect.centerx=windowSurface.get_rect().centerx
#textRect.centery=windowSurface.get_rect().centery
#pygame.draw.rect(screen, RED, (0,0,16,16))




for y in range(szy):
	for x in range(szx):
		if slope[y][x]>0:pygame.draw.rect(screen,(255,0,0),(csx*x,csy*y,csx,csy))
		if landuse[y][x]>0:pygame.draw.rect(screen,(0,255,0),(csx*x,csy*y,csx,csy))
		if urban[y][x]>0:pygame.draw.rect(screen,(0,0,255),(csx*x,csy*y,csx,csy))
		if exclude[y][x]>0:pygame.draw.rect(screen,(0,255,255),(csx*x,csy*y,csx,csy))
		if streets[y][x]>0:pygame.draw.rect(screen,(255,255,255),(csx*x,csy*y,csx,csy))
		text=basicFont.render(str(slope[y][x]),True, (0,0,0))
		screen.blit(text,(x*16,y*16,16,16))
		
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
pygame.image.save(screen, "map.png")
pygame.quit()
sys.exit()
