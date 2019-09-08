#Classes and object
class PartyAnimal:
    x=0

    def party(self):
        self.x = self.x +1
        print("So far: ", self.x)



#calling constructor
an = PartyAnimal()
print(dir(an))

print(type(an))

#calling methods
an.party()
an.party()
an.party()
an.party()