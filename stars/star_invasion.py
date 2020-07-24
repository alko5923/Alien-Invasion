import sys
import pygame
from star_settings import Settings
from star import Star


class StarInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
            self.settings.screen_height))

        pygame.display.set_caption("Star Invasion")

        self.stars = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):    
        # Respond to keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

 
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()


    def _create_fleet(self):
        """Create the fleet of stars."""
        # Make a star and find the number of stars in a row.
        # Spacing between two stars is equal to one star width. 
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - 2 * star_height
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fit onto the screen.
        available_space_y = self.settings.screen_height - 2 * star_height
        number_rows = available_space_y // (2 * star_height)

        # Create the full fleet of stars. 
        for row_number in range(number_rows):
            for star_number in range(number_stars_x): 
                self._create_star(star_number, row_number)


    def _create_star(self, star_number, row_number):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x 
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        self.stars.draw(self.screen)

        # Make the most recently drawn screen visible. 
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = StarInvasion()
    si.run_game()

