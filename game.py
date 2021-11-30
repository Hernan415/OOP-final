import Classes.py

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




def game():
    pygame.init()


    return game
game
