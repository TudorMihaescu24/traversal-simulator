
import queue
import pygame
from config import State
from layout import Layout


class Bfs(Layout):
    def __init__(self, game):
        super().__init__(game)
        self.start = self.grid.getStart()
        self.finish = self.grid.getFinish()
        self.matrix = self.grid.getMatrixStates()
        
    def bfs(self):
        self.start = self.grid.getStart()
        self.finish = self.grid.getFinish()
        self.matrix = self.grid.getMatrixStates()
        found = False
        visited = {self.start} 
        pred = {}
        
        
        print(f"Start: {self.start} and Finish: {self.finish}")
        q = queue.Queue()
        q.put(self.start)

        self.matrix[self.start[0]][self.start[1]] = State.VISITING

        while not q.empty() and not found:
            current = q.get()
            print(current)
            if current == self.finish:
                found = True
                break
            
            i, j = current
            self.matrix[i][j] = State.VISITED
            self.grid.draw()
            pygame.display.flip()
            neighbours = self.grid.getNeighbours(i, j)
            
            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    pred[neighbour] = current
                    q.put(neighbour)
                    x, y = neighbour
                    self.matrix[x][y] = State.VISITING
                    self.grid.draw()
                    pygame.display.flip()   

        print(found)
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
        self.bfs()
        