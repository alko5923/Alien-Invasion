import sys
import pygame
from star_settings import Settings
from star import Star
from random import randint 


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
            self._update_stars()
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


    def _create_star(self, star_number, row_number):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        random_number = randint(-10, 10)
        star.x = star_width + 2 * star_width * random_number
        star.rect.x = star.x 
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)
        

    def _create_fleet(self):
        """Create the fleet of stars."""
        # Make a star and find the number of stars in a row.
        # Spacing between two stars is equal to one star width. 
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - 2 * star_width
        number_stars_x = available_space_x // (2 * star_width)
        
        # Determine the number of rows of stars that fit onto the screen.
        available_space_y = self.settings.screen_height - 2 * star_height
        number_rows = available_space_y // (2 * star_height)
        
        # Create the full fleet of stars. 
        for row_number in range(number_rows):
            for star_number in range(number_stars_x): 
                self._create_star(star_number, row_number)
        

    def _update_stars(self):
        """Check if the fleet is at an edge, then update the positions of all 
            stars in the fleet."""
        self._check_fleet_edges()
        self.stars.update()


    def _check_fleet_edges(self):
        """Respond appropriately if any stars have reached the edge."""
        for star in self.stars.sprites():
            if star.check_edges():
                self._change_fleet_direction()
                break 

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for star in self.stars.sprites():
            star.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 
        self._count_stars()

    def _count_stars(self):
        """Count the number of stars on screen."""
        number_stars = 0
        for star in self.stars:
            number_stars += 1
            if star.rect.y > 600:
                number_stars -= 1 
        return number_stars

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        self.stars.draw(self.screen)

        self._repopulate_stars()


        # Make the most recently drawn screen visible. 
        pygame.display.flip()


    def _repopulate_stars(self):
        """If screen is empty, repopulate screen withs stars."""
        if self._count_stars() == 0:
            self._create_fleet()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = StarInvasion()
    si.run_game()

