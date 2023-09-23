import pygame

# Défini les couleurs
noir = (0, 0, 0)


def main():
    # Initialise Pygame
    pygame.init()

    # Défini la fenêtre de jeu
    largeur_fenetre: int = 800
    hauteur_fenetre: int = 600
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Tetris")

    # Variables du jeu
    game_over: bool = False

    # Boucle principale du jeu
    while not game_over:
        # Capture les événements de l'utilisateur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Met à jour la logique interne du jeu
        pass

        # Met à jour l'écran sur base de la logique interne
        # Efface l'écran (rempli de noir)
        fenetre.fill(noir)
        # Met à jour l'écran
        pygame.display.update()

    # Fin du jeu
    pygame.quit()


if __name__ == "__main__":
    main()
