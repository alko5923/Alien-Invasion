import pygame
import sys
from rocket_settings import Settings 
from rocket import Rocket 


class RocketGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and its resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
            self.settings.screen_height))

        pygame.display.set_caption("Rocket, Rocket Fly Away")
        self.rocket = Rocket(self)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()


    def _check_events(self):    
        # Respond to keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the rocket to the right
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the rocket to the left
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            # Move the rocket up
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the rocket down
            self.rocket.moving_down = True 
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False


    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        
        # Make the most recently drawn screen visible. 
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rr = RocketGame()
    rr.run_game()