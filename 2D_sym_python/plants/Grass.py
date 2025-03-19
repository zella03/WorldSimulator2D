from Plant import *

class Grass(Plant):

    def __init__(self):
        super().__init__()
        self.name='g'

    def GetName(self):
        return 'g'
    
    def GetOrganismFullName(self):
        return "Grass"