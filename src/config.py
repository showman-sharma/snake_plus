import pygame

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors

snake_color = (0, 204, 102)
shadow_color = (50, 50, 50)
apple_color = (204, 0, 0)
leaf_color = (0, 153, 0)
eye_color = (255, 255, 255)
pupil_color = (0, 0, 0)
fang_color = (255, 255, 255)
grass_color = (34, 139, 34)
brick_color = (139, 69, 19)
blood_color = (255, 0, 0)
rat_color = (105, 105, 105)
hedgehog_color = (160, 82, 45)
hole_color = (0, 0, 0)
mole_color = (139, 69, 19)
mole_snout_color = (165, 42, 42)
mole_nose_color = (0, 0, 0)

# Game settings
brick_size = 20
snake_block = 20
snake_normal_speed = 15
snake_slow_speed = 11.25  # 75% of normal speed
rat_speed = 11.25  # 75% of normal speed
hedgehog_speed = 7.5
mole_speed = 12

# Sounds
pygame.mixer.init()
crunch_sound = pygame.mixer.Sound("assets/sounds/crunch.mp3")
rat_squish_sound = pygame.mixer.Sound("assets/sounds/rat_squish.mp3")
snake_squish_sound = pygame.mixer.Sound("assets/sounds/snake_squish.mp3")
rat_squeak_sound = pygame.mixer.Sound("assets/sounds/rat_squeak.mp3")
hedgehog_squeak_sound = pygame.mixer.Sound("assets/sounds/hedgehog_squeak.mp3")
snake_crunch_sound = pygame.mixer.Sound("assets/sounds/snake_crunch.mp3")
mole_squeak_sound = pygame.mixer.Sound("assets/sounds/mole_squeak.mp3")
buzzer_sound = pygame.mixer.Sound("assets/sounds/buzzer.mp3") 

# Blink settings for hedgehogs
blink_interval = 250  # milliseconds
blink_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

# Load images
wood_texture = pygame.image.load("assets/images/wood_texture.png")