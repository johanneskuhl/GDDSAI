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
clock = pygame.time.Clock()
# for player/enemy
PLAYER_RADIUS = 25
PLAYER_SIZE = PLAYER_RADIUS * 2
x = WIDTH // 2
y = HEIGHT // 2
# for gamerunning
GAMESTATE = "ACTIVE"
# timer for score
start_time = pygame.time.get_ticks()
survival_time = 0
timer_font = pygame.font.Font(None, 50)
# for data/csv stuff
filename = "runs.csv"


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

def create_enemy():
    start_x, start_y = choose_start_pos()

    rect = enemy_surf.get_rect(
        center=(start_x, start_y)
    )

    position = pygame.Vector2(rect.center)

    enemy_dict = {
        "surface": enemy_surf,
        "rect": rect,
        "position": position,
        "speed": 150,
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
            csvwriter.writerow(["survival time", "enemy count", "spawn interval"])
        
        csvwriter.writerow([survival_time, enemy_count, spawn_interval])


# PLAYER
player_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(player_surf, "White", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
player_rect = player_surf.get_rect(center=(x, y))
player_position = pygame.Vector2(player_rect.center)
player_speed = 250 # p/s


# ENEMY
enemy_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(enemy_surf, "Blue", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
enemies = [create_enemy()]
spawn_timer = 0
spawn_interval = 2.0


while True:
    #EVENT LOOP
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if GAMESTATE == "GAMEOVER":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    GAMESTATE = "ACTIVE"

                    player_position.update(x, y)
                    player_rect.center = player_position

                    enemies.clear()
                    enemies.append(create_enemy())

                    spawn_timer = 0
                    start_time = pygame.time.get_ticks()
                    survival_time = 0

    dt = clock.tick(60) / 1000

    if GAMESTATE == "GAMEOVER":
        create_gameover(screen, survival_time)

    if GAMESTATE == "ACTIVE":
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

        if spawn_timer >= spawn_interval:
            enemies.append(create_enemy())
            spawn_timer -= spawn_interval

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
                save_run(survival_time, enemy_count, spawn_interval)
                break


    
    pygame.display.update()
    

