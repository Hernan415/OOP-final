import pygame
import sys
import random

# Width & height of the game screen, in pixels
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Width & height of one square, in pixels
SQUARE_SIZE = random.randint(0,40)

# Width & height of the game screen, in # of squares
GRID_WIDTH = SCREEN_WIDTH / SQUARE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / SQUARE_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
# Directions
UP = (0,-1)

#Game that has a path that changes with power ups and obstacles and you as a player have to make it to 100 points to win

#path
class Path():
    def __init__(self):

    #Width

        #Modify as time goes on, no smaller than player + obstacles width
        def drawPath(surface):
            for


##obstacles
#class Obstacles():
#    def __init__(self)
#        self.position = (0,0)
#        self.randomize_color()
#        self.randomize_poition()
#        self.randomize_size()
#
#    def randomize_position(self):
#        self.position = (
#            random.randint(0, GRID_WIDTH - 1) * SQUARE_SIZE,
#            random.randint(0, GRID_HEIGHT - 1) * SQUARE_SIZE
#        )
#    def randomize_color(self):
#        self.color = (
#            random.randint(0,128),
#            random.randint(0,128),
#            random.randint(0,128),
#        )
#    def randomize_size(self, surface):
#        r = pygame.Rect((self.position[0],self.position[1]), (SQUARE_SIZE, SQUARE_SIZE))
#        pygame.draw.rect(surface, self.color, r)
#
##player
#class Player():
#    def __init__(self)
#
#    # shape
#
#    # Cordinates
#
#        # Arrow keys
#        def handle_keys(self):
#            for event in pygame.event.get():
#                if event.type == pygame.QUIT:
#                    pygame.quit()
#                    sys.exit()
#                elif event.type == pygame.KEYDOWN:
#                    if event.key == pygame.K_UP or pygame.K_W:
#                        self.turn(UP)
#                    elif event.key == pygame.K_DOWN or pygame.K_S:
#                        self.turn(DOWN)
#                    elif event.key == pygame.K_LEFT or pygame.K_A:
#                        self.turn(LEFT)
#                    elif event.key == pygame.K_RIGHT or pygame.K_D:
#                        self.turn(RIGHT)
#
#        # increase as more power ups are eaten
#
##Power ups
#class Power():
#    def __init__(self):
#        self.position = (0,0)
#        self.randomize_color()
#        self.randomize_poition()
#        self.randomize_size()
#        self.randomize_value()
#    #Location
#    def randomize_position(self):
#        self.position = (
#            random.randint(0, GRID_WIDTH - 1) * SQUARE_SIZE,
#            random.randint(0, GRID_HEIGHT - 1) * SQUARE_SIZE
#        )
#    #color
#    def randomize_color(self):
#        self.color = (
#            random.randint(129,255),
#            random.randint(129,255),
#            random.randint(129,255),
#        )
#    #Drawing
#    def randomize_size(self, surface):
#        r = pygame.Rect((self.position[0],self.position[1]), (SQUARE_SIZE, SQUARE_SIZE))
#        pygame.draw.rect(surface, self.color, r)
#
#    #Value of points
#    def randomize_value(self):
#        self.value = (
#            random.randint(1,128)
#        )
#
##Scoreboard
#class Scoreboard():
#    #points
#        #power up - obstacles
#

def game():
    pygame.init()

    # Setup code
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    framerate = 10 # Re-draw the screen 10 times every second

    drawPath(screen)


game()
