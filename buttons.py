import pygame

class button(object):
	def __init__(self, xlocation, ylocation, x2size, y2size, r, g, b, picture=""):
		self.xlocation=xlocation
		self.ylocation=ylocation
		self.x2size=x2size
		self.y2size=y2size
		self.rec = pygame.Rect(xlocation, ylocation, x2size, y2size)
   		self.sq = pygame.Surface([x2size, y2size])
   		self.sq.fill((r,g,b))
   		if picture:
   			self.buttonimg = pygame.image.load(picture)
   		else:
   			self.buttonimg = ""
	def draw(self,main_screen):
		if self.buttonimg:
			main_screen.blit(self.buttonimg, self.rec)
		else:
			main_screen.blit(self.sq, self.rec)

    

