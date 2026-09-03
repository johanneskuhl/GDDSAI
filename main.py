import pygame

from player import (
    WASDmovement
)

from enemy import (
    enemymovement
)
pygame.init()


WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
PLAYER_RADIUS = 25
PLAYER_SIZE = PLAYER_RADIUS * 2
x = WIDTH // 2
y = HEIGHT // 2

# PLAYER
player_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(player_surf, "White", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
player_rect = player_surf.get_rect(center=(x, y))
player_position = pygame.Vector2(player_rect.center)
player_speed = 300 # p/s

# ENEMY
enemy_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(enemy_surf, "Blue", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
enemy_rect = enemy_surf.get_rect(center=(0, y))
enemy_position = pygame.Vector2(enemy_rect.center)
enemy_speed = 250 # p/s

while True:
    #EVENT LOOP
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player_rect = WASDmovement(clock, player_speed, player_rect, player_position, WIDTH, HEIGHT)

    enemy_rect = enemymovement(clock, player_position, enemy_position, enemy_speed, enemy_rect)

    distance = player_position.distance_to(enemy_position)
    if distance <= PLAYER_RADIUS * 2:
        pygame.quit()
        exit()

    
    screen.fill((0, 0, 0))
    screen.blit(player_surf, player_rect)
    screen.blit(enemy_surf, enemy_rect)
    pygame.display.update()
    

