import pygame as pg

pg.init()

# Setting the display and giving it dimensions
WIDTH, HEIGHT = 900, 900
WIN = pg.display.set_mode((WIDTH, HEIGHT))

# Setting the dimensions of Board
b_side = int(2 * WIDTH / 3)
b_x, b_y = int((WIDTH - b_side) / 2), int((HEIGHT - b_side) / 2)

# Setting a caption
pg.display.set_caption('Tic Tac Toe')

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

# Board to store values
board = [[None] * 3, [None] * 3, [None] * 3]

XO = True
winner = None

board_pos = [[(b_x, b_y), (b_x + b_side / 3 + 10, b_y), (b_x + 2 * b_side / 3 + 20, b_y)],
             [(b_x, b_y + b_side / 3 + 10), (b_x + b_side / 3 + 10, b_y + b_side / 3 + 10),
              (b_x + 2 * b_side / 3 + 20, b_y + b_side / 3 + 10)],
             [(b_x, b_y + 2 * b_side / 3 + 10), (b_x + b_side / 3 + 10, b_y + 2 * b_side / 3 + 10),
              (b_x + 2 * b_side / 3 + 20, b_y + 2 * b_side / 3 + 10)]
             ]

print(board_pos[0])
print(board_pos[1])
print(board_pos[2])

# Importing X and O images

x_img = pg.image.load("X_neon.png")
o_img = pg.image.load("o_neon.png")

x_img = pg.transform.scale(x_img, (180, 180))
o_img = pg.transform.scale(o_img, (180, 180))


# For the board lines
def draw_lines():
    # Vertical Lines

    pg.draw.line(WIN, BLACK, (b_x + b_side / 3, b_y), (b_x + b_side / 3, b_y + b_side), 10)
    pg.draw.line(WIN, BLACK, (b_x + 2 * b_side / 3, b_y), (b_x + 2 * b_side / 3, b_y + b_side), 10)

    # Horizontal Lines
    pg.draw.line(WIN, BLACK, (b_x, b_y + b_side / 3), (b_x + b_side, b_y + b_side / 3), 10)
    pg.draw.line(WIN, BLACK, (b_x, b_y + 2 * b_side / 3), (b_x + b_side, b_y + 2 * b_side / 3), 10)


def click(XO):
    x, y = pg.mouse.get_pos()
    if x in range(b_x, WIDTH - b_x) and y in range(b_y, HEIGHT - b_y):
        if x < board_pos[0][1][0] - 10:
            col = 0
        elif x < board_pos[0][2][0] - 10:
            col = 1
        else:
            col = 2

        if y < board_pos[1][0][1] - 10:
            row = 0
        elif y < board_pos[2][0][1] - 10:
            row = 1
        else:
            row = 2

        # print(col,row)
        if board[row][col] == None and winner is None:
            board[row][col] = XO
            XO = not XO

    return XO


def draw_board():
    global board, board_pos

    # find values in board which are filled and then at those positions displaying the  images
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                if board[i][j] == True:
                    WIN.blit(x_img, (board_pos[i][j][0], board_pos[i][j][1]))
                if board[i][j] == False:
                    WIN.blit(o_img, (board_pos[i][j][0], board_pos[i][j][1]))


def check_win():
    global board, winner

    # checking for winning rows
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(WIN, RED, (b_x, board_pos[row][0][1] + 100 - 5),
                         (b_x + b_side, board_pos[row][0][1] + 100 - 5), 10)

    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(WIN, RED, (board_pos[0][col][0] + 100 - 5, b_y),
                         (board_pos[0][col][0] + 100 - 5, b_y + b_side), 10)

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        # game won diagonally left to right
        winner = board[0][0]
        pg.draw.line(WIN, RED, (b_x, b_y), (b_x + b_side, b_y + b_side), 10)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        # game won diagonally right to left
        winner = board[0][2]
        pg.draw.line(WIN, RED, (b_x, b_y + b_side), (b_x + b_side, b_y), 10)

    if None not in board[0] + board[1] + board[2]:
        winner = 'draw '

    return winner


def draw_status():
    # getting the global variable draw
    # into action

    if winner is None and winner != 'draw':
        if XO:
            message = 'X' + "'s Turn"
        else:
            message = 'O' + "'s Turn"
    else:
        if XO:
            message = 'O' + " won !"
        else:
            message = 'X' + " won !"
    if winner == 'draw':
        message = "Game Draw !"

    # setting a font object
    font_s = pg.font.Font(None, 50)
    font_e = pg.font.Font(None, 50)

    # setting the font properties like
    # color and width of the text
    status_text = font_s.render(message, True, (0, 0, 0))
    end_text = font_e.render('GAME OVER PRESS R TO RESTART', True,(0,0,0))

    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    status_text_rect = status_text.get_rect(center=(b_x + (b_side / 2), b_y + b_side + 75))
    end_text_rect = end_text.get_rect(center=(b_x + (b_side / 2),75))

    WIN.blit(status_text, status_text_rect)
    if winner is not None:
        WIN.blit(end_text, end_text_rect)

    pg.display.update()


def restart():
    global board, winner, XO
    board = [[None] * 3, [None] * 3, [None] * 3]
    XO = True
    winner = None

    return board, winner, XO


def draw():
    # Background as white
    WIN.fill(WHITE)

    # Drawing the lines of tic tac toe
    draw_lines()

    draw_board()

    check_win()

    draw_status()

    pg.display.update()


# Main function of the game
def main():
    global XO
    # To set FPS
    clock = pg.time.Clock()
    run = True
    while run:
        # FPS set this is for more constant experience across all system

        draw()
        check_win()

        clock.tick(FPS)
        for event in pg.event.get():
            # For exist button
            if event.type == pg.QUIT:
                run = False

        if pg.mouse.get_pressed(5)[0]:
            XO = click(XO)

        if winner is not None:
            key_pressed = pg.key.get_pressed()
            if key_pressed[pg.K_r]:
                restart()

        draw()

    pg.quit()


if __name__ == '__main__':
    main()
