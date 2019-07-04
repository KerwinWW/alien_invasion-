import sys

import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats	import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
	#创建窗口对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width , ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")


	#创建PLAY 按键
	play_button = Button(ai_settings, screen, "Play")


	#创建一个用于存储游戏的统计信息的实例
	stats = GameStats(ai_settings)
	#创建记分实例
	scoreboard = Scoreboard(ai_settings, screen, stats)

	#创建飞船
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_settings, screen, aliens, ship)

	while True:
		#键盘鼠标事件
		gf.check_events(ai_settings,screen, ship ,bullets, stats,
			play_button, aliens, scoreboard)
		if stats.game_active:
			ship.update()
			gf.revome_bullets(bullets, aliens ,ai_settings, screen,
				ship, stats, scoreboard)
			gf.update_alients(aliens, ai_settings, ship, screen, bullets, stats, scoreboard)
		#刷新屏幕
		gf.update_screen(ai_settings,screen, ship , aliens, bullets, 
			stats, play_button, scoreboard) 
		

run_game()
