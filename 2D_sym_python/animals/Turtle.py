from Animal import*
import random

class Turtle(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'T'
        self.strength = 2
        self.initiative = 1
    
    def action(self, world):
        side_to_go = random.randint(0,3)
        if side_to_go==0:
            world.moveOrganism(self,1)
        else: self.SetOrganismWantedPosition(self.position['x'],self.position['y'])
    
    def collision(self, world, organismToFight):
        if self.isAttacker == True:
            self.defaultAttack(world, organismToFight)
            return True
        else:
            if organismToFight.GetStrength() < 5:
                world.AddCommentatorVector(reportType.ATTACK_REFLECTED,organismToFight,None,0)
                return True
            else: return False
    
    def GetName(self):
        return 'T'
    
    def GetOrganismFullName(self):
        return "Turtle"
    