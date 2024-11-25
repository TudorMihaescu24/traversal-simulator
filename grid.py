import pygame
from config import State, Colors
from maze import Maze

class Grid:
    def __init__(self, game, size):
        self.game = game
        self.cellSize = 800 // size  
        self.matrixSize = size  
        self.start = (0, 0)  
        self.finish = (size - 1, size - 1)  
        self.matrixStates = self.initStateMatrix() 

    def initColorMatrix(self):
        matrixColors = [[Colors.EMPTY.value for _ in range(self.matrixSize)] for _ in range(self.matrixSize)]
        x, y = self.start
        matrixColors[x][y] = Colors.START.value  
        x, y = self.finish
        matrixColors[x][y] = Colors.FINISH.value  
        return matrixColors

    def initStateMatrix(self):
        matrixStates = [[State.EMPTY for _ in range(self.matrixSize)] for _ in range(self.matrixSize)]
        x, y = self.start
        matrixStates[x][y] = State.START 
        x, y = self.finish
        matrixStates[x][y] = State.FINISH
        return matrixStates

    def getMatrixStates(self):
        return self.matrixStates
    
    def generateMatrix(self):
        maze = Maze(self.matrixSize)
        self.matrixStates = maze.generateMaze()
    
    def resetMatrix(self):
        self.matrixStates = [[State.EMPTY for _ in range(self.matrixSize)] for _ in range(self.matrixSize)]
        self.matrixStates[self.start[0]][self.start[1]] = State.START  
        self.matrixStates[self.finish[0]][self.finish[1]] = State.FINISH 
        
    def restartMatrix(self):
        for row in range(self.matrixSize):
            for col in range(self.matrixSize):
                if self.matrixStates[row][col] not in {State.WALL, State.START, State.FINISH}:
                    self.matrixStates[row][col] = State.EMPTY
        self.matrixStates[self.start[0]][self.start[1]] = State.START  
        self.matrixStates[self.finish[0]][self.finish[1]] = State.FINISH 
                
    def colorMatrix(self):
        newMatrix = [[Colors.EMPTY.value for _ in range(self.matrixSize)] for _ in range(self.matrixSize)]
        for row in range(self.matrixSize):
            for col in range(self.matrixSize):
                match self.matrixStates[row][col]:
                    case State.EMPTY:
                        newMatrix[row][col] = Colors.EMPTY.value
                    case State.WALL:
                        newMatrix[row][col] = Colors.WALL.value
                    case State.START:
                        newMatrix[row][col] = Colors.START.value
                    case State.FINISH:
                        newMatrix[row][col] = Colors.FINISH.value
                    case State.VISITED:
                        newMatrix[row][col] = Colors.VISITED.value
                    case State.VISITING:
                        newMatrix[row][col] = Colors.VISITING.value
                    case State.PATH:
                        newMatrix[row][col] = Colors.PATH.value
                    case State.ERROR:
                        newMatrix[row][col] = Colors.ERROR.value
        return newMatrix

    def draw(self):
        coloredMatrix = self.colorMatrix()  
        for row in range(self.matrixSize):
            for col in range(self.matrixSize):
                rect = pygame.Rect(col * self.cellSize, row * self.cellSize + 100, self.cellSize, self.cellSize)
                color = coloredMatrix[row][col]  
                pygame.draw.rect(self.game.screen, color, rect)  
                pygame.draw.rect(self.game.screen, Colors.BORDER.value, rect, 1) 

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if event.button == 1:
                    if pygame.key.get_pressed()[pygame.K_LCTRL]:
                        self.setStart(mousePos)
                    else:
                        self.placeWall(mousePos) 
                elif event.button == 3: 
                    if pygame.key.get_pressed()[pygame.K_LCTRL]:
                        self.setFinish(mousePos)
                    else:
                        self.removeWall(mousePos)
                        
    def placeWall(self, row, col):
        if row in range(self.matrixSize) and col in range(self.matrixSize):
            if self.matrixStates[row][col] not in {State.START, State.FINISH}:
                self.matrixStates[row][col] = State.WALL

    def removeWall(self, row, col):
        if row in range(self.matrixSize) and col in range(self.matrixSize):
            if self.matrixStates[row][col] == State.WALL:
                self.matrixStates[row][col] = State.EMPTY

    def setStart(self, row, col):
        if row in range(self.matrixSize) and col in range(self.matrixSize):
            if self.matrixStates[row][col] != State.FINISH:
                self.matrixStates[self.start[0]][self.start[1]] = State.EMPTY  # Clear previous start
                self.start = (row, col)
                self.matrixStates[row][col] = State.START

    def setFinish(self, row, col):
        if row in range(self.matrixSize) and col in range(self.matrixSize):
            if self.matrixStates[row][col] != State.START:
                self.matrixStates[self.finish[0]][self.finish[1]] = State.EMPTY  # Clear previous finish
                self.finish = (row, col)
                self.matrixStates[row][col] = State.FINISH
            
    def getStart(self):
        return self.start
    
    def getFinish(self):
        return self.finish
    
    def getNeighbours(self, x, y):
        neighbours = []
        
        if x > 0 and self.matrixStates[x - 1][y] in {State.EMPTY, State.FINISH}:
            neighbours.append((x - 1, y))

        if x < (self.matrixSize - 1) and self.matrixStates[x + 1][y] in {State.EMPTY, State.FINISH}:
            neighbours.append((x + 1, y))

        if y > 0 and self.matrixStates[x][y - 1] in {State.EMPTY, State.FINISH}:
            neighbours.append((x, y - 1))

        if y < (self.matrixSize - 1) and self.matrixStates[x][y + 1] in {State.EMPTY, State.FINISH}:
            neighbours.append((x, y + 1))

        return neighbours
    