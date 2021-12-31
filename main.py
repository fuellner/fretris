import pygame
import Fretris
import Figure
import random

from pygame.draw import line

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 37, 179)
]

pygame.init()
screen = pygame.display.set_mode((380,670))
pygame.display.set_caption("Fretris")

done = False
fps = 2
clock = pygame.time.Clock()
counter = 0
zoom = 30

game = Fretris.Fretris(20, 10)

pressing_down = False
pressing_left = False
pressing_right = False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

while not done:
    if game.state == "start":
        game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                pressing_left = True
            if event.key == pygame.K_RIGHT:
                pressing_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False
            if event.key == pygame.K_LEFT:
                pressing_left = False
            if event.key == pygame.K_RIGHT:
                pressing_right = False
        if pressing_down:
            # Methode in drop() umbennen
            game.down()
        if pressing_left:
            game.left()
        if pressing_right:
            game.right()

    screen.fill(color=WHITE)

    for i in range(game.height):
        for j in range(game.width):
            if game.field[i][j] == 0:
                color = GRAY
                just_border = 1
            else:
                color = colors[game.field[i][j]]
                just_border = 0
            pygame.draw.rect(screen, color, [30+j*zoom, 30+i*zoom, zoom, zoom], just_border)
    if game.Figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.Figure.image():
                    pygame.draw.rect(screen, game.Figure.color,
                                     [30+(j + game.Figure.x)*zoom, 30+(i + game.Figure.y)*zoom, zoom, zoom])

    gameover_font = pygame.font.SysFont('Ubuntu', 65, True, False)
    text_gameover = gameover_font.render("GAME OVER \n Press ESC", True, (255,255,12))

    if game.state == "gameover":
        screen.blit(text_gameover, [30, 250])

    score_font = pygame.font.SysFont('Ubuntu', 15, True, False)
    text_score = score_font.render("Score: " + str(game.score), True, (12, 12, 12))
    screen.blit(text_score, [0,0])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
