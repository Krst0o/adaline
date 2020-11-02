import pygame
import numpy as np
import random
# import training inputs and variables
import data
from variables import *

# GUI INIT
pygame.init()
font = pygame.font.SysFont('comicsansms', 20)
label_font = pygame.font.SysFont('comicsansms', 28)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Adaline - neural network")

grid = np.array(1600 * [0])

# Draw grid
def draw_grid():
    global grid
    for i in range(1600):
        color = white
        if grid[i] == 1:
            color = darkgray
        pygame.draw.rect(screen, color, [(block_width + 1) * int(i % 40), (block_height + 1) * int(i / 40),
                                         block_width, block_height])
    ### FIRST ROW
    # Create clear button with text
    clear_button_text = font.render("CLEAR", False, (0, 0, 0))
    clear_button = pygame.draw.rect(screen, lightgray, (0, 270, 59, 32))
    screen.blit(clear_button_text, clear_button)
    # Create up button with text
    up_button_text = font.render("UP", False, (0, 0, 0))
    up_button = pygame.draw.rect(screen, gray, (60, 270, 59, 32))
    screen.blit(up_button_text, up_button)
    # Create inverse button with text
    inverse_button_text = font.render("INVERSE", False, (0, 0, 0))
    inverse_button = pygame.draw.rect(screen, lightgray, (120, 270, 59, 32))
    screen.blit(inverse_button_text, inverse_button)
    # Create blur button with text
    blur_button_text = font.render("BLUR", False, (0, 0, 0))
    blur_button = pygame.draw.rect(screen, lightgray, (180, 270, 59, 32))
    screen.blit(blur_button_text, blur_button)

    ### SECOND ROW
    # Create left button with text
    left_button_text = font.render("LEFT", False, (0, 0, 0))
    left_button = pygame.draw.rect(screen, gray, (0, 303, 59, 32))
    screen.blit(left_button_text, left_button)
    # Create down button with text
    down_button_text = font.render("DOWN", False, (0, 0, 0))
    down_button = pygame.draw.rect(screen, gray, (60, 303, 59, 32))
    screen.blit(down_button_text, down_button)
    # Create right button with text
    right_button_text = font.render("RIGHT", False, (0, 0, 0))
    right_button = pygame.draw.rect(screen, gray, (120, 303, 59, 32))
    screen.blit(right_button_text, right_button)
    # Create exit button with text
    exit_button_text = font.render("EXIT", False, (0, 0, 0))
    exit_button = pygame.draw.rect(screen, lightgray, (180, 303, 59, 32))
    screen.blit(exit_button_text, exit_button)

    ### THIRD ROW
    # Create learn button
    learn_button_text = font.render("LEARN", False, (0, 0, 0))
    learn_button = pygame.draw.rect(screen, lightgray, (0, 336, 59, 32))
    screen.blit(learn_button_text, learn_button)
    # Create check button
    learn_button_text = font.render("CHECK", False, (0, 0, 0))
    learn_button = pygame.draw.rect(screen, lightgray, (60, 336, 59, 32))
    screen.blit(learn_button_text, learn_button)

    # FOURTH ROW
    # Create label
    label = label_font.render(which_perceptron, 0, (255, 255, 255))
    screen.blit(label, (0, 380))

# Change button color and gird value after click on proper button
def change_clicked_button(clicked_x, clicked_y):
    global grid
    # Get row and column
    row = int(clicked_y / 6)
    col = int(clicked_x / 6)
    i = 40 * row + col
    # Change color and value
    if grid[i] == 0:
        grid[i] = 1
    else:
        grid[i] = 0

# Set grid values to 0
def clear_grid_button():
    global grid
    global which_perceptron
    for i in range(1600):
        grid[i] = 0


# Turn over grid values
def inverse_grid_button():
    global grid
    for i in range(1600):
        if grid[i] == 0:
            grid[i] = 1
        else:
            grid[i] = 0


# Change random button value
def blur_grid_button():
    global grid
    noise = np.random.binomial(1, 0.1, size=(40, 40))
    grid += noise.reshape((-1))
    grid = np.where(grid > 0, 1, 0)


# Shift array
def up_grid_button():
    global grid
    grid = grid.reshape((40, 40))
    grid = np.roll(grid, -1, axis=0)
    grid = grid.reshape((-1))

# Shift array
def down_grid_button():
    global grid
    grid = grid.reshape((40, 40))
    grid = np.roll(grid, 1, axis=0)
    grid = grid.reshape((-1))

# Shift array
def left_grid_button():
    global grid
    grid = grid.reshape((40, 40))
    grid = np.roll(grid, -1, axis=1)
    grid = grid.reshape((-1))


# Shift array
def right_grid_button():
    global grid
    grid = grid.reshape((40, 40))
    grid = np.roll(grid, 1, axis=1)
    grid = grid.reshape((-1))

# Main loop
def main():
    while True:
        # Update grid
        pygame.display.update()
        draw_grid()

        # Listen for events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked_x = pygame.mouse.get_pos()[0]
                    clicked_y = pygame.mouse.get_pos()[1]
                    # Clicked grid
                    if (clicked_x > 0 and clicked_x < 240) and (clicked_y > 0 and clicked_y < 240):
                        change_clicked_button(clicked_x, clicked_y)
                    # Clicked clear button
                    if (clicked_x >= 0 and clicked_x <= 64) and (clicked_y >= 270 and clicked_y <= 302):
                        clear_grid_button()
                    # Clicked up button
                    if (clicked_x >= 65 and clicked_x <= 129) and (clicked_y >= 270 and clicked_y < 302):
                        up_grid_button()
                    # Clicked inverse button
                    if (clicked_x >= 130 and clicked_x <= 194) and (clicked_y >= 270 and clicked_y < 302):
                        inverse_grid_button()
                    # Clicked blur button
                    if (clicked_x >= 195 and clicked_x <= 259) and (clicked_y >= 270 and clicked_y < 302):
                        blur_grid_button()
                    # Clicked left button
                    if (clicked_x >= 0 and clicked_x <= 64) and (clicked_y >= 303 and clicked_y <= 335):
                        left_grid_button()
                    # Clicked down button
                    if (clicked_x >= 65 and clicked_x <= 129) and (clicked_y >= 303 and clicked_y <= 335):
                        down_grid_button()
                    # Clicked right button
                    if (clicked_x >= 130 and clicked_x <= 194) and (clicked_y >= 303 and clicked_y <= 335):
                        right_grid_button()
                    # Clicked exit button
                    if (clicked_x >= 195 and clicked_x <= 259) and (clicked_y >= 303 and clicked_y <= 335):
                        pygame.quit()
            else:
                continue


main()