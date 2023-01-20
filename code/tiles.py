import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
	def __init__(self,sizeX,sizeY,x,y):
		super().__init__()
		self.image = pygame.Surface((sizeX,sizeY))
		self.rect = self.image.get_rect(topleft = (x,y))

	def update(self,shift):
		self.rect.x += shift

class StaticTile(Tile):
	def __init__(self,sizeX,sizeY,x,y,surface):
		super().__init__(sizeX,sizeY,x,y)
		self.image = surface

class AnimatedTile(Tile):
	def __init__(self,sizeX,sizeY,x,y,path):
		super().__init__(sizeX,sizeY,x,y)
		self.frames = import_folder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,shift):
		self.animate()
		self.rect.x += shift

class Metro(StaticTile):
	def __init__(self,sizeX,sizeY,x,y,path):
		super().__init__(sizeX,sizeY,x,y,path)

class Tile_Level_0(StaticTile):
	def __init__(self,sizeX,sizeY,x,y,path):
		super().__init__(sizeX,sizeY,x,y,path)

class Coin_Level_0(StaticTile):
		def __init__(self,sizeX,sizeY,x,y,path,value):
			super().__init__(sizeX,sizeY,x,y,path)
			center_x = x + int(sizeX / 2)
			center_y = y + int(sizeY / 2)
			self.rect = self.image.get_rect(center = (center_x,center_y))
			self.value = value
