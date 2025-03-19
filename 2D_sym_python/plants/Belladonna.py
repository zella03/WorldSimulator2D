from Plant import*

class Belladonna(Plant):

    def __init__(self):
        super().__init__()
        self.name='b'
        self.strength=99
    
    def collision(self, world, organismToFight):
        if self.isAttacker == True:
            return True
        else:
            if LETTER_RANGE_ANIMAL_A < ord(organismToFight.GetName()) < LETTER_RANGE_ANIMAL_Z:
                organismToFight.SetOrganismLifespan(False)
                self.isAlive = False
                animalPos = organismToFight.GetOrganismPosition()
                world.SetOrganismVectorData(None, animalPos['y'],animalPos['x'])
                world.SetOrganismVectorData(None, self.position['y'],self.position['x'])

                world.AddCommentatorVector(reportType.CONSUMPTION,organismToFight, self,0)
                world.AddCommentatorVector(reportType.KILL, self,organismToFight,0)
        return True
    
    def GetName(self):
        return 'b'
    
    def GetOrganismFullName(self):
        return "Belladonna"
            