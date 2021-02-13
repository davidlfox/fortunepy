class Teller:
    def __init__(self, colors, position, fortunes):
        self.colors = colors
        self.position = position
        self.fortunes = fortunes
    
    def toggle(self):
        self.position = not self.position
    
    def __str__(self):
        ret = (
            f'{self.colors[0]}\n'
            f'{self.position}'     
        )
        return ret