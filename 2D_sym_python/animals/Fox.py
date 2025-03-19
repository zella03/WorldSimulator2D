from Animal import*
import random

class Fox(Animal):

    def __init__(self):
        super().__init__()
        self.name='F'
        self.strength = 3
        self.initiative = 7
    
    def action(self, world):
        side_to_go = random.randint(0,3)

        if side_to_go==0:
            if self.position['x']-1 >= 0:
                self.dueToStrength(world,self.position['x']-1,self.position['y'])
            else: self.SetOrganismWantedPosition(self.position['x'],self.position['y'])
        elif side_to_go == 1:
            if self.position['x']+1 < world.GetHorizSize():
                self.dueToStrength(world,self.position['x']+1,self.position['y'])
            else: self.SetOrganismWantedPosition(self.position['x'],self.position['y'])
        elif side_to_go == 2:
            if self.position['y']-1 >= 0:
                self.dueToStrength(world,self.position['x'],self.position['y']-1)
            else: self.SetOrganismWantedPosition(self.position['x'],self.position['y'])
        elif side_to_go == 3:
            if self.position['y']+1 < world.GetVerticSize():
                self.dueToStrength(world,self.position['x'],self.position['y']+1)
            else: self.SetOrganismWantedPosition(self.position['x'],self.position['y'])
    
    def dueToStrength(self, world, posX, posY):
        org = world.GetOrganismVectorData(posY,posX)
        if (org != None and org.GetStrength() < self.GetStrength()) or org==None:
              self.SetOrganismWantedPosition(posX, posY)
        else: self.SetOrganismWantedPosition(self.position['x'], self.position['y'])
    
    def GetName(self):
        return 'F'
    
    def GetOrganismFullName(self):
        return "Fox"