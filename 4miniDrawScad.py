import pygame, sys
from random import randint
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')
screen.fill((0,0,0))
pygame.display.update()

arr=[]

running=True
while running:
	for event in pygame.event.get():
		if event.type==QUIT:running=False
	mouseX,mouseY=mouse=pygame.mouse.get_pos()
	clr=(randint(0,255),randint(0,255),randint(0,255))
	if pygame.mouse.get_pressed()[0]:
		pygame.draw.circle(screen, clr, mouse, 20, 0)
		
		arr.append(list(mouse))
		
	pygame.display.update()
	
with open('data.scad','w') as f:
	f.write('data=[')
	for p in arr:
		f.write(str(p)+',\n')
	f.write('];')
	
pygame.quit()
sys.exit()