from Organism import Organism
from Defines import*

class Animal(Organism):

    def __init__(self):
        super().__init__()
        self.initiative = 0
        self.strength = 0
        self.name = ''
        self.isAlive = True
    
    def action(self, world):
        world.moveOrganism(self, ONE_STEP)
    
    def collision(self,world,organismToFight):
        if(self.isAttacker==True):
            self.defaultAttack(world, organismToFight)
            return True
        return False
    
    def defaultAttack(self, world, organismToFight):
        if organismToFight.GetOrganismLifespan()==True:

            if self.name == organismToFight.GetName():
                if world.addConcreteOrganism(self, organismToFight, NEW_ORGANISM):
                    world.AddCommentatorVector(reportType.SPAWN, self, None, 0)
                self.SetOrganismWantedPosition(0, 0)
            
            elif not organismToFight.collision(world, self):
                if self.strength == organismToFight.GetStrength() or self.strength > organismToFight.GetStrength():
                    organismToFight.SetOrganismLifespan(False)

                    world.SetOrganismVectorData(None, self.position['y'], self.position['x'])
                    self.SetOrganismPosition(self.wantedPos['x'],self.wantedPos['y'])
                    self.SetOrganismWantedPosition(0, 0)

                    world.SetOrganismVectorData(self, self.position['y'], self.position['x'])
                    world.AddCommentatorVector(reportType.ANIMAL_OR_PLANT, self, organismToFight, 0)
                else:
                    self.isAlive = False
                    self.SetOrganismWantedPosition(0, 0)
                    world.SetOrganismVectorData(None, self.position['y'], self.position['x'])
                    world.AddCommentatorVector(reportType.ANIMAL_OR_PLANT, organismToFight, self, 0)
        
        else:
            world.SetOrganismVectorData(None,self.position['y'],self.position['x'])
            self.SetOrganismPosition(self.wantedPos['x'],self.wantedPos['y'])
            self.SetOrganismWantedPosition(0,0)
            world.SetOrganismVectorData(self, self.position['y'],self.position['x'])

            world.addCommentatorVector(reportType.MOVED, self,None,0)
        return True
        