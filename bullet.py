import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, ai_settings, screen, ship):
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen
		self.ship = ship
		
		#在（0，0）处创建子弹rect, 再设置正确的位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
			ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#存储小数表示的子弹位置
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		#设置子弹移动（float 微调）
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		#在屏幕上绘 出子弹
		pygame.draw.rect(self.screen, self.color, self.rect)


