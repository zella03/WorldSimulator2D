from Animal import*
import random

class Antelope(Animal):
    def __init__(self):
        super().__init__()
        self.name='A'
        self.strength=4
        self.initiative=4
    
    def action(self, world):
        world.moveOrganism(self,TWO_STEPS)
    
    def collision(self, world, organismToFight):
        if self.isAttacker == True:
            self.defaultAttack(world,organismToFight)
            return True
        else:
            my_chances=random.randint(0,1)
            if my_chances == 0:
                newPosition = world.posFreeAround(self)
                if newPosition['x'] != world.GetHorizSize()+1:
                    world.SetOrganismVectorData(None, self.position['y'], self.position['x'])
                    self.SetOrganismPosition(newPosition['x'], newPosition['y'])
                    world.SetOrganismVectorData(self, self.position['y'], self.position['x'])
                    world.AddCommentatorVector(reportType.MOVED, self, None, 0)
                    return True
                else: return False
            else: return False

    def GetName(self):
        return 'A'
    
    def GetOrganismFullName(self):
        return "Antelope"