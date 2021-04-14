import sys

import pygame

from .colors import Colors
from .utils import generate_random_values, scale_list

SCREEN_HEIGHT, SCREEN_WIDTH = 500, 450
GAP = 10
ARRAY = [25, 38, 80, 31, 62, 52, 36, 11, 73, 51, 43, 32, 37, 8, 14, 26, 58, 23, 13, 20]


class Quicksort:
    TICKS = 10
    VALUE_COUNT = 20

    ARRAY = ARRAY.copy()
    COLOR_MAP = {}

    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Quick sort visualization")

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
