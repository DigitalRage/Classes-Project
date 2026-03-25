class GameTime:
    def __init__(self):
        self.day = 1
        self.hour = 8

    def advance(self, hours):
        if hours < 0:
            hours = 0
        self.hour += hours
        while self.hour >= 24:
            self.hour -= 24
            self.day += 1

    def get_time_string(self):
        return f"Day {self.day}, {self.hour:02d}:00"
