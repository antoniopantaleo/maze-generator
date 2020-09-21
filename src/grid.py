from cell import Cell
import pygame


class Grid:

    def __init__(self, size, cellDim):
        self.size = size
        self.cellDim = cellDim
        self.visited_stack = []
        self.screen = pygame.display.set_mode((size, size))
        columns = int(size/cellDim)
        rows = columns
        self.cells = [[None for j in range(rows)] for i in range(columns)]
        for i in range(rows):
            for j in range(columns):
                self.cells[i][j] = Cell(self, cellDim*i, cellDim*j, cellDim)
        self.current = self.cells[0][0]
        self.current.visited = True
        self.current.start = True
        self.cells[-1][-1].end = True
        self.visited_stack.append(self.current)
