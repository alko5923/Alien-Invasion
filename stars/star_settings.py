class Settings:
    """A class to store all settings for Star Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings:
        self.screen_width = 1080
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

    # Star settings
        self.star_speed = 1.0 
        self.fleet_drop_speed = 1
        # fleet direction of 1 represent right; -1 represents left
        self.fleet_direction = 1 

        
