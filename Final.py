#External Libraries
import pygame
import sys
import random

#Game screen
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

#Size
OBJECT_SIZE = 20

class Player():
    def __init__(self):
        self.draw
        self.position = (0,0)
        self.color = 

    def draw(self,surface):
        r = pygame.Rect((self.position[0], self.position[1]), (OBJECT_SIZE, OBJECT_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or pygame.K_w:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN or pygame.K_s:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT or pygame.K_a:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT or pygame.K_d:
                    self.turn(RIGHT)
    def drawPath(surface):
        for y in range(0, int(GRID_HEIGHT)):
            for x in range(0, int(GRID_WIDTH)):
                if (x + y) % 2 == 0: # for all even squares
                    r = pygame.Rect((x * OBJECT_SIZE, y * OBJECT_SIZE), (OBJECT_SIZE, OBJECT_SIZE))
                    pygame.draw.rect(surface,(93, 216, 228), r)
                else: # for all odd squares
                    rr = pygame.Rect((x * OBJECT_SIZE, y * OBJECT_SIZE), (OBJECT_SIZE, OBJECT_SIZE))
                    pygame.draw.rect(surface, (84, 194, 205), rr)
#Game
def game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    player = Player()
    player.draw(screen)

    while True:
        player.handle_keys()
        drawPath(screen)



game()
