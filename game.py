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
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)


#Game that has a path that changes with power ups and obstacles and you as a player have to make it to 100 points to win

#path
    #Width
        #Modify as time goes on, no smaller than player + obstacles width

#obstacles
class Obstacles():
    def __init__(self)
        self.position = (0,0)
        self.randomize_color()
        self.randomize_poition()
        self.randomize_size()


    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1) * SQUARE_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * SQUARE_SIZE
        )
    def randomize_color(self):
        self.color = (
            random.randint(0,128),
            random.randint(0,128),
            random.randint(0,128),
        )
        def randomize_size(self, surface):
        r = pygame.Rect((self.position[0],self.position[1]), (SQUARE_SIZE, SQUARE_SIZE))
        pygame.draw.rect(surface, self.color, r)

#player
class Player():
    def __init__(self)
    # shape

    # Cordinates

        # Arrow keys

        # increase as more power ups are eaten

#Power ups
class Power():
    def __init__(self):
    # shape
        # random pixels between 1-20 x 1-20

    # points
        # Add points when touched
    #power up
        #increase speed depending on color

#Scoreboard
    #points
        # obstacles - power up
