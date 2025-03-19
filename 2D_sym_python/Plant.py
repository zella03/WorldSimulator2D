from Organism import Organism
from Defines import*
import random

class Plant(Organism):
    
    def __init__(self):
        super().__init__()
        self.initiative = 0
        self.strength = 0
        self.position = {'x': 0, 'y': 0}
        self.wantedPos = {'x': 0, 'y': 0}
        self.name = ''
        self.isAlive = True
    
    def action(self, world):
        self.defaultAction(world)
    
    def defaultAction(self,world):
        my_chances=random.randint(1, 50)

        if my_chances==19:
            if world.addConcreteOrganism(self,self,NEW_ORGANISM):
                world.AddCommentatorVector(reportType.SPAWN,self,None,0)
        self.SetOrganismWantedPosition(self.position['x'],self.position['y'])
    
    def collision(self,world,organismToFight):
        return False
    
    def defaultAttack (self, world, organismToFight):
        return False
