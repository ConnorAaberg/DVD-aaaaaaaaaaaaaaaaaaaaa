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

# Get the size of the resized image
rect = surf.get_rect()

# Set the window title
pygame.display.set_caption('DVD')

# Initialize the clock for measuring FPS
clock = pygame.time.Clock()

# Main game loop
rect_x = window_size[0] // 2 - rect.width // 2
rect_y = window_size[1] // 2 - rect.height // 2
speed = 5
rect_speed_x = speed
rect_speed_y = speed
running = True

font = pygame.font.Font(None, 37)  # Choose a font and font size

# Create a list to store previous positions for the line trail effect
trail_positions = []

# Define a variable to store the time when the last color change occurred
last_color_change_time = pygame.time.get_ticks()

# Initialize trail_color outside the loop
trail_color = (160, 32, 240)

def trailcolor():
    global last_color_change_time  # Reference the global last_color_change_time
    global trail_color  # Reference the global trail_color
    # Check if it's time to change the trail color (e.g., every 2 seconds)
    current_time = pygame.time.get_ticks()
    if current_time - last_color_change_time >= 2000:
        trail_color_1 = random.randint(0, 255)
        trail_color_2 = random.randint(0, 255)
        trail_color_3 = random.randint(0, 255)
        # Update the time of the last color change
        last_color_change_time = current_time
        # Update trail_color
        trail_color = (trail_color_1, trail_color_2, trail_color_3)
    return trail_color

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add the current position to the trail positions list
    trail_positions.append((rect_x + rect.width // 2, rect_y + rect.height // 2))

    # Fill the screen with a black background
    screen.fill((0, 0, 0))

    # Update trail_color by calling trailcolor
    trail_color = trailcolor()

    # Draw the line trail by connecting the positions in the trail_positions list
    if len(trail_positions) >= 2:
        pygame.draw.lines(screen, trail_color, False, trail_positions, 2)

    # Draw the image at the current position
    screen.blit(surf, (rect_x, rect_y))

    # Check if the image hits the left or right edges of the window
    if rect_x <= 0 or rect_x >= window_size[0] - rect.width:
        rect_speed_x *= -1.

    # Check if the image hits the top or bottom edges of the window
    if rect_y <= 0 or rect_y >= window_size[1] - rect.height:
        rect_speed_y *= -1.

    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Calculate FPS and render it on the screen
    fps = clock.get_fps()

    fps_text = font.render(f"FPS: {int(fps)}", True, (0, 255, 255))

    screen.blit(fps_text, (10, 10))

    rect_speed_x_ree = font.render(f"SPEED X:{str(rect_speed_x)}",True, (0,255,255))
    rect_speed_y_ree = font.render(f"SPEED Y:{str(rect_speed_y)}",True, (0,255,255))

    screen.blit(rect_speed_x_ree, (10, 50))
    screen.blit(rect_speed_y_ree, (10, 70))

    trail_color_text = font.render(f"TRAIL COLOR:{str(trail_color)}",True, (0,255,255))
    screen.blit(trail_color_text, (110, 10))

    pygame.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

# Quit Pygame
pygame.quit()
sys.exit()
