from Plant import*

class Guarana(Plant):

    def __init__(self):
        super().__init__()
        self.name='u'
    
    def collision(self, world, organismToFight):
        if self.isAttacker==True:
            return True
        else:
            if LETTER_RANGE_ANIMAL_A < ord(organismToFight.GetName()) <LETTER_RANGE_ANIMAL_Z:
                tempStrength = organismToFight.GetStrength()*3
                organismToFight.SetOrganismStrength(tempStrength)
                world.AddCommentatorVector(reportType.STRENGTH_INC,organismToFight,None,0)
        return False
    
    def GetName(self):
        return 'u'
    
    def GetOrganismFullName(self):
        return "Guarana"