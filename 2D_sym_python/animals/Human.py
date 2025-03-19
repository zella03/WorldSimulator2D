from Animal import*

class Human(Animal):

    def __init__(self):
        super().__init__()
        self.name='H'
        self.strength = 5
        self.initiative = 4
        self.specialAbility = False
        self.abilityRounds = 0
        self.abilityStrength = 10
        self.basicStrength = 5
        self.actionToDo = ''
    
    def abilityTurnOn(self):
        self.SetOrganismStrength(self.abilityStrength)
        if (self.abilityStrength != self.basicStrength):
            self.abilityStrength-=1
            return True
        elif self.abilityRounds >=0 : 
            return False
        return True
    
    def action(self, world):
        if self.actionToDo == 'p' and self.abilityRounds == 0:
            world.AddCommentatorVector(reportType.HUMAN_GOT_AB, None, None, 0)
            self.specialAbility = True
            self.abilityRounds = 10
            self.abilityStrength = 10
        elif self.actionToDo != 'p':
            if self.actionToDo == 'up' and self.position['y'] - 1 >= 0:
                self.SetOrganismWantedPosition(self.position['x'], self.position['y'] - 1)
            elif self.actionToDo == 'right' and self.position['x'] + 1 < world.GetHorizSize():
                self.SetOrganismWantedPosition(self.position['x'] + 1, self.position['y'])
            elif self.actionToDo == 'down' and self.position['y'] + 1 < world.GetVerticSize():
                self.SetOrganismWantedPosition(self.position['x'], self.position['y'] + 1)
            elif self.actionToDo == 'left' and self.position['x'] - 1 >= 0:
                self.SetOrganismWantedPosition(self.position['x'] - 1, self.position['y'])
        
            if (self.actionToDo != ''):
                world.OrganismActionCollision(self)
                self.actionToDo==''
        else:
            self.SetOrganismWantedPosition(self.position['x'], self.position['y'])
    
    def collision(self, world, organismToFight):
        if self.specialAbility:
            if self.abilityTurnOn(): world.AddCommentatorVector(reportType.ROUND_OG_AB, self, None, 0)
            else: world.AddCommentatorVector(reportType.CANT_USE_AB, None, None, self.abilityRounds)
            self.abilityRounds-=1
            if self.abilityRounds == 0:
                self.specialAbility = False
            
        if organismToFight != None:
            if self.isAttacker == True:
                self.defaultAttack(world,organismToFight)
                return True
            else: return False
        else: return True
    

    def GetName(self):
        return 'H'

    def GetOrganismFullName(self):
        return "Human"
    
    def setActionToDo(self,actDo, world):
        self.actionToDo = actDo
        self.action(world)