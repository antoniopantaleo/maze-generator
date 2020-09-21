from random import choice
import pygame


background = (30, 30, 30)
walls = (255, 255, 255)


class Cell:

    def __init__(self, grid, x, y, size):
        self.grid = grid
        self.x = x
        self.y = y
        self.size = size
        self.up = True
        self.right = True
        self.bottom = True
        self.left = True
        self.visited = False
        self.start = False
        self.end = False

    def cell2grid(self, xOffset, yOffset):
        i = int(self.x / self.size)
        j = int(self.y / self.size)
        if i+xOffset >= 0 and i+xOffset < len(self.grid.cells) and j+yOffset >= 0 and j+yOffset < len(self.grid.cells):
            return self.grid.cells[i+xOffset][j+yOffset]
        else:
            return None

    def nextNeighbor(self):
        neighbors = []
        # Top
        up = self.cell2grid(0, -1)
        if up != None and not up.visited:
            neighbors.append(up)
        # Right
        right = self.cell2grid(1, 0)
        if right != None and not right.visited:
            neighbors.append(right)
        # Bottom
        bottom = self.cell2grid(0, 1)
        if bottom != None and not bottom.visited:
            neighbors.append(bottom)
        # Left
        left = self.cell2grid(-1, 0)
        if left != None and not left.visited:
            neighbors.append(left)
        if len(neighbors) > 0:
            return choice(neighbors)
        else:
            return None

    def removeWall(self, _next):
        x = int(self.x / self.size) - int(_next.x / self.size)
        y = int(self.y / self.size) - int(_next.y / self.size)

        if x == 1:  # Next on the left
            self.left = False
            _next.right = False
        if x == -1:  # Next on the right
            self.right = False
            _next.left = False

        if y == 1:  # Next on the top
            self.up = False
            _next.bottom = False
        if y == -1:  # Next on the bottom
            self.bottom = False
            _next.up = False

    def draw(self):
        if self.up:
            pygame.draw.line(self.grid.screen, walls,
                             (self.x, self.y), (self.x+self.size, self.y), 1)
        if self.right:
            pygame.draw.line(self.grid.screen, walls, (self.x+self.size, self.y),
                             (self.x+self.size, self.y+self.size), 1)
        if self.bottom:
            pygame.draw.line(self.grid.screen, walls, (self.x+self.size,
                                                       self.y+self.size), (self.x, self.y+self.size), 1)
        if self.left:
            pygame.draw.line(self.grid.screen, walls,
                             (self.x, self.y+self.size), (self.x, self.y), 1)
        if self.start:
            pygame.draw.circle(self.grid.screen, (255, 0, 0), (int(
                self.x + (self.size/2)), int(self.y+(self.size/2))), int(self.size/4))
        if self.end:
            pygame.draw.circle(self.grid.screen, (0, 0, 255), (int(
                self.x + (self.size/2)), int(self.y+(self.size/2))), int(self.size/4))
        if self == self.grid.current and self != self.grid.cells[0][0]:
            pygame.draw.rect(self.grid.screen, (0, 0, 255),
                             (self.x, self.y, self.size, self.size), 0)
