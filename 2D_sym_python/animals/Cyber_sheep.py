from Animal import*

class Cyber_sheep(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'C'
        self.strength = 11
        self.initiative = 4

    def action(self, world):
        if world.GetSizeHogweedList() == 0:
            world.moveOrganism(self, ONE_STEP)
        else:
            min = 123456
            tempX, tempY = 0, 0
            toGoX, toGoY = 0, 0
            for i in range(world.GetSizeHogweedList()):
                tempX = self.position['x'] - world.GetHogweedList(i).position['x']
                if tempX < 0: tempX*=(-1)
                tempY = self.position['y'] - world.GetHogweedList(i).position['y']
                if tempY < 0: tempY*=(-1)

                if (tempX+tempY) < min:
                    min = (tempX+tempY)
                    toGoX = world.GetHogweedList(i).position['x']
                    toGoY = world.GetHogweedList(i).position['y']
            
            if self.position['x']<toGoX:
                self.SetOrganismWantedPosition(self.position['x']+1, self.position['y'])
            elif self.position['x']>toGoX:
                self.SetOrganismWantedPosition(self.position['x']-1, self.position['y'])
            elif self.position['y']<toGoY:
                self.SetOrganismWantedPosition(self.position['x'], self.position['y']+1)
            elif self.position['y']>toGoY:
                self.SetOrganismWantedPosition(self.position['x'], self.position['y']-1)
            else:
                self.SetOrganismWantedPosition(self.position['x'], self.position['y'])
    
    def collision(self, world, organismToFight):
        if(self.isAttacker==True):
            if organismToFight.GetName()!='h':
                self.defaultAttack(world, organismToFight)
            else:
                for i in range(world.GetSizeHogweedList()):
                    if (self.wantedPos['x']==world.GetHogweedList(i).position['x']) and (self.wantedPos['y']==world.GetHogweedList(i).position['y']):
                        world.RemoveFromHogweedList(i)
                        break

                world.AddCommentatorVector(reportType.CONSUMPTION, self, organismToFight, 0)
                organismToFight.SetOrganismLifespan(False)

                plantPos = organismToFight.GetOrganismPosition()
                world.SetOrganismVectorData(None, plantPos['y'], plantPos['x'])

                world.SetOrganismVectorData(None, self.position['y'], self.position['x'])
                self.SetOrganismPosition(self.wantedPos['x'],self.wantedPos['y'])
                self.SetOrganismWantedPosition(0, 0)

                world.SetOrganismVectorData(self, self.position['y'], self.position['x'])
            return True
        return False
    
    def GetName(self):
        return 'C'
    
    def GetOrganismFullName(self):
        return "Cyber_sheep"