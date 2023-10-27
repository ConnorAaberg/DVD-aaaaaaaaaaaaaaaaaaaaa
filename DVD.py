import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the window (width x height)
window_size = (1920, 1080)

# Create the blank window
screen = pygame.display.set_mode(window_size)

# Load the image
surf = pygame.image.load('images/dvd.png')

# Define the new size for the image (width x height)
new_surf_size = (226, 104.5)

# Resize the image
surf = pygame.transform.scale(surf, new_surf_size)

# Get the size of the resized image
rect = surf.get_rect()

# Set the window title
pygame.display.set_caption('DVD')

# Initialize the clock for measuring FPS
clock = pygame.time.Clock()

# Main game loop
rect_x = window_size[0] // 2 - rect.width // 2
rect_y = window_size[1] // 2 - rect.height // 2
rect_speed_x = 5
rect_speed_y = 5
running = True

font = pygame.font.Font(None, 37)  # Choose a font and font size

# Create a list to store previous positions for the line trail effect
trail_positions = []
trail_color_1 = random.randint(0,255)
trail_color_2 = random.randint(0,255)
trail_color_3 = random.randint(0,255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add the current position to the trail positions list
    trail_positions.append((rect_x + rect.width // 2, rect_y + rect.height // 2))

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Draw the line trail by connecting the positions in the trail_positions list
    if len(trail_positions) >= 2:
        pygame.draw.lines(screen, (trail_color_1, trail_color_2, trail_color_3), False, trail_positions, 2)

    # Draw the image at the current position
    screen.blit(surf, (rect_x, rect_y))

    # Check if the image hits the left or right edges of the window
    if rect_x <= 0 or rect_x >= window_size[0] - rect.width:
        rect_speed_x *= -1

    # Check if the image hits the top or bottom edges of the window
    if rect_y <= 0 or rect_y >= window_size[1] - rect.height:
        rect_speed_y *= -1

    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Calculate FPS and render it on the screen
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {int(fps)}", True, (0, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
