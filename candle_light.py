import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Candle Light Effect")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 100)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CANDLE_COLOR = (255, 255, 255)  # White color for the candle body
GLOW_COLOR = (255, 255, 150)  # Light yellow for the glow effect

# Function to draw a realistic candle flame
def draw_flame(x, y, flicker):
    # Flame size and color based on flicker
    # Set maximum flame width to be less than candle body width (30)
    flame_width = min(20 + flicker, 30)  # Ensure flame width is less than or equal to 30
    flame_height = 40 + flicker * 2

    # Draw the glow effect
    pygame.draw.ellipse(screen, GLOW_COLOR, (x - flame_width // 2 , y - 10, flame_width, flame_height + 10))

    # Draw the flame using ellipses for a more realistic look
    pygame.draw.ellipse(screen, YELLOW, (x - flame_width // 2, y, flame_width, flame_height))
    pygame.draw.ellipse(screen, ORANGE, (x - flame_width // 4, y + flame_height // 4, flame_width // 2, flame_height // 2))
    pygame.draw.ellipse(screen, RED, (x - flame_width // 8, y + flame_height // 2, flame_width // 4, flame_height // 4))

# Function to draw the candle body
def draw_candle(x, y):
    candle_width = 30
    candle_height = 100
    pygame.draw.rect(screen, CANDLE_COLOR, (x - candle_width // 2, y, candle_width, candle_height))

# Main loop
def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        screen.fill(BLACK)

        # Get random flicker value
        flicker = random.randint(-5, 5)

        # Draw the candle body at the center of the screen
        candle_x = width // 2
        candle_y = height // 2

        draw_candle(candle_x, candle_y)

        # Draw the candle flame above the body
        # The flame should be drawn at the top of the candle body
        draw_flame(candle_x, candle_y - 20, flicker)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

if __name__ == "__main__":
    main()