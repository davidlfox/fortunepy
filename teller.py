class Teller:
    def __init__(self, colors, fortunes):
        self.colors = colors
        self.fortunes = fortunes
    
    # helped debugging
    def __str__(self):
        ret = (
            f'{self.colors[0]}\n'
            f'{self.fortunes}'     
        )
        return ret