from config import State
from collections import deque
import random

class Maze():
    def __init__(self, mazeSize):
        self.mazeSize = mazeSize
        self.start = (0,0)
        self.finish = (mazeSize-1,mazeSize-1)
        self.maze = [[State.EMPTY for _ in range(self.mazeSize)] for _ in range (self.mazeSize)]
        self.visited = [[False for _ in range(self.mazeSize)] for _ in range (self.mazeSize)]
      
    def initMaze(self):
        if(self.mazeSize % 2 == 1):
            for row in range(self.mazeSize):
                for col in range(self.mazeSize):
                    if(row % 2 != 0 and col % 2 != 0):
                        self.maze[row][col] = State.WALL
        else:
            for row in range(self.mazeSize):
                for col in range(self.mazeSize):
                    if row <= self.mazeSize // 2:
                        if col <= self.mazeSize // 2:
                            if row % 2 != 0 and col % 2 != 0:
                                self.maze[row][col] = State.WALL
                        elif col > self.mazeSize // 2:
                            if row % 2 != 0 and col % 2 != 0:
                                self.maze[row][col - 1] = State.WALL
                    elif row > self.mazeSize // 2:
                        if col <= self.mazeSize // 2:
                            if row % 2 != 0 and col % 2 != 0:
                                self.maze[row - 1][col] = State.WALL
                        elif col > self.mazeSize // 2:
                            if row % 2 != 0 and col % 2 != 0:
                                self.maze[row - 1][col - 1] = State.WALL    
        
    def getNeighbours(self, x, y):
        neighbours = []
        if 0 <= x < self.mazeSize and 0 <= y < self.mazeSize:
            if x > 0 and self.maze[x - 1][y] not in {State.WALL, State.PATH}:
                neighbours.append((x - 1, y))
            if x < (self.mazeSize - 1) and self.maze[x + 1][y] not in {State.WALL, State.PATH}:
                neighbours.append((x + 1, y))
            if y > 0 and self.maze[x][y - 1] not in {State.WALL, State.PATH}:
                neighbours.append((x, y - 1))
            if y < (self.mazeSize - 1) and self.maze[x][y + 1]  not in {State.WALL, State.PATH}:
                neighbours.append((x, y + 1))
        
        return neighbours
    
    def finalizeMaze(self):
        for row in range(self.mazeSize):
            for col in range(self.mazeSize):
                match self.maze[row][col]:
                    case State.WALL:
                        self.maze[row][col] = State.WALL
                    case State.PATH:
                        self.maze[row][col] = State.EMPTY
                    case State.EMPTY:
                        self.maze[row][col] = State.WALL
                        
        self.maze[0][0] = State.START
        self.maze[self.mazeSize - 1][self.mazeSize - 1] = State.FINISH
                        
    def generateMaze(self):
        self.initMaze()
        stack = deque()
        stack.append(self.start)
        
        while stack:
            current = stack.popleft()
            x, y = current
            
            neighbours = self.getNeighbours(x, y)
            if neighbours:
                randElem = random.choice(neighbours)
                neighbours.remove(randElem)
                stack.appendleft(randElem)
                nx, ny = randElem
                
                self.maze[x][y] = State.PATH
                if randElem in stack:
                    self.maze[nx][ny] = State.WALL
                else:
                    self.maze[nx][ny] = State.PATH
                for n in neighbours:
                    stack.append(n)
          
        self.finalizeMaze()
        return self.maze