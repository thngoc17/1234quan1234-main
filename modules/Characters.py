import pygame


class Hero(pygame.sprite.Sprite):
	def __init__(self, imagepath, coordinate, block_size, border_size, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imagepath)
		self.image = pygame.transform.scale(self.image, (block_size, block_size))
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = coordinate[0] * block_size + border_size[0], coordinate[1] * block_size + border_size[1]
		self.coordinate = coordinate
		self.block_size = block_size
		self.border_size = border_size
		self.imagepath = imagepath
	
	def __getstate__(self):
		state = self.__dict__.copy()
		del state['image']
		del state['rect']
		return state
	
	def __setstate__(self, state):
		self.__dict__.update(state)
		self.image = pygame.image.load(self.imagepath)
		self.image = pygame.transform.scale(self.image, (self.block_size, self.block_size))
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = self.coordinate[0] * self.block_size + self.border_size[0], self.coordinate[1] * self.block_size + self.border_size[1]
	def to_dict(self):
		return {
			'coordinate': self.coordinate,
			'block_size': self.block_size,
			'border_size': self.border_size
		}
	def move(self, direction, maze):
		blocks_list = maze.blocks_list
		if direction == 'up':
			if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[0]:
				return False
			else:
				self.coordinate[1] = self.coordinate[1] - 1
				return True
		elif direction == 'down':
			if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[1]:
				return False
			else:
				self.coordinate[1] = self.coordinate[1] + 1
				return True
		elif direction == 'left':
			if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[2]:
				return False
			else:
				self.coordinate[0] = self.coordinate[0] - 1
				return True
		elif direction == 'right':
			if blocks_list[self.coordinate[1]][self.coordinate[0]].has_walls[3]:
				return False
			else:
				self.coordinate[0] = self.coordinate[0] + 1
				return True
		else:
			raise ValueError('Unsupport direction <%s> in Hero.move...' % direction)

	def draw(self, screen):
		self.rect.left, self.rect.top = self.coordinate[0] * self.block_size + self.border_size[0], self.coordinate[1] * self.block_size + self.border_size[1]
		screen.blit(self.image, self.rect)