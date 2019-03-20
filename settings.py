class Settings:
    def __init__(self):
        self.screen_mode = (1000, 600)
        self.bg_color = (130, 130, 230)
        self.rocket_speed_factor = 1

        # data for missiles
        self.missile_speed_factor = 0.5
        self.missile_image_path = "images/missile.bmp"
        self.missiles_allowed = 2

