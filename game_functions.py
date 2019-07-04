import sys #python标准库模块 事件循环检查

import pygame 
from bullet import Bullet
from alien import Alien
from random import randint
from time import sleep

def check_keydown_events(event, ai_settings,screen, ship ,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#飞船左移
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_settings,screen, ship ,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
 
def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:	
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_events(ai_settings,screen, ship ,bullets, stats, play_button,
		aliens, scoreboard):
		#监听键盘鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen, ship ,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)	
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, play_button, mouse_x, mouse_y, aliens, 
				bullets, ai_settings, screen, ship, scoreboard)

def check_play_button(stats, play_button, mouse_x, mouse_y, aliens, 
	bullets,ai_settings, screen, ship, scoreboard):
	#点击按钮开始游戏
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		#重置游戏设置
		ai_settings.initialize_dymamic_settings()
		#隐藏光标
		pygame.mouse.set_visible(False)
		#重置上一局游戏信息
		stats.reset_stats()

		stats.game_active = True

		#重置记仇牌图像
		scoreboard.prep_score()
		scoreboard.prep_high_score()
		scoreboard.prep_level()
		scoreboard.prep_ships()


		#清空机器人和子弹列表
		aliens.empty()
		bullets.empty()

		#创建新外星人，飞船居中
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()



def update_screen(ai_settings,screen, ship , aliens, bullets,
		stats, play_button, scoreboard):
	#每次循环都重绘屏幕	
	background = pygame.image.load(
		"E:/Python_demo/alien_invasion/pic/background.jpeg")
	screen.blit(background,(0,0))

	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()


	ship.blitme()
	aliens.draw(screen)
	scoreboard.show_score()

	#如果游戏处于非活动状态，绘制Play 按钮
	if not stats.game_active:
		play_button.draw_button()
	#显示窗口
	pygame.display.flip()

def fire_bullets(ai_settings,screen, ship ,bullets):
	if len(bullets) <= ai_settings.bullet_allowde:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def revome_bullets(bullets, aliens, ai_settings, screen, ship, stats, scoreboard):
	bullets.update()
	#删除消失的子弹
	for bullet in bullets.copy():	
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			print(len(bullets))	
	check_bullet_alien_collisions(ai_settings, screen, ship, aliens,
		bullets, stats, scoreboard)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens,
		bullets, stats, scoreboard):
	# 检查是否有子弹击中了外星人
	# 如果是，就删除相应的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			#一次击落多个外星人时，统计之数之和
			stats.score += ai_settings.alien_points*len(aliens)
			scoreboard.prep_score()
		check_high_score(stats, scoreboard)	

	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()

		#提高等级
		stats.level += 1
		scoreboard.prep_level()

		create_fleet(ai_settings, screen, aliens, ship)	

def check_high_score(stats, scoreboard):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		scoreboard.prep_high_score()


def create_fleet(ai_settings, screen, aliens, ship):
	
	alien = Alien(ai_settings, screen)
	#计算每行个数
	alien_num = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_aliens_y(ai_settings, alien.rect.height, ship)
	#创建外星人群
	for row_y in range(number_rows):
		for num_x in range(alien_num):#(randint(-10,10)):
			create_alien(ai_settings, screen, aliens, num_x, row_y)


def get_number_aliens_x(ai_settings, alien_width):
	#每行外星人个数
	available_space_x = ai_settings.screen_width - (2*alien_width)
	number_available_x = int(available_space_x / (2*alien_width))
	return number_available_x

def create_alien(ai_settings, screen, aliens, alien_num, row_num):
	alien = Alien(ai_settings, screen)
	alien.x = alien.rect.width + 2*alien.rect.width*alien_num
	alien.y = alien.rect.height + 2*alien.rect.height*row_num
	alien.rect.x = alien.x
	alien.rect.y = alien.y
	aliens.add(alien)

def get_number_aliens_y(ai_settings, alien_height, ship):
	available_space_y = ai_settings.screen_height -\
						(3*alien_height) - ship.rect.height
	number_rows = int(available_space_y/(2*alien_height))
	return number_rows

def update_alients(aliens, ai_settings, ship, screen, bullets, stats, scoreboard):
	check_fleet_edges(ai_settings, aliens)
	aliens.update(ai_settings)

	#检查外星人碰撞
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(aliens, ai_settings, ship, screen, bullets, stats, scoreboard)
	#检查是否有外星人到底端
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, scoreboard)

def check_fleet_edges(ai_settings, aliens):
	#检测是否到边缘
	for alien in aliens.sprites():
		if alien.check_edges():
			#下移并反向
			change_fleet_dirction(ai_settings, aliens)
			break

def change_fleet_dirction(ai_settings, aliens):
	#外星人下移并改变方向
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1

def ship_hit(aliens, ai_settings, ship, screen, bullets, stats, scoreboard):
	if stats.ships_left > 0:
		#外星人撞飞船
		stats.ships_left -= 1

		#更新记仇牌
		scoreboard.prep_ships()

		#清空外星人列表
		aliens.empty()
		bullets.empty()
		#创建新一批外星人
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()
		sleep(1.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, scoreboard):
	#检查是否有外星人到底端
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(aliens, ai_settings, ship, screen, bullets, stats, scoreboard)
			break

