import pygame, sys

class Game():
    runners = []
    __startLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("carreraTortugas/background.png")
        pygame.display.set_caption("Carrera de bichos")
    
    def competir(self):
        gameover = False
        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
            
            self.__screen.blit(self.__background, (0,0))
            
            pygame.display.flip()
        
    


if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()