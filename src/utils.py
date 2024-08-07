# utils.py

import pygame
import random
import math
from config import *
import pandas as pd
import os
from snake import *
from rat import *
from hedgehog import *
from mole import *

def draw_grass(screen):
    screen.fill(grass_color)

def draw_brick_fencing(screen, brick_size, shadow_color, brick_color):
    for x in range(0, screen.get_width(), brick_size):
        pygame.draw.rect(screen, brick_color, [x, 0, brick_size, brick_size])
        pygame.draw.rect(screen, brick_color, [x, screen.get_height() - brick_size, brick_size, brick_size])
        pygame.draw.rect(screen, shadow_color, [x + 2, 2, brick_size - 4, brick_size - 4], 1)
        pygame.draw.rect(screen, shadow_color, [x + 2, screen.get_height() - brick_size + 2, brick_size - 4, brick_size - 4], 1)
    for y in range(0, screen.get_height(), brick_size):
        pygame.draw.rect(screen, brick_color, [0, y, brick_size, brick_size])
        pygame.draw.rect(screen, brick_color, [screen.get_width() - brick_size, y, brick_size, brick_size])
        pygame.draw.rect(screen, shadow_color, [2, y + 2, brick_size - 4, brick_size - 4], 1)
        pygame.draw.rect(screen, shadow_color, [screen.get_width() - brick_size + 2, y + 2, brick_size - 4, brick_size - 4], 1)

def draw_apple(screen, x, y, shadow_color, apple_color, leaf_color):
    # Draw shadow
    pygame.draw.ellipse(screen, shadow_color, [x + 4, y + 4, 20, 20])
    # Draw apple body
    pygame.draw.ellipse(screen, apple_color, [x, y, 20, 20])
    # Draw apple leaf
    pygame.draw.polygon(screen, leaf_color, [(x + 10, y), (x + 15, y - 10), (x + 5, y - 10)])
    # Draw apple leaf shadow
    pygame.draw.polygon(screen, shadow_color, [(x + 14, y+4), (x + 15, y - 10), (x + 5, y - 10)])
def message(screen, msg, color):
    font = pygame.font.SysFont(None, 50)
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [screen.get_width() / 6, screen.get_height() / 3])


def welcome_screen(screen, wood_texture):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        draw_grass(screen)
        draw_wooden_board(screen, wood_texture, "", (255, 0, 0))

        # Render the "SNAKE++" message
        msg_font = pygame.font.Font(None, 100)
        msg_surface = msg_font.render("SNAKE++", True, (255, 0, 0))
        msg_x = (screen.get_width() - msg_surface.get_width()) // 2
        msg_y = screen.get_height() // 4
        screen.blit(msg_surface, (msg_x, msg_y))

        # Draw the snake with 5 body parts reaching towards an apple
        snake_list = []
        snake_start_x = screen.get_width() // 2 - 50
        snake_start_y = screen.get_height() // 2
        for i in range(5):
            snake_list.append((snake_start_x + i * snake_block, snake_start_y))

        draw_snake(screen, snake_list, snake_block, shadow_color, eye_color, pupil_color, fang_color, snake_color)
        draw_apple(screen, snake_start_x + 5 * snake_block + 20, snake_start_y, shadow_color, apple_color, leaf_color)

        # Render the "Press enter to continue..." message
        small_font = pygame.font.Font(None, 35)
        small_msg_surface = small_font.render("Press enter to continue...", True, (255, 255, 255))
        small_msg_x = (screen.get_width() - small_msg_surface.get_width()) // 2
        small_msg_y = screen.get_height() // 2 + 50
        screen.blit(small_msg_surface, (small_msg_x, small_msg_y))

        pygame.display.flip()
def welcome_screen(screen, wood_texture):

    pygame.mixer.music.load(welcome_music)
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        draw_grass(screen)
        draw_brick_fencing(screen, brick_size, shadow_color, brick_color)
        draw_wooden_board(screen, wood_texture, "", (255, 0, 0))

        # Render the "SNAKE++" message with shadow
        msg_font = pygame.font.Font(None, 100)
        msg_surface_shadow = msg_font.render("SNAKE++", True, (50, 50, 50))  # Shadow color
        msg_surface = msg_font.render("SNAKE++", True, snake_color)  # Main color
        msg_x = (screen.get_width() - msg_surface.get_width()) // 2
        msg_y = screen.get_height() // 3
        screen.blit(msg_surface_shadow, (msg_x + 4, msg_y + 4))  # Draw shadow
        screen.blit(msg_surface, (msg_x, msg_y))  # Draw main text

        # Draw the snake with 5 body parts reaching towards an apple
        snake_list = []
        snake_start_x = screen.get_width() // 2 - 50
        snake_start_y = screen.get_height() // 2
        for i in range(5):
            snake_list.append((snake_start_x + i * snake_block, snake_start_y))

        draw_snake(screen, snake_list, snake_block, shadow_color, eye_color, pupil_color, fang_color, snake_color)
        draw_apple(screen, snake_start_x + 5 * snake_block + 20, snake_start_y, shadow_color, apple_color, leaf_color)

        # Render the "Press enter to continue..." message
        small_font = pygame.font.Font(None, 35)
        small_msg_surface = small_font.render("Press enter to continue...", True, (255, 255, 255))
        small_msg_x = (screen.get_width() - small_msg_surface.get_width()) // 2
        small_msg_y = screen.get_height() // 2 + 50
        screen.blit(small_msg_surface, (small_msg_x, small_msg_y))

        pygame.display.flip()

def create_blood_splatter(x, y, blood_splatters):
    for _ in range(20):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(5, 15)
        blood_x = x + radius * math.cos(angle)
        blood_y = y + radius * math.sin(angle)
        blood_splatters.append((blood_x, blood_y))

def draw_blood_splatter(screen, blood_splatters):
    for blood_x, blood_y in blood_splatters:
        pygame.draw.circle(screen, (255, 0, 0), (int(blood_x), int(blood_y)), 3)

def draw_wall_holes(screen, holes):
    for x, y in holes:
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 5)

def draw_wooden_board(screen, wood_texture, msg, color):
    board_width = 400
    board_height = 200
    board_x = (screen.get_width() - board_width) // 2
    board_y = (screen.get_height() - board_height) // 2

    # Draw the wooden board
    wood_texture = pygame.transform.scale(wood_texture, (board_width, board_height))
    screen.blit(wood_texture, (board_x, board_y))

    # Draw the message on the wooden board
    font = pygame.font.SysFont(None, 30)
    mesg = font.render(msg, True, color)
    text_rect = mesg.get_rect(center=(board_x + board_width // 2, board_y + board_height // 2-30))
    screen.blit(mesg, text_rect)

def draw_ring(screen, x, y, is_mole_hole=False):
    if is_mole_hole:
        pygame.draw.circle(screen, (160, 82, 45), (int(x), int(y)), 10)  # Draw the brown ring
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 5)  # Draw the small black dot inside the ring
    else:
        pygame.draw.circle(screen, (160, 82, 45), (int(x), int(y)), 20)  # Draw the brown ring
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 10)  # Draw the normal black hole

def new_apple_position():
    foodx = round(random.randrange(brick_size, screen_width - snake_block - brick_size) / 20.0) * 20.0
    foody = round(random.randrange(brick_size, screen_height - snake_block - brick_size) / 20.0) * 20.0
    return foodx, foody

def get_high_score(high_score_file=high_score_file):
    if not os.path.exists(high_score_file):
        return 0
    try:
        df = pd.read_csv(high_score_file)
        return df['score'].max()
    except Exception as e:
        print(f"Error reading high score file: {e}")
        return 0

def save_score(name, score, high_score_file=high_score_file):
    if not os.path.exists(high_score_file):
        df = pd.DataFrame(columns=['name', 'score'])
    else:
        df = pd.read_csv(high_score_file)

    new_entry = pd.DataFrame([[name, score]], columns=['name', 'score'])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(high_score_file, index=False)

def get_user_name(screen, wood_texture):
    input_box = pygame.Rect(0, 0, 140, 32)  # Initialize with zero position
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None, 32)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        draw_grass(screen)
        draw_wooden_board(screen, wood_texture, "", (255, 0, 0))
        draw_brick_fencing(screen, brick_size, shadow_color, brick_color)

        txt_surface = font.render(text, True, pygame.Color('black'))  # Render the text in black
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        input_box.x = (screen.get_width() - input_box.w) // 2  # Center the input box horizontally
        input_box.y = screen.get_height() // 2  # Center the input box vertically

        # Render the "Enter Your Name" message above the input box
        msg_font = pygame.font.Font(None, 50)
        msg_surface = msg_font.render("Enter Your Name:", True, (255, 0, 0))
        msg_x = (screen.get_width() - msg_surface.get_width()) // 2
        msg_y = input_box.y - 50  # Position the message above the input box

        # Draw the message and input box with white background
        screen.blit(msg_surface, (msg_x, msg_y))
        screen.fill((255, 255, 255), input_box)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
def difficulty_screen(screen, wood_texture):
    # Define button properties
    button_font = pygame.font.Font(None, 20)
    button_width, button_height = 100, 30
    easy_button_rect = pygame.Rect((screen.get_width() // 2 - 160, screen.get_height() // 2 + 30), (button_width, button_height))
    medium_button_rect = pygame.Rect((screen.get_width() // 2 - 50, screen.get_height() // 2 + 30), (button_width, button_height))
    hard_button_rect = pygame.Rect((screen.get_width() // 2 + 60, screen.get_height() // 2 + 30), (button_width, button_height))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button_rect.collidepoint(event.pos):
                    return easy_speed_fraction # Easy speed
                if medium_button_rect.collidepoint(event.pos):
                    return medium_speed_fraction  # Medium speed
                if hard_button_rect.collidepoint(event.pos):
                    return hard_speed_fraction  # Hard speed

        draw_grass(screen)
        draw_brick_fencing(screen, brick_size, shadow_color, brick_color)
        draw_wooden_board(screen, wood_texture, "SELECT DIFFICULTY", (255, 0, 0))

        # Draw buttons
        pygame.draw.rect(screen, (0, 255, 0), easy_button_rect)
        pygame.draw.rect(screen, (255, 255, 0), medium_button_rect)
        pygame.draw.rect(screen, (255, 0, 0), hard_button_rect)

        # Draw button text
        easy_text = button_font.render("Easy", True, (0, 0, 0))
        medium_text = button_font.render("Medium", True, (0, 0, 0))
        hard_text = button_font.render("Difficult", True, (0, 0, 0))

        screen.blit(easy_text, easy_button_rect.move(50, 15))
        screen.blit(medium_text, medium_button_rect.move(40, 15))
        screen.blit(hard_text, hard_button_rect.move(35, 15))

        pygame.display.flip()


def draw_buttons(screen, button_continue, button_quit):
    pygame.draw.rect(screen, (0, 255, 0), button_continue)
    pygame.draw.rect(screen, (255, 0, 0), button_quit)
    font = pygame.font.Font(None, 35)
    text_continue = font.render('Replay', True, (0, 0, 0))
    text_quit = font.render('Quit', True, (0, 0, 0))
    screen.blit(text_continue, (button_continue.x + 10, button_continue.y + 5))
    screen.blit(text_quit, (button_quit.x + 25, button_quit.y + 5))

def instruction_screen(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        draw_grass(screen)
        draw_brick_fencing(screen, brick_size, shadow_color, brick_color)

        # Title text
        font = pygame.font.Font(None, 50)
        title_surface = font.render("KNOW YOUR WILDLIFE", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(screen.get_width() // 3, 50))
        screen.blit(title_surface, title_rect)

        # Instructions and images
        small_font = pygame.font.Font(None, 30)
        y_offset = 100

        # Snake instruction
        snake_list = [(screen.get_width() // 3 - 200, y_offset), (screen.get_width() // 3 - 180, y_offset), (screen.get_width() // 3 - 160, y_offset)]
        draw_snake(screen, snake_list, snake_block, shadow_color, eye_color, pupil_color, fang_color, snake_color)
        snake_text = "Snake: Always hungry. Use arrow keys to feed it well."
        snake_surface = small_font.render(snake_text, True, (255, 255, 255))
        snake_rect = snake_surface.get_rect(midleft=(screen.get_width() // 3 - 130, y_offset + 10))
        screen.blit(snake_surface, snake_rect)

        y_offset += 60

        # Apple instruction
        draw_apple(screen, screen.get_width() // 3 - 200, y_offset, shadow_color, apple_color, leaf_color)
        apple_text = "Apple: Tasty and stationary. +1 point, +1 length."
        apple_surface = small_font.render(apple_text, True, (255, 255, 255))
        apple_rect = apple_surface.get_rect(midleft=(screen.get_width() // 3 - 130, y_offset + 10))
        screen.blit(apple_surface, apple_rect)

        y_offset += 60

        # Rat instruction
        draw_rat(screen, {'x': screen.get_width() // 3 - 200, 'y': y_offset}, snake_block, shadow_color, eye_color, pupil_color, fang_color, rat_color)
        rat_text = "Rat: Soft but agile. +2 points, +1 length."
        rat_surface = small_font.render(rat_text, True, (255, 255, 255))
        rat_rect = rat_surface.get_rect(midleft=(screen.get_width() // 3 - 130, y_offset + 10))
        screen.blit(rat_surface, rat_rect)

        y_offset += 60

        # Mole instruction
        draw_mole(screen, {'x': screen.get_width() // 3 - 200, 'y': y_offset}, shadow_color, eye_color, pupil_color, mole_color, mole_snout_color, mole_nose_color)
        mole_text = "Mole: Loves apples. +3 points, +1 length."
        mole_surface = small_font.render(mole_text, True, (255, 255, 255))
        mole_rect = mole_surface.get_rect(midleft=(screen.get_width() // 3 - 130, y_offset + 10))
        screen.blit(mole_surface, mole_rect)

        y_offset += 60

        # Hedgehog instruction
        draw_hedgehog(screen, {'x': screen.get_width() // 3 - 200, 'y': y_offset}, snake_block, shadow_color, eye_color, pupil_color, hedgehog_color)
        hedgehog_text = "Hedgehog: Spikey. Slows the snake down. Dodge it."
        hedgehog_surface = small_font.render(hedgehog_text, True, (255, 255, 255))
        hedgehog_rect = hedgehog_surface.get_rect(midleft=(screen.get_width() // 3 - 130, y_offset + 10))
        screen.blit(hedgehog_surface, hedgehog_rect)

        # Render the "Press enter to continue..." message
        y_offset += 80
        continue_text = "Press enter to continue..."
        continue_surface = small_font.render(continue_text, True, (255, 255, 255))
        continue_rect = continue_surface.get_rect(center=(screen.get_width() // 3, screen.get_height() - 50))
        screen.blit(continue_surface, continue_rect)

        pygame.display.flip()
