import pygame

class Scene:
    def __init__(self, game):
        self.game = game

    def events(self):
        pass
    
    def getMousePos(self):
        return pygame.mouse.get_pos()
    
    def getMousePress(self):
        return pygame.mouse.get_pressed()
    
    def update(self):
        pass

    def draw(self):
        pass