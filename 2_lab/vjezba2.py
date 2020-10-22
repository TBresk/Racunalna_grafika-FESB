import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

print("Imports done!")

#Vrhovi
vertices = (
	(0, 1, 0),
	(-1, -1, 0),
	(1, -1, 0)
)

#Bridovi
edges = (
	(0, 1),
	(0, 2),
	(1, 2)
)

#Površine
surface = (0, 1, 2)

#Boje
colors = (
	(1, 0, 0),
	(0, 0, 1),
	(0, 0, 1),
	(1, 0, 0)
)

#Funkcija koja iscrtava poligon
def Draw():
	glBegin(GL_QUADS)
	glColor3f(255, 0, 0)
	for vertex in surface:
		glVertex3fv(vertices[vertex])
	glEnd()

	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])			
	glEnd()

def main():
	pygame.init()
	display = (600, 400)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
	pygame.display.set_caption('2. laboratorijska vjezba')
	
	gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
	glTranslatef(0.0, 0.0, -5)
	glRotatef(0, 0, 0, 0)
	#Povećavanje poligona za 40%
	glScalef(1.4, 1.4, 1.4)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					print("X pressed!") 
					glRotate(10, 1, 0, 0)
				if event.key ==  pygame.K_y:
					print("Y pressed!") 
					glRotate(5, 0, 1, 0)

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		Draw()
		pygame.display.flip()	
		pygame.time.wait(10)

main()

























