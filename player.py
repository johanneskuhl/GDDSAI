import pygame

pygame.init()

def WASDmovement(dt, player_speed, player_rect, player_position, WIDTH, HEIGHT):
    
    keys = pygame.key.get_pressed()
    direction = pygame.Vector2(0, 0)

    if keys[pygame.K_w]:
        direction.y -= 1
    if keys[pygame.K_a]:
        direction.x -= 1
    if keys[pygame.K_s]:
        direction.y += 1
    if keys[pygame.K_d]:
        direction.x += 1

    if direction.length_squared() > 0:
        direction.normalize_ip()

    player_position += direction * player_speed * dt

    half_width = player_rect.width / 2
    half_height = player_rect.height / 2

    player_position.x = max(half_width, min(WIDTH - half_width, player_position.x))
    player_position.y = max(half_height, min(HEIGHT - half_height, player_position.y))

    player_rect.center = (round(player_position.x), round(player_position.y))

    return player_rect