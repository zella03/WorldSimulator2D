from Plant import*

class Sosnowsky_hogweed(Plant):

    def __init__(self):
        super().__init__()
        self.name='h'
        self.strength=10
    
    def action(self, world):
        if self.position['x']-1 >= 0:
            self.killAnimalAround(world, self.position['x']-1,self.position['y'])
        if self.position['x']+1 < world.GetHorizSize():
            self.killAnimalAround(world, self.position['x']+1,self.position['y'])
        if self.position['y']-1 >= 0:
            self.killAnimalAround(world, self.position['x'],self.position['y']-1)
        if self.position['y']+1 < world.GetVerticSize():
            self.killAnimalAround(world, self.position['x'],self.position['y']+1)
        self.SetOrganismWantedPosition(self.position['x'],self.position['y'])
    
    def killAnimalAround(self, world, posX, posY):
        if world.GetOrganismVectorData(posY,posX) != None and (LETTER_RANGE_ANIMAL_A < ord(world.GetOrganismVectorData(posY,posX).GetName()) < LETTER_RANGE_ANIMAL_Z) and world.GetOrganismVectorData(posY,posX).GetName()!='C':
            world.GetOrganismVectorData(posY,posX).SetOrganismLifespan(False)

            world.AddCommentatorVector(reportType.KILL, self,world.GetOrganismVectorData(posY,posX),0)
            world.SetOrganismVectorData(None,posY,posX)
    
    def collision(self, world, organismToFight):
        if self.isAttacker == True:
            return True
        else:
            for i in range(world.GetSizeHogweedList()):
                if (self.position['x']==world.GetHogweedList(i).position['x']) and (self.position['y']==world.GetHogweedList(i).position['y']):
                    world.RemoveFromHogweedList(i)
                    break

            world.AddCommentatorVector(reportType.CONSUMPTION, organismToFight, self, 0)
            world.AddCommentatorVector(reportType.KILL, self, organismToFight, 0)
            organismToFight.SetOrganismLifespan(False)
            self.isAlive = False
            animalPos = organismToFight.GetOrganismPosition()
            world.SetOrganismVectorData(None, animalPos['y'], animalPos['x'])
            world.SetOrganismVectorData(None, self.position['y'], self.position['x'])
        return True
    
    def GetName(self):
        return 'h'
    
    def GetOrganismFullName(self):
        return "Sosnowsky_hogweed"