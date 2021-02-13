class Fortune:
    def __init__(self, number, fortune):
        self.number = number
        self.fortune = fortune
    
    def __str__(self):
        return f'fortune {self.number} reads "{self.fortune}"'