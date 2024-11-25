import pygame
from collections import deque
from config import State
from layout import Layout

class Dfs(Layout):
    def __init__(self, game):
        super().__init__(game)
        self.start = self.grid.getStart()
        self.finish = self.grid.getFinish()
        self.matrix = self.grid.getMatrixStates()

    def dfs(self):
        self.start = self.grid.getStart()
        self.finish = self.grid.getFinish()
        self.matrix = self.grid.getMatrixStates()
        found = False
        visited = {self.start} 
        prev = {}
        
        st = deque()
        st.append(self.start)

        self.matrix[self.start[0]][self.start[1]] = State.VISITING

        while st and not found:
            current = st.pop()
            
            if current == self.finish:
                found = True
                break
            
            i, j = current
            self.matrix[i][j] = State.VISITED
            self.grid.draw()
            pygame.display.flip()
            neighbours = self.grid.getNeighbours(i, j)
            
            for neighbour in neighbours:
                if neighbour not in visited and neighbour != (-1,-1):
                    visited.add(neighbour)
                    st.append(neighbour)
                    x, y = neighbour
                    self.matrix[x][y] = State.VISITING
                    self.grid.draw()
                    pygame.display.flip()
            
                    
    
    def startAlgorithm(self):
        self.dfs()
