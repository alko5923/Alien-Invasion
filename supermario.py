import pygame

class SuperMario:
    """A class to manage our superhero."""

    def __init__(self, ai_game):
        """Initialize the character."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the image and get its rect
        self.image = pygame.image.load('images/supermario.bmp')
        self.rect = self.image.get_rect()

        # Start the character at the bottom center of the screen
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Draw the character at its current location."""

        self.screen.blit(self.image, self.rect)

