import pygame

class button(object):
	def __init__(self, xlocation, ylocation, x2size, y2size):
		self.xlocation=xlocation
		self.ylocation=ylocation
		self.x2size=x2size
		self.y2size=y2size
		self.rec = pygame.Rect(xlocation, ylocation, x2size, y2size)
   		self.sq = pygame.Surface([x2size, y2size])
	def draw(self,main_screen):
		main_screen.blit(self.sq, self.rec)
    
