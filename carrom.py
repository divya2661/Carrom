#!use/bin/python
import os,sys,pygame
pygame.init()
from pygame.locals import *
import random
import math
#-----------window-------------
bg_color=(236,229,182)
(width, height) = (550,570)
screen = pygame.display.set_mode((width, height))
screen.fill(bg_color)
BLUE  = (  43,   27, 23)
RED = (159, 0, 15)
BLACK=(0,0,0)
PPR=(125, 5, 82)
pi=3.141592653
# upper lines---------------------
pygame.draw.line(screen, BLUE, (100, 60), (450, 60), 4)
pygame.draw.line(screen, BLUE, (100, 80), (450, 80), 2)
pygame.draw.circle(screen, BLUE, (100, 71), 11, 0)
pygame.draw.circle(screen, RED, (100, 71), 9, 0)
pygame.draw.circle(screen, BLUE, (450, 70), 11, 0)
pygame.draw.circle(screen, RED, (450, 70), 9, 0)

#LEFT LINES-------------------------
pygame.draw.line(screen, BLUE, (480, 100), (480,450), 4)
pygame.draw.line(screen, BLUE, (460, 100), (460, 450), 2)
pygame.draw.circle(screen, BLUE, (472, 100), 11, 0)
pygame.draw.circle(screen, RED, (472, 100), 9, 0)
pygame.draw.circle(screen, BLUE, (472, 450), 11, 0)
pygame.draw.circle(screen, RED, (472, 450), 9, 0)

#bottom line----------------------------

pygame.draw.line(screen, BLUE, (100, 490), (450, 490), 4)
pygame.draw.line(screen, BLUE, (100, 470), (450, 470), 2)
pygame.draw.circle(screen, BLUE, (100, 480), 11, 0)
pygame.draw.circle(screen, RED, (100, 480), 9, 0)
pygame.draw.circle(screen, BLUE, (450, 480), 11, 0)
pygame.draw.circle(screen, RED, (450, 480), 9, 0)

#right line------------------------------

pygame.draw.line(screen, BLUE, (70, 100), (70,450), 4)
pygame.draw.line(screen, BLUE, (90, 100), (90, 450), 2)
pygame.draw.circle(screen, BLUE, (80, 100), 11, 0)
pygame.draw.circle(screen, RED, (80, 100), 9, 0)
pygame.draw.circle(screen, BLUE, (80, 450), 11, 0)
pygame.draw.circle(screen, RED, (80, 450), 9, 0)

#corner circles---------------

pygame.draw.circle(screen, BLACK, (11, 11), 16, 0)
pygame.draw.circle(screen, BLACK, (539, 11), 16, 0)
pygame.draw.circle(screen, BLACK, (11, 557), 16, 0)
pygame.draw.circle(screen, BLACK, (539, 557), 16, 0)

#center circle-------------------

pygame.draw.circle(screen, RED, (275, 285), 50, 0)
pygame.draw.circle(screen, bg_color, (275, 285), 45, 0)
pygame.draw.circle(screen, RED, (275, 285), 40, 0)
pygame.draw.circle(screen, bg_color, (275, 285), 35, 0)
pygame.draw.circle(screen, RED, (275, 285), 30, 0)
pygame.draw.circle(screen, bg_color, (275, 285), 25, 0)
pygame.draw.circle(screen, RED, (275, 285), 20, 0)
pygame.draw.circle(screen, BLUE, (275, 285), 15, 0)

#arrow circles-------------
pygame.draw.circle(screen, BLUE, (90, 85), 9, 0)
pygame.draw.circle(screen, bg_color, (90, 85), 7, 0)

pygame.draw.circle(screen, BLUE, (460, 85), 9, 0)
pygame.draw.circle(screen, bg_color, (460, 85), 7, 0)

pygame.draw.circle(screen, BLUE, (460, 464), 9, 0)
pygame.draw.circle(screen, bg_color, (460, 464), 7, 0)

pygame.draw.circle(screen, BLUE, (90, 464), 9, 0)
pygame.draw.circle(screen, bg_color, (90, 464), 7, 0)

# arraw lines---------------------

#pygame.draw.line(screen, BLUE, (65, 61), (180,176), 3)
#pygame.draw.arc( screen, BLUE, [145,145,40,40], pi/2,0,2)

#create particles-------------------------
class Particle:
	def __init__(self,(x,y),size):

		self.x=x
		self.y=y
		self.size=size
		self.color=PPR
		#self.speed=speed
		#self.angle=angle
	def display(self):
		pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)
		

size =12
n=10
for n in range(n):
	x = random.randint(size, width - size)
	y = random.randint(size, height - size)
	particle = Particle((x, y), size)
	particle.speed=random.random()
	particle.angle=random.uniform(0,math.pi*2)
    Particle.display()


#------------------------------------------
pygame.display.flip()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running= False