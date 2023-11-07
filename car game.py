import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
CAR_WIDTH, CAR_HEIGHT = 50, 100
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 100, 20
CAR_SPEED = 5
OBSTACLE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Load car image
car_img = pygame.image.load("car.jpg")
car_img = pygame.transform.scale(car_img, (CAR_WIDTH, CAR_HEIGHT))

# Initialize car position
car_x = (WIDTH - CAR_WIDTH) // 2
car_y = HEIGHT - CAR_HEIGHT - 20

# Initialize obstacle position
obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
obstacle_y = -OBSTACLE_HEIGHT

# Game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= CAR_SPEED
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += CAR_SPEED

    # Move the obstacle
    obstacle_y += OBSTACLE_SPEED

    # Collision detection
    if car_x < obstacle_x + OBSTACLE_WIDTH and car_x + CAR_WIDTH > obstacle_x and car_y < obstacle_y + OBSTACLE_HEIGHT and car_y + CAR_HEIGHT > obstacle_y:
        game_over = True

    # Respawn the obstacle when it goes off the screen
    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
        obstacle_y = -OBSTACLE_HEIGHT

    # Clear the screen
    screen.fill(WHITE)

    # Draw the car
    screen.blit(car_img, (car_x, car_y))

    # Draw the obstacle
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
