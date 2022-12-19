import pygame
import random

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (400, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Flappy Bird")

# Load the images
background_image = pygame.image.load("background.png")
bird_image = pygame.image.load("bird.png")
pipe_image = pygame.image.load("pipe.jpeg")

# The y-coordinate of the bird
bird_y = 250

# The y-coordinate of the pipes
pipe_y = 0

# The gap between the top and bottom pipes
pipe_gap = 150

# The distance between the pipes
pipe_distance = 300

# The x-coordinate of the pipes
pipe_x = 400

# The speed of the pipes
pipe_speed = 2

# The distance traveled
distance = 0

# The font for the score
font = pygame.font.Font(None, 36)

# The game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the bird up or down based on the key pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y -= 3
    if keys[pygame.K_DOWN]:
        bird_y += 3

    # Move the pipes
    pipe_x -= pipe_speed

    # If the pipes are off the screen, reset their position
    if pipe_x < -52:
        pipe_x = 400
        pipe_y = random.randint(0, 300)

    # Increment the distance traveled
    distance += 1

    # Draw the background
    screen.blit(background_image, (0, 0))

    # Draw the pipes
    screen.blit(pipe_image, (pipe_x, pipe_y - 480))
    screen.blit(pipe_image, (pipe_x, pipe_y + pipe_gap))

    # Draw the bird
    screen.blit(bird_image, (100, bird_y))

    # Draw the score
    score = font.render(str(distance), 1, (0, 0, 0))
    screen.blit(score, (10, 10))

    # Update the display
    pygame.display.update()
