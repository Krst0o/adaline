import pygame
import numpy as np
# GUI VARIABLES
# Colors
window_size = (264, 400)
black = (0, 0, 0)
darkgray = (50, 50, 50)
gray = (140, 140, 140)
white = (255, 255, 255)
lightgray = (170, 170, 170)
# Block seizures
block_width = 34
block_height = 34
margin = 1

# PYGAME VARIABLES
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Numbers - neural network")

# MAIN VARIABLES
grid = np.array(49 * [0])