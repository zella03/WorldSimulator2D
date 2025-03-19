from abc import ABC, abstractmethod

class World:
    pass

class Organism(ABC):
    def __init__(self):
        self.initiative = 0
        self.strength = 0
        self.position = {'x': 0, 'y': 0}
        self.wantedPos = {'x': 0, 'y': 0}
        self.name = ''
        self.isAlive = True
        self.isAttacker = False

    @abstractmethod
    def defaultAttack(self, world, organismToFight):
        pass

    @abstractmethod
    def action(self, world):
        pass

    @abstractmethod
    def collision(self, world, organismToFight):
        pass

    @abstractmethod
    def GetOrganismFullName(self):
        pass

    def GetName(self):
        return self.name

    def GetStrength(self):
        return self.strength

    def GetInitiative(self):
        return self.initiative

    def SetOrganismStrength(self, strength):
        self.strength = strength

    def SetOrganismPosition(self, x, y):
        self.position['x'] = x
        self.position['y'] = y

    def SetOrganismLifespan(self, isAlive):
        self.isAlive = isAlive

    def SetOrganismWantedPosition(self, x, y):
        self.wantedPos['x'] = x
        self.wantedPos['y'] = y

    def SetOrganismIsAttacker(self, isAttacker):
        self.isAttacker = isAttacker

    def GetOrganismPosition(self):
        return self.position

    def GetOrganismWantedPosition(self):
        return self.wantedPos

    def GetOrganismLifespan(self):
        return self.isAlive

    def GetOrganismIsAttacker(self):
        return self.isAttacker

    def __del__(self):
        pass
