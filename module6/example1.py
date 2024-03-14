class Dogs:
    rasa = ''

    def __init__(self, rasa=None):
        if rasa:
            self.rasa = rasa
        else:
            self.rasa = 'Maidanez'

    def latra(self):
        if self.rasa == 'Doberman':
            print('Uooof Uooof')
        else:
            print('Uof Uof')

dog = Dogs()
print(dog.rasa)
dog.latra()

dog2 = Dogs(rasa='Doberman')
print(dog2.rasa)
dog2.latra()
