import pygame
from time import sleep, time
from random import choice
from grid import Grid

background = (30, 30, 30)
walls = (255, 255, 255)

pygame.init()
RUNNING = True

grid = Grid(600, 30)

while RUNNING:
    for tneve in pygame.event.get():
        if tneve.type == pygame.QUIT:
            RUNNING = False
    grid.screen.fill(background)
    _next = grid.current.nextNeighbor()
    if _next != None:
        grid.current.removeWall(_next)
        grid.current = _next
        _next.visited = True
        grid.visited_stack.append(grid.current)
    else:
        if len(grid.visited_stack) > 0:
            grid.current = grid.visited_stack.pop()
    for i in range(len(grid.cells)):
        for j in range(len(grid.cells[i])):
            grid.cells[i][j].draw()
    pygame.display.update()
