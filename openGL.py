import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(-1, -1, -1),	#node 0
	(1, -1, -1),	#node 1 	
	(1, 1, -1),		#node 2
	(-1, 1, -1),	#node 3
	(-1, -1, 1),	#node 4
	(1, -1, 1),		#node 5
	(1, 1, 1),		#node 6
	(-1, 1, 1),		#node 7
	(0, 0, 2),		#node 8
	(0, 0, -2),		#node 9
	(0, 2, 0),		#node 10
	(0, -2, 0),		#node 11
	(2, 0, 0),		#node 12
	(-2, 0, 0)		#node 13
	)

edges = (
	(0,1),
	(1,2),
	(2,3),
	(3,0),
	(4,5),
	(5,6),
	(6,7),
	(7,4),
	(0,4),
	(1,5),
	(2,6),
	(3,7),
	(8,9),
	(10,11),
	(12,13)
	)
	
surfaces = (
	(0,1,2,3),
	(4,5,6,7),
	(0,1,5,4),
	(3,2,6,7),
	(1,5,6,2),
	(0,4,7,3)
	)

colors = (
	(0,0,1),
	(0,1,0),
	(1,0,0)
	)
	
def Cube():
	glBegin(GL_QUADS)
	color = 0
	for surface in surfaces:
		for vertex in surface:
			glColor3fv(colors[color])
			glVertex3fv(vertices[vertex])
			color+=1
			if(color==3):
				color=0
	glEnd()

	glBegin(GL_LINES)
	glColor3fv((1,1,1))
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
	
def main():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	
	glTranslatef(0.0, 0.0, -5)
	
	glRotate(0, 0, 0, 0)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		glRotate(1, 2, 3, 2)
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Cube()
		pygame.display.flip()
		pygame.time.wait(10)
		
main()
	
	