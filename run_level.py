import pygame

class Run_Level():

    def __init__(self):
        self.FONT = pygame.font.SysFont("monospace", 25)
        self.COLOR = pygame.Color(0)
        self.CHOIX_NIVEAU_TXT = self.FONT.render("Niveau désiré 'a', 'a' pour validé", 1, (255, 255, 255))

    def update(self, NIVEAU, screen):
        screen.blit(self.CHOIX_NIVEAU_TXT, (200, 100))
        Lancement = True
        running = True
        Victoire = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    NIVEAU += 1
                    screen.fill(self.COLOR)
                elif event.key == pygame.K_LEFT:
                    NIVEAU -= 1
                    screen.fill(self.COLOR)
                elif event.key == pygame.K_a:
                    NIVEAU = NIVEAU % 22
                    Lancement = False
        if Lancement:
            if NIVEAU % 22 != 0:
                choix_niveau = self.FONT.render(f"{NIVEAU % 22}", 1, (255, 255, 255))
            else:
                choix_niveau = self.FONT.render("Aleatoire", 1, (255, 255, 255))
            screen.blit(choix_niveau, (350, 200))
            pygame.display.flip()
        return NIVEAU, Lancement, Victoire, running