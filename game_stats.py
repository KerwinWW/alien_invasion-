class GameStats(object):
	"""docstring for GameStats"""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		
		self.game_active = False

		#永远不重置最高分
		self.high_score = 0

	def reset_stats(self):
		#初始化在游戏运行期间可能变化的统计信息
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1