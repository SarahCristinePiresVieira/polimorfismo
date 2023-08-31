class AnimalAquatico:
    def nadando(self):
        pass

class Peixe(AnimalAquatico):
    def nadando(self):
        return "O peixe está nadando!"

class Tartaruga(AnimalAquatico):
    def nadando(self):
        return "A tartaruga está nadando."


peixe = Peixe()
tartaruga = Tartaruga()

print(peixe.nadando())
print(tartaruga.nadando())
