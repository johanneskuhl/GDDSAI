import pygame

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


def create_gameover(screen, survival_time):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    # gameover text
    gameover_text = font.render("GAME OVER", True, "White")
    gameover_text_rect = gameover_text.get_rect(center=(x, y))

    # timer text
    timer_text = timer_font.render(f"YOU SURVIVED {survival_time} SECONDS", True, "White")
    timer_text_rect = timer_text.get_rect(center=(x, y + 80))

    # restart text
    restart_text = timer_font.render("PRESS R TO START AGAIN", True, "White")
    restart_text_rect = restart_text.get_rect(center=(x, y + 150))

    # change screen
    screen.blit(gameover_text, gameover_text_rect)
    screen.blit(timer_text, timer_text_rect)
    screen.blit(restart_text, restart_text_rect)

def reset_screen(enemy_rect, player_rect, enemy_position, player_position):
    enemy_position.update(0, y)
    player_position.update(x, y)

    enemy_rect.center = enemy_position
    player_rect.center = player_position


# PLAYER
player_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(player_surf, "White", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
player_rect = player_surf.get_rect(center=(x, y))
player_position = pygame.Vector2(player_rect.center)
player_speed = 150 # p/s


# ENEMY
enemy_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(enemy_surf, "Blue", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
enemy_rect = enemy_surf.get_rect(center=(0, y))
enemy_position = pygame.Vector2(enemy_rect.center)
enemy_speed = 130 # p/s


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
                    reset_screen(enemy_rect, player_rect, enemy_position, player_position)
                    start_time = pygame.time.get_ticks()
                    survival_time = 0

    dt = clock.tick(60) / 1000

    keys = pygame.key.get_pressed()

    if GAMESTATE == "GAMEOVER":
        create_gameover(screen, survival_time)

    if GAMESTATE == "ACTIVE": 
        current_time = pygame.time.get_ticks()

        survival_time = (current_time - start_time) / 1000

        player_rect = WASDmovement(dt, player_speed, player_rect, player_position, WIDTH, HEIGHT)

        enemy_rect = enemymovement(dt, player_position, enemy_position, enemy_speed, enemy_rect)

        distance = player_position.distance_to(enemy_position)
            
        screen.fill((0, 0, 0))
        screen.blit(player_surf, player_rect)
        screen.blit(enemy_surf, enemy_rect)

        if distance <= PLAYER_RADIUS * 2:
            GAMESTATE = "GAMEOVER"

    
    pygame.display.update()
    

