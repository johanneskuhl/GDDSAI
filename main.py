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

while True:
    #EVENT LOOP
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 1

    screen.fill((0, 0, 0))
    screen.blit(player_surf, player_rect)
    pygame.display.update()
    clock.tick(60)

