import pygame

import random

import csv 

from player import (
    WASDmovement
)

from enemy import (
    enemymovement
)
pygame.init()

# general
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# for player/enemy
PLAYER_RADIUS = 25
PLAYER_SIZE = PLAYER_RADIUS * 2
x = WIDTH // 2
y = HEIGHT // 2
# for gamerunning 
GAMESTATE = "STARTSCREEN"
# timer for score
survival_time = 0
timer_font = pygame.font.Font(None, 50)
# for data/csv stuff
filename = "runs.csv"
# difficulty regelen
difficulty_dict = {
    "easy": {
        "enemy speed": 120, #p/s
        "spawn interval": 3 # sec/enem
    }, 
    "medium": {
        "enemy speed": 150, #p/s
        "spawn interval": 2 # sec/enem
    },
    "hard": {
        "enemy speed": 180, #p/s
        "spawn interval": 1 # sec/enem
    }
}
# gekozen diff
diff = ""

def create_gameover(screen, survival_time):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    # gameover text
    gameover_text = font.render("GAME OVER", True, "White")
    gameover_text_rect = gameover_text.get_rect(center=(x, y))

    # timer text
    timer_text = timer_font.render(f"YOU SURVIVED {survival_time:.1f} SECONDS", True, "White")
    timer_text_rect = timer_text.get_rect(center=(x, y + 80))

    # restart text
    restart_text = timer_font.render("PRESS R TO START AGAIN", True, "White")
    restart_text_rect = restart_text.get_rect(center=(x, y + 150))

    # change screen
    screen.blit(gameover_text, gameover_text_rect)
    screen.blit(timer_text, timer_text_rect)
    screen.blit(restart_text, restart_text_rect)

def create_startscreen(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)

    # explain options
    diff_choose_text = font.render("Choose difficulty:", True, "White")
    diff_choose_text_rect = diff_choose_text.get_rect(center=(x, y - 150))

    # button for easy mode
    Easy_mode_button_rect = button("Easy", 150, y + 50, "White", "Black", 50)

    # button medium 
    Medium_mode_button_rect = button("Medium", 350, y + 50, "White", "Black", 50)

    # button hard
    Hard_mode_button_rect = button("Hard", 550, y + 50, "White", "Black", 50)

    # start button
    Start_button_rect = button("READY", 600, y + 200, "White", "Green", 50)

    screen.blit(diff_choose_text, diff_choose_text_rect)
    return (
        Easy_mode_button_rect,
        Medium_mode_button_rect,
        Hard_mode_button_rect,
        Start_button_rect
    )

def button(text, x, y, color, back_color, text_size):
    font = pygame.font.Font(None, text_size)
    text_surf = font.render(text, True, color)

    width = text_surf.get_width() + 40
    height = text_surf.get_height() + 20

    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, back_color, rect, border_radius=20)

    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

    return rect

def create_enemy(speed):
    start_x, start_y = choose_start_pos()

    rect = enemy_surf.get_rect(
        center=(start_x, start_y)
    )

    position = pygame.Vector2(rect.center)

    enemy_dict = {
        "surface": enemy_surf,
        "rect": rect,
        "position": position,
        "speed": speed
    }

    return enemy_dict

def choose_start_pos():
    side = random.choice(["TOP", "BOTTOM", "LEFT", "RIGHT"])

    if side == "TOP":
        start_x = random.randint(0, WIDTH)
        start_y = 0 - PLAYER_RADIUS
    elif side == "BOTTOM":
        start_x = random.randint(0, WIDTH)
        start_y = HEIGHT + PLAYER_RADIUS
    elif side == "LEFT":
        start_x = 0 - PLAYER_RADIUS
        start_y = random.randint(0, HEIGHT)
    else: #side == "RIGHT"
        start_x = WIDTH + PLAYER_RADIUS
        start_y = random.randint(0, HEIGHT)

    return start_x, start_y

def save_run(survival_time, enemy_count, spawn_interval):
    with open(f"data/{filename}", "a", newline = "") as runs:            
        csvwriter = csv.writer(runs)

        if runs.tell() == 0:
            csvwriter.writerow(["survival time", "enemy count", "spawn interval", "difficulty"])
        
        csvwriter.writerow([survival_time, enemy_count, spawn_interval, diff])


# PLAYER
player_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(player_surf, "White", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
player_rect = player_surf.get_rect(center=(x, y))
player_position = pygame.Vector2(player_rect.center)
player_speed = 250 # p/s


# ENEMY
enemy_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(enemy_surf, "Blue", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
spawn_timer = 0
enemies = []

# timer
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
survival_time = 0

while True:
    #EVENT LOOP
    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
            pygame.quit()
            exit()
        if GAMESTATE == "GAMEOVER":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    GAMESTATE = "ACTIVE"

                    player_position.update(x, y)
                    player_rect.center = player_position

                    enemies.clear()
                    enemies.append(create_enemy(difficulty_dict[diff]["enemy speed"]))

                    spawn_timer = 0
                    start_time = pygame.time.get_ticks()
                    survival_time = 0

        if GAMESTATE == "STARTSCREEN":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Easy_mode_button_rect.collidepoint(event.pos):
                    diff = "easy"
                if Medium_mode_button_rect.collidepoint(event.pos):
                    diff = "medium"
                if Hard_mode_button_rect.collidepoint(event.pos):
                    diff = "hard"
                if diff:
                    if Start_button_rect.collidepoint(event.pos):
                        GAMESTATE = "ACTIVE"


    dt = clock.tick(60) / 1000

    if GAMESTATE == "GAMEOVER":
        create_gameover(screen, survival_time)

    if GAMESTATE == "STARTSCREEN":
        (
        Easy_mode_button_rect,
        Medium_mode_button_rect,
        Hard_mode_button_rect,
        Start_button_rect
    ) = create_startscreen(screen)

    if GAMESTATE == "ACTIVE":
        if not enemies:
            enemies = [create_enemy(difficulty_dict[diff]["enemy speed"])]

        current_time = pygame.time.get_ticks()
        survival_time = (current_time - start_time) / 1000

        player_rect = WASDmovement(
            dt,
            player_speed,
            player_rect,
            player_position,
            WIDTH,
            HEIGHT,
        )

        spawn_timer += dt

        if spawn_timer >= difficulty_dict[diff]["spawn interval"]:
            enemies.append(create_enemy(difficulty_dict[diff]["enemy speed"]))
            spawn_timer -= difficulty_dict[diff]["spawn interval"]

        enemy_count = len(enemies)

        screen.fill((0, 0, 0))

        screen.blit(player_surf, player_rect)

        for enemy in enemies:
            enemy["rect"] = enemymovement(
                dt,
                player_position,
                enemy["position"],
                enemy["speed"],
                enemy["rect"],
            )

            screen.blit(
                enemy["surface"],
                enemy["rect"],
            )

            distance = player_position.distance_to(
                enemy["position"]
            )

            if distance <= PLAYER_RADIUS * 2:
                GAMESTATE = "GAMEOVER"
                save_run(survival_time, enemy_count, difficulty_dict[diff]["spawn interval"])
                break


    
    pygame.display.update()
    

