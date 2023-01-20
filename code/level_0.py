import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height, screen_width
from tiles import Tile, StaticTile, Tile_Level_0, Coin_Level_0
from enemy import Enemy
from player import Player
from particles import ParticleEffect
from game_data import levels
import random
class Level_0:
	def __init__(self,current_level,surface,create_overworld,change_coins,change_health):
		# general setup
		self.display_surface = surface
		self.world_shift = 0
		self.current_x = None
		# overworld connection
		self.create_overworld = create_overworld
		self.current_level = current_level
		level_data = levels[self.current_level]
		self.new_max_level = level_data['unlock']
		# user interface
		self.change_coins = change_coins
		# player
		player_layout = import_csv_layout(level_data['player'])
		self.player = pygame.sprite.GroupSingle()
		self.goal = pygame.sprite.GroupSingle()
		self.player_setup(player_layout,change_health)
		# dust
		self.dust_sprite = pygame.sprite.GroupSingle()
		self.player_on_ground = False
		# explosion particles
		self.explosion_sprites = pygame.sprite.Group()

		self.shake_time = 0
		self.reading_message = False
		#ground
		ground_layout = import_csv_layout(level_data['ground'])
		self.ground_sprite = self.create_tile_group(ground_layout,'ground')

		#bground
		bground_layout = import_csv_layout(level_data['bground'])
		self.bground_sprite = self.create_tile_group(bground_layout,'bground')

		#coins
		coins_layout = import_csv_layout(level_data['coins'])
		self.coins_sprite = self.create_tile_group(coins_layout,'coins')

		#constraints
		constraints_layout = import_csv_layout(level_data['constraints'])
		self.constraints_sprite = self.create_tile_group(constraints_layout,'constraints')

		#decoration
		decoration_layout = import_csv_layout(level_data['decoration'])
		self.decoration_sprite = self.create_tile_group(decoration_layout,'decoration')

		#enemies
		enemies_layout = import_csv_layout(level_data['enemies'])
		self.enemies_sprite = self.create_tile_group(enemies_layout,'enemies')

		#message
		message_layout = import_csv_layout(level_data['message'])
		self.message_sprite = self.create_tile_group(message_layout,'message')

		#message_sign
		message_sign_layout = import_csv_layout(level_data['message_sign'])
		self.message_sign_sprite = self.create_tile_group(message_sign_layout,'message_sign')

		end_layout = import_csv_layout(level_data['end'])
		self.end_sprite = self.create_tile_group(end_layout,'end')




	#Creates a sprite group from your csv files
	def create_tile_group(self,layout,type):
		sprite_group = pygame.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val != '-1':
					x = col_index * tile_size
					y = row_index * tile_size

					if type == 'ground':
						if val == '0' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/0.png').convert_alpha())
						if val == '1' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/1.png').convert_alpha())
						if val == '2' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/2.png').convert_alpha())
						if val == '3' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/3.png').convert_alpha())
						if val == '4' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/4.png').convert_alpha())
						if val == '5' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/5.png').convert_alpha())
						if val == '6' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/6.png').convert_alpha())
						if val == '7' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/7.png').convert_alpha())
						if val == '8' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/8.png').convert_alpha())
						if val == '9' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/9.png').convert_alpha())
						if val == '10' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/10.png').convert_alpha())
						if val == '11' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/11.png').convert_alpha())
						if val == '12' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/12.png').convert_alpha())
						if val == '13' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/13.png').convert_alpha())
						if val == '14' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/14.png').convert_alpha())
						if val == '15' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/15.png').convert_alpha())
						if val == '16' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/16.png').convert_alpha())
						if val == '17' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/17.png').convert_alpha())
						if val == '18' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/18.png').convert_alpha())
						if val == '19' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/ground/19.png').convert_alpha())

					if type == 'bground':
						if val == '0' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/0.png').convert_alpha())
						if val == '1' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/1.png').convert_alpha())
						if val == '2' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/2.png').convert_alpha())
						if val == '3' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/3.png').convert_alpha())
						if val == '4' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/4.png').convert_alpha())
						if val == '5' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/5.png').convert_alpha())
						if val == '6' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/6.png').convert_alpha())
						if val == '7' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/7.png').convert_alpha())
						if val == '8' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/8.png').convert_alpha())
						if val == '9' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/9.png').convert_alpha())
						if val == '10' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/10.png').convert_alpha())
						if val == '11' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/11.png').convert_alpha())
						if val == '12' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/12.png').convert_alpha())
						if val == '13' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/13.png').convert_alpha())
						if val == '14' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/14.png').convert_alpha())
						if val == '15' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/15.png').convert_alpha())
						if val == '16' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/16.png').convert_alpha())
						if val == '17' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/17.png').convert_alpha())
						if val == '18' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/18.png').convert_alpha())
						if val == '19' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/19.png').convert_alpha())
						if val == '20' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/20.png').convert_alpha())
						if val == '21' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/21.png').convert_alpha())
						if val == '22' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/22.png').convert_alpha())
						if val == '23' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/23.png').convert_alpha())
						if val == '24' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/24.png').convert_alpha())
						if val == '25' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/25.png').convert_alpha())
						if val == '26' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/26.png').convert_alpha())
						if val == '27' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/27.png').convert_alpha())
						if val == '28' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/28.png').convert_alpha())
						if val == '29' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/29.png').convert_alpha())
						if val == '30' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/30.png').convert_alpha())
						if val == '31' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/31.png').convert_alpha())
						if val == '32' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/32.png').convert_alpha())
						if val == '33' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/bground/33.png').convert_alpha())

					if type == 'coins':
						sprite = Coin_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/coins/koshary/coin.png').convert_alpha(),1)

					if type == 'constraints':
						sprite = Tile(tile_size,tile_size,x,y)

					if type == 'end':
						sprite = Tile(tile_size,tile_size,x,y)

					if type == 'decoration':
						if val == '0' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/decoration/0.png').convert_alpha())
						if val == '1' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/decoration/1.png').convert_alpha())
						if val == '2' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/decoration/2.png').convert_alpha())
						if val == '3' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/decoration/3.png').convert_alpha())
						if val == '4' : sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/decoration/4.png').convert_alpha())

					if type == 'enemies':
						sprite = Enemy(tile_size,x,y,'../graphics/enemy/Joker')

					if type == 'message':
						sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/message/0.png').convert_alpha())

					if type == 'message_sign':
						sprite = Tile_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/Level_0/message/1.png').convert_alpha())



					sprite_group.add(sprite)




		return sprite_group


	#Setup the player's start and the game end
	def player_setup(self,layout,change_health):
		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				if val == '0':
					sprite = Player((x,y),self.display_surface,self.create_jump_particles,change_health)
					self.player.add(sprite)
				if val == '1':
					hat_surface = pygame.image.load('../graphics/character/bat.png').convert_alpha()
					sprite = StaticTile(tile_size,tile_size,x,y,hat_surface)
					self.goal.add(sprite)




	#Reverses the enemy's direction when it hits the constraints
	def enemy_collision_reverse(self):
		for enemy in self.enemies_sprite.sprites():

			if pygame.sprite.spritecollide(enemy,self.constraints_sprite,False):
				enemy.reverse()




	#Creates a particles animation when the player jumps
	def create_jump_particles(self,pos):
		if self.player.sprite.facing_right:
			pos -= pygame.math.Vector2(10,5)
		else:
			pos += pygame.math.Vector2(10,-5)
		jump_particle_sprite = ParticleEffect(pos,'jump')
		self.dust_sprite.add(jump_particle_sprite)




	#Creates the horizontal movement of the player
	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.collision_rect.x += player.direction.x * player.speed
		                     ##############################
		collidable_sprites = self.ground_sprite
		                     #############################
		for sprite in collidable_sprites:
			if sprite.rect.colliderect(player.collision_rect):
				if player.direction.x < 0:
					player.collision_rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.collision_rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right






	#Creates the Vertical movement of the player
	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()
		                     ##############################
		collidable_sprites = self.ground_sprite
		                     #############################

		for sprite in collidable_sprites:
			if sprite.rect.colliderect(player.collision_rect):
				if player.direction.y > 0:
					player.collision_rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.collision_rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False


	def horizontal_end(self):
		player = self.player.sprite
		player.collision_rect.x += player.direction.x * player.speed
		                     ##############################
		collidable_sprites = self.end_sprite
		                     #############################
		for sprite in collidable_sprites:
			if sprite.rect.colliderect(player.collision_rect):
				if player.direction.x < 0:
					player.collision_rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.collision_rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right


	def shake_count_down(self):
		if self.shake_time > 0:
			self.shake_time -= 1
	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_s]:
			if self.reading_message == True:
				self.shake_time = 60
				self.reading_message = False




	#Creates the screen's movement when the player gets out of range
	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x
		if self.shake_time == 0:
			if player_x < screen_width / 4 and direction_x < 0:
				self.world_shift = 8
				player.speed = 0
			elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
				self.world_shift = -8
				player.speed = 0
			else:
				self.world_shift = 0
				player.speed = 8
		else:
			for i in range(60):
				self.world_shift = random.randint(-5,5)





	#Checks if the playr of ground
	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False





	#Creates landing animation when the playes falls
	def create_landing_dust(self):
		if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
			if self.player.sprite.facing_right:
				offset = pygame.math.Vector2(10,15)
			else:
				offset = pygame.math.Vector2(-10,15)
			fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset,'land')
			self.dust_sprite.add(fall_dust_particle)




	#Checks if the Player had died
	def check_death(self):
		if self.player.sprite.rect.top > screen_height:
			self.create_overworld(self.current_level,0)



	#Checks if the player reaches the end of the level
	def check_win(self):
		if pygame.sprite.spritecollide(self.player.sprite,self.goal,False):
			self.create_overworld(self.current_level,self.new_max_level)



	#Checks if the player gains coins (koshary)
	def check_coin_collisions(self):

		collided_coins = pygame.sprite.spritecollide(self.player.sprite,self.coins_sprite,True)
		if collided_coins:
			for coin in collided_coins:
				self.change_coins(coin.value)



	#Checks the collision with  the enemy
	def check_enemy_collisions(self):

		enemy_collisions = pygame.sprite.spritecollide(self.player.sprite,self.enemies_sprite,False)

		if enemy_collisions:
			for enemy in enemy_collisions:
				enemy_center = enemy.rect.centery
				enemy_top = enemy.rect.top
				player_bottom = self.player.sprite.rect.bottom
				if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
					self.player.sprite.direction.y = -15
					explosion_sprite = ParticleEffect(enemy.rect.center,'explosion')
					self.explosion_sprites.add(explosion_sprite)
					enemy.kill()
				else:
					self.player.sprite.get_damage()
	def check_message_collision(self):
		collided_message = pygame.sprite.spritecollide(self.player.sprite,self.message_sprite,True)
		if collided_message:
			for message in collided_message:
				self.reading_message = True



	def draw_speech_bubble(self,screen, pos, size):
		if self.reading_message == True:
			text_surface = pygame.image.load('../graphics/terrain/Level_0/message/2.png').convert_alpha()
			text_rect = text_surface.get_rect(midbottom=pos)
			screen.blit(text_surface, text_rect)
	# runs the entire game / level
	def run(self):
		# run the entire game / level


		self.bground_sprite.update(self.world_shift)
		self.bground_sprite.draw(self.display_surface)


		self.ground_sprite.update(self.world_shift)
		self.ground_sprite.draw(self.display_surface)


		self.coins_sprite.update(self.world_shift)
		self.coins_sprite.draw(self.display_surface)


		self.decoration_sprite.update(self.world_shift)
		self.decoration_sprite.draw(self.display_surface)

		self.message_sprite.update(self.world_shift)
		self.message_sprite.draw(self.display_surface)

		self.message_sign_sprite.update(self.world_shift)
		self.message_sign_sprite.draw(self.display_surface)

		self.end_sprite.update(self.world_shift)

		self.draw_speech_bubble(self.display_surface,(900,400),200)
		self.enemies_sprite.update(self.world_shift)
		self.constraints_sprite.update(self.world_shift)
		self.enemy_collision_reverse()
		self.enemies_sprite.draw(self.display_surface)
		self.explosion_sprites.update(self.world_shift)
		self.explosion_sprites.draw(self.display_surface)



		# player sprites
		self.player.update(self.world_shift)
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.horizontal_end()
		self.create_landing_dust()

		self.scroll_x()
		self.player.draw(self.display_surface)
		self.goal.update(self.world_shift)
		self.goal.draw(self.display_surface)

		self.check_death()
		self.check_win()

		self.shake_count_down()
		self.get_input()
		self.check_coin_collisions()
		self.check_enemy_collisions()
		self.check_message_collision()
