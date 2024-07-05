#!/Users/cemakay/Python/.venv/bin/python


from math import pi

class Valutoaomregner:
    def __init__(self) -> None:
        self.kurs = 7.5

    def krtileur(pris):
        kurs = 7.5
        print(f'{pris}kr. giver {pris/kurs}')


    def eurtilkr(pris):
        kurs = 7.5
        print(f'{pris}kr. giver {pris*kurs}')
    

class Dyr:  
    def SigNoget():
        return 'Jeg er et dyr'

class Hund(Dyr):
    def sigNoget(self):
        return 'wuf wuf'
    def eat(self):
        return 'Jeg spiser ben'
    
class Kat(Dyr):
    def sigNoget(self):
        return 'Miaww'
    
    def eat(self):
        return 'Jeg spiser kattemad'

hund = Hund()
kat = Kat()

animallist = [hund, kat]

for animals in animallist:
    print(f'{animals.__class__.__name__} siger: {animals.eat()}')



