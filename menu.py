import pygame
from config import BLACK
from scene import Scene
from layout import Layout
from bfs import Bfs
from dfs import Dfs
from astar import Astar


class MainMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.pressed = True
        self.buttons = {
            "bfs": {
                "normal": pygame.image.load("assets/button-bfs.png"),
                "hover": pygame.image.load("assets/button-bfs-hover.png"),
                "rect": pygame.image.load("assets/button-bfs.png").get_rect(topleft=(275, 310))
            },
            "dfs": {
                "normal": pygame.image.load("assets/button-dfs.png"),
                "hover": pygame.image.load("assets/button-dfs-hover.png"),
                "rect": pygame.image.load("assets/button-dfs.png").get_rect(topleft=(275, 380))
            },
            "astar": {
                "normal": pygame.image.load("assets/button-a.png"),
                "hover": pygame.image.load("assets/button-a-hover.png"),
                "rect": pygame.image.load("assets/button-a.png").get_rect(topleft=(275, 450))
            },
            "exit": {
                "normal": pygame.image.load("assets/button-exit.png"),
                "hover": pygame.image.load("assets/button-exit-hover.png"),
                "rect": pygame.image.load("assets/button-exit.png").get_rect(topleft=(275, 520))
            }
        }

    def draw(self):
        self.game.screen.fill(BLACK)
        for button in self.buttons.values():
            if button["rect"].collidepoint(self.getMousePos()):  # Now correctly calls get_mouse_pos()
                self.game.screen.blit(button["hover"], button["rect"].topleft)
            else:
                self.game.screen.blit(button["normal"], button["rect"].topleft)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button_name, btn in self.buttons.items():
                    if btn["rect"].collidepoint(self.getMousePos()) and not self.pressed:
                        self.pressed = True
                        match button_name:
                            case "bfs":
                                self.game.changeScene(Bfs)
                            case "dfs":
                                self.game.changeScene(Dfs)
                            case "astar":
                                self.game.changeScene(Astar)
                            case "exit":
                                self.game.running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.pressed = False
