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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.quicksort(self.ARRAY)
                        self.ARRAY = ARRAY.copy()

                    elif event.key == pygame.K_r:
                        self.ARRAY = generate_random_values(self.VALUE_COUNT, (5, 75))
                        self.quicksort(self.ARRAY)

    def update_screen(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.draw_lines()
        pygame.display.update()
        self.clock.tick(self.TICKS)

    def draw_lines(self):
        self.window.fill(Colors.BLACK)

        array = scale_list(self.ARRAY, (1, SCREEN_HEIGHT))

        for idx, elem in enumerate(array):
            elem = round(elem)

            if idx not in self.COLOR_MAP:
                self.COLOR_MAP[idx] = Colors.WHITE

            # Positions mapping
            # Start of the line is the TOP section, Get the index and gap multiplication, and add a gap of 10
            x_axis = idx * GAP + 10

            # End of the line is the current element value sub from the total height
            y_axis = SCREEN_HEIGHT - elem

            position_1 = (x_axis, SCREEN_HEIGHT)
            position_2 = (x_axis, y_axis)

            pygame.draw.line(self.window, self.COLOR_MAP[idx], position_1, position_2)

    def partition(self, array: list, low: int, high: int):
        pivot = low
        self.COLOR_MAP[pivot] = Colors.TURQUOISE

        for i in range(low + 1, high + 1):
            self.COLOR_MAP[i] = Colors.RED
            self.update_screen()

            self.COLOR_MAP[i] = Colors.WHITE

            if array[i] <= array[low]:
                pivot += 1

                self.COLOR_MAP[pivot] = Colors.TURQUOISE
                array[i], array[pivot] = array[pivot], array[i]

        self.update_screen()

        self.COLOR_MAP[pivot] = Colors.WHITE
        array[pivot], array[low] = array[low], array[pivot]

        self.update_screen()
        self.COLOR_MAP[pivot] = Colors.GREEN

        return pivot

    def quicksort(self, array: list):
        """
        Color Coding Syntax:

        - TURQUOISE: Pivot bar
        - Green: Sorted bar
        - White: Unsorted bar
        """
        low, high = 0, len(array) - 1

        def _quicksort(array, low, high):
            if low >= high:
                return

            pivot = self.partition(array, low, high)

            _quicksort(array, low, pivot - 1)

            self.update_screen()
            for i in range(0, pivot + 1):
                self.COLOR_MAP[i] = Colors.GREEN

            _quicksort(array, pivot + 1, high)

        return _quicksort(array, low, high)
