import pygame

class Run():

    def update(self):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                #recupération des touches appuyer et faire les deplacement
                if event.key == pygame.K_RIGHT:
                    return [0, 1], running, False
                elif event.key == pygame.K_LEFT:
                    return [0, -1], running, False
                elif event.key == pygame.K_UP:
                    return [-1, 0], running, False
                elif event.key == pygame.K_DOWN:
                    return [1, 0], running, False
                elif event.key == pygame.K_a:
                    return None, running, True


        return None, running, False
