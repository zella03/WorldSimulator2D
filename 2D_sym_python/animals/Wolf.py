from Animal import*

class Wolf(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'W'
        self.strength = 9
        self.initiative = 5
    
    def GetName(self):
        return 'W'
    
    def GetOrganismFullName(self):
        return "Wolf"