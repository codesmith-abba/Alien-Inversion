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
        # Bullet Settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        