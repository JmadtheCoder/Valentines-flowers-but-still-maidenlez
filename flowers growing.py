import pygame
import math

# Initialize Pygame
pygame.init()

# Full-screen mode
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
RED = (255, 50, 50)
DARK_RED = (200, 0, 0)
BROWN = (139, 69, 19)
BLUE = (135, 206, 250)
YELLOW = (255, 223, 0)

# Flower Properties
stem_height = 0
flower_grown = False
petal_radius = 0

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLUE)  # Background sky color
    
    # Ground
    pygame.draw.rect(screen, GREEN, (0, HEIGHT - 150, WIDTH, 150))

    # Flower stem grows
    if stem_height < HEIGHT // 3:
        stem_height += 5
    else:
        flower_grown = True

    # Draw Stem
    pygame.draw.rect(screen, BROWN, (WIDTH // 2 - 10, HEIGHT - 150 - stem_height, 20, stem_height))

    # Draw Flower (Only after stem is fully grown)
    if flower_grown:
        # Expand petals
        if petal_radius < 50:
            petal_radius += 2

        center_x = WIDTH // 2
        center_y = HEIGHT - 150 - stem_height - 40

        # Petals (with shading)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x = center_x + math.cos(rad) * (petal_radius + 5)
            y = center_y + math.sin(rad) * (petal_radius + 5)
            pygame.draw.circle(screen, DARK_RED, (int(x), int(y)), petal_radius)

        # Flower Center
        pygame.draw.circle(screen, YELLOW, (center_x, center_y), petal_radius // 2)

        # Show Valentine's Message
        font = pygame.font.Font(None, 60)
        text = font.render("Can you be my Valentine?", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 250, HEIGHT // 4))

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    pygame.display.update()
    clock.tick(30)

pygame.quit()