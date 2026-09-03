import pygame

pygame.init()

def enemymovement(dt, player_position, enemy_position, enemy_speed, enemy_rect):

    enemy_direction = player_position - enemy_position

    if enemy_direction.length_squared() > 0:
        enemy_direction.normalize_ip()

    enemy_position += enemy_direction * enemy_speed * dt

    enemy_rect.center = (round(enemy_position.x), round(enemy_position.y))

    return enemy_rect
