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

    
class label(object):

	def __init__(self, a, b, c, d, text\
	90 ):
		self.label_rec = pygame.Rect(a, b, c, d)
    	self.orderlabel = pygame.font.Font(None, 50)
    	self.label = orderlabel.render(text, 1, (255, 0,0), (41, 218, 206))
    	main_screen.blit(self.label, self.label_rec)
