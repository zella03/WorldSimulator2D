from Organism import Organism
from Reports import Reports
from Defines import *
import random
import pygame, sys , os
from pygame.locals import *
from animals.Fox import*
from animals.Antelope import*
from animals.Sheep import*
from animals.Turtle import*
from animals.Wolf import*
from animals.Cyber_sheep import*
from plants.Belladonna import*
from plants.Grass import*
from plants.Guarana import*
from plants.Sosnowsky_hogweed import*
from plants.Sow_thistle import*

game_folder = os.path.dirname(__file__)
texture_folder = os.path.join(game_folder, 'photos')
static_temp = True


class button:
    def __init__(self, world):
        self.data = pygame.Rect(0, 0, world.imgSize, world.imgSize)
        self.pos = {'x':0, 'y':0}

class World:
    def __init__(self):
        self.horizSize = HORIZ_SIZE
        self.verticSize = VERTIC_SIZE
        self.organisms = [[None] * DEF_MATRIX_SIZE for _ in range(DEF_MATRIX_SIZE)]
        self.imgSize = self.SetImgSize()
        self.fightList = []
        self.newOrgList = []
        self.hogweedList = []
        self.buttonList = [[None] * DEF_MATRIX_SIZE for _ in range(DEF_MATRIX_SIZE)]
        self.commentator = Reports()
        self.movementHuman = MovementSide.NONE

        for i in range(DEF_MATRIX_SIZE+1):
            randO = random.randint(1, 2)
            for j in range(randO):
                self.addRandomOrganism(i, FIGHT_LIST)
        
        self.orgImg = []
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'NullOrg.png')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Wolf.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Antelope.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Fox.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Human.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Sheep.png')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Turtle.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Cyber_sheep.png')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Belladonna.png')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Grass.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Guarana.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Sosnowsky_hogweed.jpg')).convert_alpha())
        self.orgImg.append(pygame.image.load(os.path.join(texture_folder, 'Sow_thistle.jpg')).convert_alpha())
            
    def userWorld(self):
        self.organisms.clear()
        self.fightList.clear()
        self.buttonList.clear()
        self.imgSize = self.SetImgSize()
        self.organisms = [[None] * self.GetHorizSize() for _ in range(self.GetVerticSize())]
        self.buttonList = [[button] * self.GetHorizSize() for _ in range(self.GetVerticSize())]

        for i in range(DEF_MATRIX_SIZE+1):
            randO = random.randint(1, 2)
            for j in range(randO):
                self.addRandomOrganism(i, FIGHT_LIST)


    def addRandomOrganism(self,numO,whichVect):
        organism = None
        if numO==0:
            organism = Wolf()
        elif numO == 1:
            organism = Sheep()
        elif numO== 2:
            organism = Fox()
        elif numO==3:
            organism = Turtle()
        elif numO==4: 
            organism = Antelope()
        elif numO==5:
            organism = Grass()
        elif numO==6:
            organism = Sow_thistle()
        elif numO==7:
            organism = Guarana()
        elif numO==8:
            organism = Belladonna()
        elif numO==9:
            organism = Sosnowsky_hogweed()
            self.hogweedList.append(organism)
        elif numO==10:
            organism = Cyber_sheep()
        
        position = self.randPosition()
        self.addOrganism(position, organism, whichVect, True)
    
    def addOrganism(self,position,organism,whichVect,addToList):
        
        organism.SetOrganismPosition(position['x'],position['y'])
        self.organisms[position['y']][position['x']]=organism

        if addToList:
            if whichVect == FIGHT_LIST: self.fightList.append(organism)
            elif whichVect == NEW_ORGANISM: self.newOrgList.append(organism)
    
    def addConcreteOrganism(self, first, second,whichVect):
        name = first.GetName()
        temp = self.addByName(name)

        position = self.posFreeAround(first)
        if position['x']== (self.GetHorizSize() + 1):
            position = self.posFreeAround(second)
        if position['x']!=(self.GetHorizSize() + 1):
            self.addOrganism(position,temp, whichVect, True)
            return True
        
        return False #No place for organism
    
    def addByName(self,name):
        temp=None
        if name == 'W':
            temp = Wolf()
        elif name == 'S':
            temp = Sheep()
        elif name == 'F':
            temp = Fox()
        elif name == 'T':
            temp = Turtle()
        elif name == 'A':
            temp = Antelope()
        elif name == 'g':
            temp = Grass()
        elif name == 'u':
            temp = Guarana()
        elif name == 'b':
            temp = Belladonna()
        elif name == 's':
            temp = Sow_thistle()
        elif name == 'h':
            temp = Sosnowsky_hogweed()
            self.hogweedList.append(temp)
        elif name == 'C':
            temp = Cyber_sheep()
        return temp
    
    def killOrg(self):
        index = 0
        while index < len(self.fightList):
            if self.fightList[index].GetOrganismLifespan()==False:
                self.fightList.pop(index)
            else: index += 1
    
    def randPosition(self):
        tempPoint = {'x':0,'y':0}
        rand = random.Random()

        while True:
            y = rand.randint(0, self.GetVerticSize() - 1)
            x = rand.randint(0, self.GetHorizSize() - 1)
            if self.organisms[y][x] is None:
                break
        tempPoint = {'x':x,'y':y}
        return tempPoint
    
    def posFreeAround (self, org_):
        position = org_.GetOrganismPosition()
        tempPoint = {'x':0,'y':0}

        if position['x']-1>=0 and self.organisms[position['y']][position['x']-1]==None:
            tempPoint = {'x': position['x']-1,'y': position['y']}
        elif position['x']+1<self.GetHorizSize() and self.organisms[position['y']][position['x']+1]==None:
            tempPoint = {'x': position['x']+1,'y': position['y']}
        elif position['y']-1>=0 and self.organisms[position['y']-1][position['x']]==None:
            tempPoint = {'x': position['x'],'y': position['y']-1}
        elif position['y']+1<self.GetVerticSize() and self.organisms[position['y']+1][position['x']]==None:
            tempPoint = {'x': position['x'],'y': position['y']+1}
        else:
            tempPoint = {'x':self.GetHorizSize()+1,'y':self.GetVerticSize()+1}
        return tempPoint
    
    def moveOrganism(self,organism, numFields):
        rand = random.Random()
        side_to_go = random.choice(list(sideMove)) #0,3
        position = organism.GetOrganismPosition()

        if side_to_go==sideMove.LEFT:
            if position['x'] - numFields >= 0:
                organism.SetOrganismWantedPosition(position['x'] - numFields, position['y'])
            else: organism.SetOrganismWantedPosition(position['x'], position['y'])
        elif side_to_go == sideMove.RIGHT:
            if position['x'] + numFields < self.GetHorizSize():
                organism.SetOrganismWantedPosition(position['x'] + numFields, position['y'])
            else: organism.SetOrganismWantedPosition(position['x'], position['y'])
        elif side_to_go == sideMove.UP:
            if position['y'] - numFields >= 0:
                organism.SetOrganismWantedPosition(position['x'], position['y'] - numFields)
            else: organism.SetOrganismWantedPosition(position['x'], position['y'])
        elif side_to_go == sideMove.DOWN:
            if position['y'] + numFields < self.GetVerticSize():
                organism.SetOrganismWantedPosition(position['x'], position['y'] + numFields)
            else: organism.SetOrganismWantedPosition(position['x'], position['y'])

    def makeTurn(self):
        self.sort_fight_list_by_initiative()

        for i in range(len(self.fightList)):
            if self.fightList[i].GetOrganismLifespan()==True:
                self.fightList[i].action(self)
                self.OrganismActionCollision(self.fightList[i])
        self.killOrg()

        for i in range(len(self.newOrgList)):
            self.fightList.append(self.newOrgList[i])
        self.newOrgList.clear()
    
    def OrganismActionCollision(self,org_):
        posCheck = org_.GetOrganismWantedPosition()
        posNow = org_.GetOrganismPosition()

        if (posCheck['x']!=posNow['x'] or posCheck['y']!=posNow['y']) and (self.organisms[posCheck['y']][posCheck['x']]!=None):
            org_.SetOrganismIsAttacker(True)
            self.organisms[posCheck['y']][posCheck['x']].SetOrganismIsAttacker(False)
            org_.collision(self,self.organisms[posCheck['y']][posCheck['x']])
        else:
            if org_.GetName() == 'H':
                org_.collision(self,None)
            
            self.organisms[posCheck['y']][posCheck['x']]=org_
            if posCheck['x']!=posNow['x'] or posCheck['y']!=posNow['y']:
                self.organisms[posNow['y']][posNow['x']]=None
                self.commentator.reportMoved(org_)
            org_.SetOrganismPosition(posCheck['x'],posCheck['y'])
            org_.SetOrganismWantedPosition(0,0)
    
    def drawWorld(self, screen):
        rect = {'x':10, 'y':10}
        global static_temp

        for i in range(self.GetVerticSize()):
            for j in range(self.GetHorizSize()):
                b_data = button(self)
                organism = self.GetOrganismVectorData(i, j)
                
                icon = self.getImageForOrganism(organism)
                image = pygame.transform.scale(icon, (self.imgSize, self.imgSize))

                b_data.data = pygame.Rect(rect['x'], rect['y'], self.imgSize, self.imgSize)
                #b_data.org_ = organism
                b_data.pos = {'x':j, 'y':i}
                self.buttonList[i][j] = b_data

                pygame.draw.rect(screen.screen, (255, 0, 0), self.buttonList[i][j].data)  # Draw the rectangle
                screen.screen.blit(image, self.buttonList[i][j].data.topleft)
                rect['x'] += (self.imgSize + 5)
            rect['x'] = 10
            rect['y'] += (self.imgSize + 5)

        static_temp = False

        self.commentator.printReports(screen)
        self.commentator.clearReports()
    
    def getImageForOrganism(self, organism):
        if organism == None:
            return self.orgImg[0]

        if organism.GetName() == 'W':
            return self.orgImg[1]
        elif organism.GetName() == 'A':
            return self.orgImg[2]
        elif organism.GetName() == 'F':
            return self.orgImg[3]
        elif organism.GetName() == 'H':
            return self.orgImg[4]
        elif organism.GetName() == 'S':
            return self.orgImg[5]
        elif organism.GetName() == 'T':
            return self.orgImg[6]
        elif organism.GetName() == 'C':
            return self.orgImg[7]
        elif organism.GetName() == 'b':
            return self.orgImg[8]
        elif organism.GetName() == 'g':
            return self.orgImg[9]
        elif organism.GetName() == 'u':
            return self.orgImg[10]
        elif organism.GetName() == 'h':
            return self.orgImg[11]
        elif organism.GetName() == 's':
            return self.orgImg[12]
            
    
    def AddCommentatorVector(self,whichComment, killing, dying, roundsAd):
        if whichComment == reportType.KILL: self.commentator.reportKill(killing,dying)
        elif (whichComment == reportType.CONSUMPTION): self.commentator.reportConsumption(killing, dying)
        elif (whichComment == reportType.SPAWN): self.commentator.reportSpawn(killing)
        elif (whichComment == reportType.MOVED): self.commentator.reportMoved(killing)
        elif (whichComment == reportType.STRENGTH_INC): self.commentator.strengthIncrease(killing)
        elif (whichComment == reportType.ATTACK_REFLECTED): self.commentator.attackReflected(killing)
        elif (whichComment == reportType.HUMAN_GOT_AB): self.commentator.humanGotAbility()
        elif (whichComment == reportType.ROUND_OG_AB): self.commentator.roundOfAbility(killing)
        elif (whichComment == reportType.CANT_USE_AB): self.commentator.cantUseAbility(roundsAd)
        elif (whichComment == reportType.ANIMAL_OR_PLANT): self.commentator.AnimalOrPlant(killing, dying)
        elif (whichComment == reportType.ORGANISM_ADDED): self.commentator.reportAdding(killing)
    
    def CommentatorSaveOpen(self,whichComment,fileName):
        if (whichComment == reportType.FILE_SAVED): self.commentator.fileSaved(fileName)
        elif (whichComment == reportType.FILE_OPENED): self.commentator.fileOpened(fileName)

    def CommentatorPrintOrClear(self, whichAct):
        if (whichAct == reportType.PRINT): self.commentator.printReports()
        elif (whichAct == reportType.CLEAR): self.commentator.clearReports()

    def SetHorizSize(self, horizonS):
        self.horizSize=horizonS
    
    def SetVerticSize(self,verticS):
        self.verticSize=verticS
    
    def SetMovementHumanSide(self,side):
        self.movementHuman = side
    
    def SetOrganismVectorData(self, org_, y, x):
        self.organisms[y][x]=org_
    
    def AddFightVectorData(self, org_):
        self.fightList.append(org_)

    def AddNewOrgVectorData(self,org_):
        self.newOrgList.append(org_)
    
    def SetHumanSAb(self, specialAb): #bool
        self.specialAbility=specialAb
    
    def SetAbRounds(self,abilityR):
        self.abilityRounds=abilityR
    
    def SetAbStrength(self, abilityStr):
        self.abilityStrength=abilityStr
    
    def SetSignKeyboardAcction(self, key):
        self.signKeyboard=key
    
    def SetWhoMoves(self, who):
        self.whoMoves=who
    
    def GetHorizSize(self):
        return self.horizSize
    
    def GetVerticSize(self):
        return self.verticSize
    
    def GetMovementHumanSide(self):
        return self.movementHuman
    
    def GetOrganismVectorData(self, i, j):
        return self.organisms[i][j]
    
    def GetFightVectorData(self, i):
        return self.fightList[i]
    
    def GetFightVectorSize(self):
        return len(self.fightList)
    
    def GetNewOrgVectorData(self, i):
        return self.newOrgList[i]
    
    def GetImgSize(self):
        return self.imgSize
    
    def GetHumSAb(self): #bool
        return self.specialAbility
    
    def GetAbRounds(self):
        return self.abilityRounds
    
    def GetAbStrength(self):
        return self.abilityStrength
    
    def GetSignKeyboardAcction(self):
        return self.signKeyboard
    
    def GetWhoMoves(self):
        return self.whoMoves
    
    
    def clearFightVect(self):
        self.fightList.clear()
    
    def clearNewOrgVect(self):
        self.newOrgList.clear()
    
    def clearOrganismVect(self):
        self.organisms.clear()
    
    def SetImgSize(self):
        if self.GetHorizSize()>self.GetVerticSize():
            return 600/self.GetHorizSize()
        else: 
            return 600/self.GetVerticSize()
    
    def SetImgSizeChange(self):
        if self.GetHorizSize()>self.GetVerticSize():
            self.imgSize = 600/self.GetHorizSize()
        else:
            self.imgSize = 600/self.GetVerticSize()

    def sort_fight_list_by_initiative(self):
        sorted_fight_list = sorted(self.fightList, key=lambda o: o.GetInitiative(), reverse=True)
        self.fightList = sorted_fight_list
    
    def GetHogweedList(self, i):
        return self.hogweedList[i]
    
    def RemoveFromHogweedList(self, i):
        self.hogweedList.pop(i)

    def AddHogweedList(self, org_):
        self.hogweedList.append(org_)
    
    def clearHogweedList(self):
        self.hogweedList.clear()
    
    def GetSizeHogweedList(self):
        return len(self.hogweedList)
    
    def organismsVectorResize(self):
        self.organisms = [[None] * self.GetHorizSize() for _ in range(self.GetVerticSize())]
        self.buttonList = [[button] * self.GetHorizSize() for _ in range(self.GetVerticSize())]
    
    def GetButtonData(self, i, j):
        return self.buttonList[i][j]
    
    def SetButttonData(self, i, j, organism):
        self.buttonList[i][j].org_ = organism
    