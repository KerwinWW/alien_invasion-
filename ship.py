import pygame

from pygame.sprite import Sprite


class Ship(Sprite):
	"""docstring for Ship"""
	def __init__(self, ai_settings ,screen):
		super().__init__()
		#加载图像，获取矩形
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load(
			"E:/Python_demo/alien_invasion/pic/ship.png")
		self.rect = self.image.get_rect()
		self.screen_rect =screen.get_rect()

		#每艘飞船放在屏幕中间	
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 在飞船的属性center中存储小数值
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def update(self):
		if self.moving_right and (self.rect.right < self.screen_rect.right):
			#飞船右移
			self.centerx += self.ai_settings.ship_speed_factor
		elif self.moving_left and (self.rect.left > self.screen_rect.left):
			self.centerx -= self.ai_settings.ship_speed_factor
		# elif self.moving_up and (self.rect.top > self.screen_rect.top):
		# 	self.centery -= self.ai_settings.ship_speed_factor
		# elif self.moving_down and (self.rect.bottom < self.screen_rect.bottom):
		# 	self.centery += self.ai_settings.ship_speed_factor

		#根据self.center 更新 rect对象
		self.rect.centerx = self.centerx
		# self.rect.centery = self.centery


					

	def blitme(self):
		#在指定位置绘制飞船
		self.screen.blit(self.image, self.rect)

	def center_ship(self):		
		#self.ai_settings.ship_clear = False
		self.centerx = self.screen_rect.centerx
		#self.rect.centerx = self.screen_rect.centerx
		#self.bottom = self.screen_rect.bottom