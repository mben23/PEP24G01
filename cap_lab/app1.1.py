class EnumeratorCuvant:
    def __init__(self, cuvant: str):
        self.cuvant = cuvant
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.cuvant):
            valoare = (self.i, self.cuvant[self.i])
            self.i += 1
            return valoare
        else:
            raise StopIteration

enumerator = EnumeratorCuvant("alfabet")
for i, litera in enumerator:
    print(f"{i}: {litera}")
