import pygame

pygame.init()


WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
PLAYER_RADIUS = 25
PLAYER_SIZE = PLAYER_RADIUS * 2
x = WIDTH // 2
y = HEIGHT // 2


player_surf = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE), pygame.SRCALPHA)
pygame.draw.circle(player_surf, "White", (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
player_rect = player_surf.get_rect(center=(x, y))

player_position = pygame.Vector2(player_rect.center)
player_speed = 300 # p/s


while True:
    #EVENT LOOP
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    dt = clock.tick(60) / 1000

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


    screen.fill((0, 0, 0))
    screen.blit(player_surf, player_rect)
    pygame.display.update()
    

