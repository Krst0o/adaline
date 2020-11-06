from variables import *
from training_data import *
# GUI INIT
pygame.init()
from gui_functions import *


# Main loop
def main():
    global grid
    while True:
        # gui_function function
        draw_grid(grid)
        # Listen for events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    grid = np.copy(number[0][1])
                if event.key == pygame.K_1:
                    grid = np.copy(number[1][1])
                if event.key == pygame.K_2:
                    grid = np.copy(number[2][1])
                if event.key == pygame.K_3:
                    grid = np.copy(number[3][1])
                if event.key == pygame.K_4:
                    grid = np.copy(number[4][1])
                if event.key == pygame.K_5:
                    grid = np.copy(number[5][1])
                if event.key == pygame.K_6:
                    grid = np.copy(number[6][1])
                if event.key == pygame.K_7:
                    grid = np.copy(number[7][1])
                if event.key == pygame.K_8:
                    grid = np.copy(number[8][1])
                if event.key == pygame.K_9:
                    grid = np.copy(number[9][1])
                if event.key == pygame.K_UP:
                    grid = up_grid_button(grid)
                if event.key == pygame.K_DOWN:
                    grid = down_grid_button(grid)
                if event.key == pygame.K_LEFT:
                    grid = left_grid_button(grid)
                if event.key == pygame.K_RIGHT:
                    grid = right_grid_button(grid)
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked_x = pygame.mouse.get_pos()[0]
                    clicked_y = pygame.mouse.get_pos()[1]
                    # gui_function function
                    if (0 < clicked_x < 256) and (0 < clicked_y <= 264):
                        grid = change_clicked_button(grid, clicked_x, clicked_y)
                    # gui_function function
                    if (0 <= clicked_x <= 64) and (270 <= clicked_y <= 302):
                        grid = clear_grid_button(grid)
                    # gui_function function
                    if (65 <= clicked_x <= 129) and (270 <= clicked_y <= 302):
                        grid = up_grid_button(grid)
                    # gui_function function
                    if (130 <= clicked_x <= 194) and (270 <= clicked_y <= 302):
                        grid = inverse_grid_button(grid)
                    # gui_function function
                    if (195 <= clicked_x <= 259) and (270 <= clicked_y <= 302):
                        grid = blur_grid_button(grid)
                    # gui_function function
                    if (0 <= clicked_x <= 64) and (303 <= clicked_y <= 335):
                        grid = left_grid_button(grid)
                    # gui_function function
                    if (65 <= clicked_x <= 129) and (303 <= clicked_y <= 335):
                        grid = down_grid_button(grid)
                    # gui_function function
                    if (130 <= clicked_x <= 194) and (303 <= clicked_y <= 335):
                        grid = right_grid_button(grid)
                    # gui_function function
                    if (195 <= clicked_x <= 259) and (303 <= clicked_y <= 335):
                        pygame.quit()
                    # gui_function function
                    if (0 <= clicked_x <= 64) and (336 <= clicked_y <= 368):
                        learn_grid_button()
                    # gui_function function
                    if (65 <= clicked_x <= 129) and (336 <= clicked_y <= 368):
                        check_grid_button()
            else:
                continue
        pygame.display.update()


if __name__ == "__main__":
    main()