import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height, screen_width
from tiles import Tile, StaticTile, Metro,Tile_Level_0,Coin_Level_0
from enemy import Enemy
from player import Player
from particles import ParticleEffect
from game_data import levels

class Level_2:
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

		####################
		#Your Variables Here
		###################
		#ground
		ground_2 = import_csv_layout(level_data['level_2_groud'])
		self.ground_sprite = self.create_tile_group(ground_2 ,'level_2_groud')

		#bground
		bground_2 = import_csv_layout(level_data['level_2_background'])
		self.bground_sprite = self.create_tile_group(bground_2 ,'level_2_background')

		#coins
		coins_2 = import_csv_layout(level_data['level_2_coins'])
		self.coins_sprite = self.create_tile_group(coins_2,'level_2_coins')

		#constraints
		constraints_2 = import_csv_layout(level_data['level_2_constrians'])
		self.constraints_sprite = self.create_tile_group(constraints_2,'level_2_constrians')

		#enemies
		enemies_2 = import_csv_layout(level_data['level_2_enemy'])
		self.enemies_sprite = self.create_tile_group(enemies_2,'level_2_enemy')

	#Creates a sprite group from your csv files
	def create_tile_group(self,layout,type):
		sprite_group = pygame.sprite.Group()

		for row_index, row in enumerate(layout):
			for col_index,val in enumerate(row):
				if val != '-1':
					x = col_index * tile_size
					y = row_index * tile_size

					#####################
					#Your Conditions Here
					#####################
					if type == 'level_2_groud':
						if val == '10' : sprite = Metro(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/level_2_g/10.png').convert_alpha())
					
					if type == 'level_2_background':
						if val == '9' : sprite = Metro(tile_size,tile_size,x,y,pygame.image.load('../graphics/terrain/level_2_bg/09.png').convert_alpha())

					if type == 'level_2_coins':
						sprite = Coin_Level_0(tile_size,tile_size,x,y,pygame.image.load('../graphics/coins/koshary/coin.png').convert_alpha(),1)

					if type == 'level_2_constrians':
						sprite = Tile(tile_size,tile_size,x,y)

					if type == 'level_2_enemy':
						sprite = Enemy(tile_size,x,y,'../graphics/enemy/level_2_enemy')

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






	#Creates the screen's movement when the player gets out of range
	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < screen_width / 4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
		elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
		else:
			self.world_shift = 0
			player.speed = 8




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
		                                                                #######################################
		collided_coins = pygame.sprite.spritecollide(self.player.sprite,self.coins_sprite
		,True)                                                          ######################################
		if collided_coins:
			for coin in collided_coins:
				self.change_coins(coin.value)



	#Checks the collision with  the enemy
	def check_enemy_collisions(self):
				                                                          ##############################
		enemy_collisions = pygame.sprite.spritecollide(self.player.sprite,self.enemies_sprite
		,False)                                                           #############################

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


	# runs the entire game / level
	def run(self):
		# run the entire game / level
		self.bground_sprite.update(self.world_shift)
		self.bground_sprite.draw(self.display_surface)


		self.ground_sprite.update(self.world_shift)
		self.ground_sprite.draw(self.display_surface)


		self.coins_sprite.update(self.world_shift)
		self.coins_sprite.draw(self.display_surface)


		self.enemies_sprite.update(self.world_shift)
		self.constraints_sprite.update(self.world_shift)
		self.enemy_collision_reverse()
		self.enemies_sprite.draw(self.display_surface)
		self.explosion_sprites.update(self.world_shift)
		self.explosion_sprites.draw(self.display_surface)





		# player sprites
		self.player.update()
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.create_landing_dust()

		self.scroll_x()
		self.player.draw(self.display_surface)
		self.goal.update(self.world_shift)
		self.goal.draw(self.display_surface)

		self.check_death()
		self.check_win()
		self.check_enemy_collisions()
		self.check_coin_collisions()
