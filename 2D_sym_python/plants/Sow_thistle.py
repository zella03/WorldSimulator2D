from Plant import*

class Sow_thistle(Plant):

    def __init__(self):
        super().__init__()
        self.name='s'
    
    def action(self, world):
        for i in range(3):
            self.defaultAction(world)
    
    def GetName(self):
        return 's'
    
    def GetOrganismFullName(self):
        return "Sow_thistle"