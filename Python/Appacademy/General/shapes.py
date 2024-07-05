#!/Users/cemakay/Python/.venv/bin/python

class Figur:
    def omkreds():
        return ' '


class Firkant(Figur):
    def __init__(self, bredde, højde):
        self.bredde = bredde
        self.højde = højde

    def omkreds(self):
        return 2 * (self.bredde + self.højde)
    
    
    

firkant = Firkant(3,4)
print(firkant.omkreds())
