class Settings(object):
	"""docstring for Setting"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#死亡次数
		self.ship_limit = 1


		#子弹设置
		self.bullet_width = 1200
		self.bullet_height = 15
		self.bullet_color = 255, 255, 255
		self.bullet_allowde = 10 

		#外星人设置
		# self.alien_width = 3
		# self.alien_height = 15
		#下降速度
		self.fleet_drop_speed = 15

		#游戏升级后移动速度加快的倍数
		self.speedup_scale = 1.1
		#外星人计分点数位数
		self.score_scale = 1.5
		#初始化游戏属性
		self.initialize_dymamic_settings()

	def initialize_dymamic_settings(self):
		'''重置游戏设置'''
		#飞船移动速度
		self.ship_speed_factor = 5
		#子弹移动速度
		self.bullet_speed_factor = 3
		#外星人移动速度
		self.alien_apeed_factor = 1
		# 1表示向右，-1向左
		self.fleet_direction = 1

		#记分
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_apeed_factor *= self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		#print(self.alien_points)
