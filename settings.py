class Settings:
    """
    A class to store all settings for alien inversion
    """
    def __init__(self):
        # Screen Settings
        self.screen_width = 400
        self.screen_height = 700
        self.bg_color = (230,230,230)
        # Ship Settings
        self.ship_speed = 3.5
        self.ship_limit = 3
        # Bullet Settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        # Alien Speed
        self.alien_speed = 1.0
        self.fleet_drop_speed = .5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """
        Initialize settings that change throughout the game
        """
        self.ship_speed = 3.5
        self.bullet_speed = 5.0
        self.alien_speed = 1.0
        
        # Scoring settings
        self.alien_points = 50
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """
        Increase the speed of the game
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)