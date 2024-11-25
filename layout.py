import pygame
from config import BLACK
from grid import Grid
from scene import Scene

class Layout(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.currentSizeIndex = 0
        self.sizes = [20, 25, 40] 
        self.gridSize = self.sizes[self.currentSizeIndex]  
        self.grid = Grid(game, self.gridSize)
        self.pressed = False        
        self.buttons = {
            "start": {
                "normal": pygame.image.load("assets/button-start.png"),
                "hover": pygame.image.load("assets/button-start-hover.png"),
                "rect": pygame.image.load("assets/button-start.png").get_rect(topleft=(30, 30))
            },
            "reset": {
                "normal": pygame.image.load("assets/button-reset.png"),
                "hover": pygame.image.load("assets/button-reset-hover.png"),
                "rect": pygame.image.load("assets/button-reset.png").get_rect(topleft=(160,30))
            },
            "generate": {
                "normal": pygame.image.load("assets/button-generate.png"),
                "hover": pygame.image.load("assets/button-generate-hover.png"),
                "rect": pygame.image.load("assets/button-generate.png").get_rect(topleft=(410, 30))
            },
            "size": {
                "normal": pygame.image.load("assets/button-20.png"),
                "hover": pygame.image.load("assets/button-20-hover.png"),
                "rect": pygame.image.load("assets/button-20.png").get_rect(topleft=(540, 30))
            },
            "menu": {
                "normal": pygame.image.load("assets/button-menu.png"),
                "hover": pygame.image.load("assets/button-menu-hover.png"),
                "rect": pygame.image.load("assets/button-menu.png").get_rect(topleft=(670,30))
            }
        }



    def draw(self):
        self.game.screen.fill(BLACK)
        self.grid.draw()
        for button in self.buttons.values():
            if button["rect"].collidepoint(self.getMousePos()):
                self.game.screen.blit(button["hover"], button["rect"].topleft)
            else:
                self.game.screen.blit(button["normal"], button["rect"].topleft)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            mousePos = self.getMousePos()  
            grid_x = (mousePos[0] // self.grid.cellSize)
            grid_y = (mousePos[1] - 100) // self.grid.cellSize  
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and mousePos[1] <= 100:
                for button_name, btn in self.buttons.items():
                    if btn["rect"].collidepoint(mousePos):
                        self.pressed = True
                        match button_name:
                            case "start":
                                self.startAlgorithm()
                            case "reset":
                                self.resetGrid()
                            case "generate":
                                self.generateGrid()
                            case "size":
                                self.changeSize()
                            case "menu":
                                from menu import MainMenu
                                self.game.changeScene(MainMenu)
                                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mousePos[1] >= 100 and mousePos[0] >= 0 and mousePos[0] <= 800:  
                    if grid_x is not None and grid_y is not None:
                        if not (pygame.key.get_mods() & pygame.KMOD_CTRL): 
                            self.grid.placeWall(grid_y, grid_x)
                        else:
                            self.grid.setStart(grid_y, grid_x)  

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  
                if mousePos[1] >= 100 and mousePos[0] >= 0 and mousePos[0] <= 800:  
                    if grid_x is not None and grid_y is not None:
                        if not (pygame.key.get_mods() & pygame.KMOD_CTRL):
                            self.grid.removeWall(grid_y, grid_x)
                        else:
                            self.grid.setFinish(grid_y, grid_x)

            elif event.type == pygame.MOUSEMOTION:
                if mousePos[1] >= 100 and mousePos[0] >= 0 and mousePos[0] <= 800:  
                        if grid_x is not None and grid_y is not None:
                            if event.buttons[0]:  
                                if not (pygame.key.get_mods() & pygame.KMOD_CTRL):
                                    self.grid.placeWall(grid_y, grid_x)
                                else:
                                    self.grid.setStart(grid_y, grid_x)
                            elif event.buttons[2]:  
                                if not (pygame.key.get_mods() & pygame.KMOD_CTRL):
                                    self.grid.removeWall(grid_y, grid_x)
                                else:
                                    self.grid.setFinish(grid_y, grid_x)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.pressed = False        
                
    def changeSize(self):
        self.currentSizeIndex = (self.currentSizeIndex + 1) % len(self.sizes)
        self.gridSize = self.sizes[self.currentSizeIndex]
        self.grid = Grid(self.game, self.gridSize)
        self.buttons["size"]["normal"] = pygame.image.load(f"assets/button-{self.gridSize}.png")
        self.buttons["size"]["hover"] = pygame.image.load(f"assets/button-{self.gridSize}-hover.png")
        self.buttons["size"]["rect"] = self.buttons["size"]["normal"].get_rect(topleft=(540, 30))
        
    def resetGrid(self):
        self.grid.resetMatrix()
        self.grid = Grid(self.game, self.gridSize)
        
    def generateGrid(self):
        self.grid.generateMatrix()
        self.grid.draw()
            
    def startAlgorithm(self):
        pass