from enum import Enum

import pygame


# Défini les couleurs
noir = (0, 0, 0)
gris = (43, 43, 43)
rouge = (255, 0, 36)
orange = (255, 144, 0)
jaune = (255, 224, 0)
vert = (0, 186, 50)
bleu_clair = (0, 175, 231)
bleu_fonce = (0, 92, 162)
violet = (159, 30, 144)
blanc = (255, 255, 255)


class Cellule(Enum):
    VIDE = 0
    ROUGE = 1
    ORANGE = 2
    JAUNE = 3
    VERT = 4
    BLEU_CLAIR = 5
    BLEU_FONCE = 6
    VIOLET = 7

    def couleur(self) -> tuple[int, int, int]:
        if self == Cellule.VIDE:
            return gris
        elif self == Cellule.ROUGE:
            return rouge
        elif self == Cellule.ORANGE:
            return orange
        elif self == Cellule.JAUNE:
            return jaune
        elif self == Cellule.VERT:
            return vert
        elif self == Cellule.BLEU_CLAIR:
            return bleu_clair
        elif self == Cellule.BLEU_FONCE:
            return bleu_fonce
        elif self == Cellule.VIOLET:
            return violet
        else:
            return blanc

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
    plateau = [[Cellule.VIDE for _ in range(12)] for _ in range(22)]
    taille_cellule = 25

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

        # Dessine le plateau
        origine_x = (largeur_fenetre - (12 * taille_cellule)) / 2
        origine_y = (hauteur_fenetre - (22 * taille_cellule)) / 2

        for x in range(12):
            for y in range(22):
                pygame.draw.rect(
                    fenetre,
                    plateau[y][x].couleur(),
                    (origine_x + (x * taille_cellule),
                     (origine_y + (y * taille_cellule)),
                     taille_cellule,
                     taille_cellule))

        # Met à jour l'écran
        pygame.display.update()

    # Fin du jeu
    pygame.quit()


if __name__ == "__main__":
    main()
