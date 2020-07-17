#instances
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print("Constructor called")

    def party(self):
        self.x = self.x + 1
        print(self.name, " X so far: ", self.x)


an = PartyAnimal("ankit")
an.party()
an.party()

j = PartyAnimal("jamal")
j.party()

