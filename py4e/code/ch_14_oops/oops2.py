#constructor and destructor
class PartyAnimal:
    x = 0

    def __init__(self):
        print("Constructor called")

    def party(self):
        self.x = self.x + 1
        print("X so far: ", self.x)

    def __del__(self):
        print("Destructor called", self.x)


an = PartyAnimal()
an.party()
an.party()

an = 42
print(an)
