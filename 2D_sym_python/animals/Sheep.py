from Animal import*

class Sheep(Animal):

    def __init__(self):
        super().__init__()
        self.name='S'
        self.strength = 4
        self.initiative = 4
    
    def GetName(self):
        return 'S'
    
    def GetOrganismFullName(self):
        return "Sheep"
