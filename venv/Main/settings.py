class Settings():
    """ A class o store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings"""

        # Screen settings
        self.screen_width=1200
        self.screen_height=650
        self.bg_color=(230,230,230)

        #Ship settings
        self.ship_speed_factor=2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor=3
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3

        #Alien Settings
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        # fleet_direction 1 is right , -1 is left
        self.fleet_direction=1