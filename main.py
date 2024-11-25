import pygame

from config import WIDTH, HEIGHT
from menu import MainMenu



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.currentScene = MainMenu(self)

    def changeScene(self, sceneClass):
        self.currentScene = sceneClass(self)

    def run(self):
        while self.running:
            self.currentScene.events()
            self.currentScene.update()
            self.currentScene.draw()
            self.clock.tick(60)

game = Game()
game.run()
pygame.quit()
