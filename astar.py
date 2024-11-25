import queue
import pygame
from config import State
from layout import Layout


class Astar(Layout):
    def __init__(self, game):
        super().__init__(game)
        self.start = self.grid.getStart()
        self.finish = self.grid.getFinish()
        self.matrix = self.grid.getMatrixStates()
        
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(self):
        self.start = self.grid.getStart()
        self.finish = self.grid.getFinish()
        self.matrix = self.grid.getMatrixStates()
        found = False
        
        open_set = {self.start} 
        closed_set = set()  
        g_score = {self.start: 0} 
        f_score = {self.start: self.heuristic(self.start, self.finish)} 
        pred = {}
        
        
        while open_set and not found:
            current = min(open_set, key=lambda x: f_score.get(x, float('inf')))
            if current == self.finish:
                found = True
                break
            
            open_set.remove(current)
            closed_set.add(current)
            self.matrix[current[0]][current[1]] = State.VISITED
            self.grid.draw()
            pygame.display.flip()

            neighbours = self.grid.getNeighbours(current[0], current[1])
            for neighbour in neighbours:
                if neighbour in closed_set:
                    continue 
                tentative_g_score = g_score[current] + 1
                
                if neighbour not in open_set:
                    open_set.add(neighbour)
                elif tentative_g_score >= g_score.get(neighbour, float('inf')):
                    continue

                pred[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = g_score[neighbour] + self.heuristic(neighbour, self.finish)
                self.matrix[neighbour[0]][neighbour[1]] = State.VISITING
                self.grid.draw()
                pygame.display.flip()

        if found:
            current = self.finish
            while current != self.start:
                x, y = current
                self.matrix[x][y] = State.PATH
                current = pred[current]
                self.grid.draw()
                pygame.display.flip()
            self.matrix[self.start[0]][self.start[1]] = State.PATH
            
    def startAlgorithm(self):
        self.grid.restartMatrix()
        self.grid.draw()
        pygame.display.flip()
        self.astar()
