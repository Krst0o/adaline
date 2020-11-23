import matplotlib.pyplot as plt
from variables import *
from training_data import *

# Draw grid
def draw_grid(received_grid):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('Arial', 16)
    label_font = pygame.font.SysFont('Arial', 18)
    for row in range(7):
        for col in range(7):
            color = white
            if received_grid[row][col] == 1:
                color = darkgray
            pygame.draw.rect(screen, color, [(block_width + 1) * col + 10, (block_height + 1) * row + 10,
                                         block_width, block_height])

    ### FIRST ROW
    # Create clear button with text
    clear_button_text = font.render("CLEAR", False, (0, 0, 0))
    clear_button = pygame.draw.rect(screen, lightgray, (0, 270, 64, 32))
    screen.blit(clear_button_text, clear_button)
    # Create up button with text
    up_button_text = font.render("UP", False, (0, 0, 0))
    up_button = pygame.draw.rect(screen, gray, (65, 270, 64, 32))
    screen.blit(up_button_text, up_button)
    # Create inverse button with text
    inverse_button_text = font.render("INVERSE", False, (0, 0, 0))
    inverse_button = pygame.draw.rect(screen, lightgray, (130, 270, 64, 32))
    screen.blit(inverse_button_text, inverse_button)
    # Create blur button with text
    blur_button_text = font.render("BLUR", False, (0, 0, 0))
    blur_button = pygame.draw.rect(screen, lightgray, (195, 270, 64, 32))
    screen.blit(blur_button_text, blur_button)

    ### SECOND ROW
    # Create left button with text
    left_button_text = font.render("LEFT", False, (0, 0, 0))
    left_button = pygame.draw.rect(screen, gray, (0, 303, 64, 32))
    screen.blit(left_button_text, left_button)
    # Create down button with text
    down_button_text = font.render("DOWN", False, (0, 0, 0))
    down_button = pygame.draw.rect(screen, gray, (65, 303, 64, 32))
    screen.blit(down_button_text, down_button)
    # Create right button with text
    right_button_text = font.render("RIGHT", False, (0, 0, 0))
    right_button = pygame.draw.rect(screen, gray, (130, 303, 64, 32))
    screen.blit(right_button_text, right_button)
    # Create exit button with text
    exit_button_text = font.render("EXIT", False, (0, 0, 0))
    exit_button = pygame.draw.rect(screen, lightgray, (195, 303, 64, 32))
    screen.blit(exit_button_text, exit_button)

    ### THIRD ROW
    # Create learn button
    learn_button_text = font.render("LEARN", False, (0, 0, 0))
    learn_button = pygame.draw.rect(screen, lightgray, (0, 336, 64, 32))
    screen.blit(learn_button_text, learn_button)
    # Create check button
    learn_button_text = font.render("CHECK", False, (0, 0, 0))
    learn_button = pygame.draw.rect(screen, lightgray, (65, 336, 64, 32))
    screen.blit(learn_button_text, learn_button)
    # Create vertical reflection button
    learn_button_text = font.render("VERTICAL", False, (0, 0, 0))
    learn_button = pygame.draw.rect(screen, lightgray, (130, 336, 64, 32))
    screen.blit(learn_button_text, learn_button)
    # Create horizontal reflection button
    learn_button_text = font.render("HORIZONTAL", False, (0, 0, 0))
    learn_button = pygame.draw.rect(screen, lightgray, (195, 336, 64, 32))
    screen.blit(learn_button_text, learn_button)

    # FOURTH ROW
    # Create label
    label0 = label_font.render("0: ", False, white)
    screen.blit(label0, (0, 375))
    pygame.draw.rect(screen, white, [20, 375, confidence[0] * 200, 20])

    label1 = label_font.render("1: ", False, white)
    screen.blit(label1, (0, 395))
    pygame.draw.rect(screen, white, [20, 395, confidence[1] * 200, 20])

    label2 = label_font.render("2: ", False, white)
    screen.blit(label2, (0, 415))
    pygame.draw.rect(screen, white, [20, 415, confidence[2] * 200, 20])

    label3 = label_font.render("3: ", False, white)
    screen.blit(label3, (0, 435))
    pygame.draw.rect(screen, white, [20, 435, confidence[3] * 200, 20])

    label4 = label_font.render("4: ", False, white)
    screen.blit(label4, (0, 455))
    pygame.draw.rect(screen, white, [20, 455, confidence[4] * 200, 20])

    label5 = label_font.render("5: ", False, white)
    screen.blit(label5, (0, 475))
    pygame.draw.rect(screen, white, [20, 475, confidence[5] * 200, 20])

    label6 = label_font.render("6: ", False, white)
    screen.blit(label6, (0, 495))
    pygame.draw.rect(screen, white, [20, 495, confidence[6] * 200, 20])

    label7 = label_font.render("7: ", False, white)
    screen.blit(label7, (0, 515))
    pygame.draw.rect(screen, white, [20, 515, confidence[7] * 200, 20])

    label8 = label_font.render("8: ", False, white)
    screen.blit(label8, (0, 535))
    pygame.draw.rect(screen, white, [20, 535, confidence[8] * 200, 20])

    label9 = label_font.render("9: ", False, white)
    screen.blit(label9, (0, 555))
    pygame.draw.rect(screen, white, [20, 555, confidence[9] * 200, 20])


# Change button color and gird value after click on proper button
def change_clicked_button(received_grid, clicked_x, clicked_y):
    # Get row and column
    row = int((clicked_y-10) / 35)
    col = int((clicked_x-10) / 35)
    # Change color and value
    if received_grid[row][col] == 0:
        received_grid[row][col] = 1
    else:
        received_grid[row][col] = 0
    return received_grid


# Set grid values to 0
def clear_grid_button(received_grid):
    for row in range(7):
        for col in range(7):
            received_grid[row][col] = 0
    return received_grid


# Turn over grid values
def inverse_grid_button(received_grid):
    for row in range(7):
        for col in range(7):
            if received_grid[row][col] == 0:
                received_grid[row][col] = 1
            else:
                received_grid[row][col] = 0
    return received_grid


# Change random button value
def blur_grid_button(received_grid):
    noise = np.random.binomial(1, 0.1, size=(7, 7))
    received_grid += noise.reshape((-1))
    received_grid = np.where(received_grid > 0, 1, 0)
    return received_grid


# Shift array
def up_grid_button(received_grid):
    received_grid = np.roll(received_grid, -1, axis=0)
    return received_grid


# Shift array
def down_grid_button(received_grid):
    received_grid = np.roll(received_grid, 1, axis=0)
    return received_grid


# Shift array
def left_grid_button(received_grid):
    received_grid = np.roll(received_grid, -1, axis=1)
    return received_grid


# Shift array
def right_grid_button(received_grid):
    received_grid = np.roll(received_grid, 1, axis=1)
    return received_grid


# Check number classification for selected values in grid
def check_grid_button(received_grid):
    for i in range(10):
        confidence[i] = adaline[i].predict(np.ravel(received_grid))



# Read data from file and train adaline
def learn_grid_button():
    print("Learn")
    for i in range(10):
        labels = np.zeros(10)
        labels[i] = 1
        adaline[i].train(training_inputs, labels)
        print("Learned {}".format(i))


def vertical_grid_button(received_grid):
    return received_grid[:, ::-1]


def horizontal_grid_button(received_grid):
    return received_grid[::-1]
