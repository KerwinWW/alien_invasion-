import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	"""docstring for Alien"""
	def __init__(self, ai_settings, screen):
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		#设置背景
		self.image = pygame.image.load(
			"E:/Python_demo/alien_invasion/pic/alien.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

	#绘制屏幕
	# def blitme(self):
	# 	self.screen.blit(self.image, self.rect)

	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True


	def update(self, ai_settings):
		self.x += (self.ai_settings.alien_apeed_factor *
						self.ai_settings.fleet_direction)
		self.rect.x = self.x

