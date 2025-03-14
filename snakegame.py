import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
WHITE, GREEN, RED, BLACK, BLUE, YELLOW = (255, 255, 255), (0, 200, 0), (200, 0, 0), (0, 0, 0), (0, 100, 200), (255, 215, 0)
FONT = pygame.font.Font(None, 30)

# Function to generate random food position
def get_random_food():
    return [random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
            random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE]

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake properties
snake = [[100, 100], [80, 100], [60, 100], [40, 100]]  # More segments to shape a snake
snake_direction = (1, 0)  # Moving right initially
food = get_random_food()
clock = pygame.time.Clock()
running = True
score = 0
speed = 10  # Initial speed

# Function to draw the snake with a more polished look
def draw_snake():
    pygame.draw.ellipse(screen, YELLOW, (*snake[0], GRID_SIZE, GRID_SIZE))  # Snake head as an ellipse
    for segment in snake[1:]:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE), border_radius=5)  # Body as rectangles with rounded edges

# Function to draw food with a circular shape
def draw_food():
    pygame.draw.ellipse(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

# Function to display score with better UI
def show_score():
    pygame.draw.rect(screen, BLACK, (5, 5, 120, 30))  # Background for score display
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
    
    # Move snake
    new_head = [snake[0][0] + snake_direction[0] * GRID_SIZE, snake[0][1] + snake_direction[1] * GRID_SIZE]
    snake.insert(0, new_head)
    
    # Check for collisions
    if new_head in snake[1:] or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
        running = False
    
    # Check if food is eaten
    if new_head == food:
        food = get_random_food()
        score += 10
        speed += 0.5  # Increase speed slightly
    else:
        snake.pop()
    
    draw_food()
    draw_snake()
    show_score()
    
    pygame.display.flip()
    clock.tick(speed)  # Control speed dynamically

pygame.quit()
sys.exit()
