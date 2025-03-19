from Defines import*
from Organism import*
import pygame, sys , os
from pygame.locals import *

class Reports:
    def __init__(self):
        self.reportList=[]
        self.reportList.append("Reports: ")

    def printReports(self, screen):
        repX = 20
        if len(self.reportList)!=0:
            for i in range(len(self.reportList)):
                self.draw_text(self.reportList[i], pygame.font.Font(None,25), (0, 0, 0), screen.screen, 700, repX)
                repX+=20
    
    def reportKill(self, killing, dying):
        report = killing.GetOrganismFullName() + "killed" + dying.GetOrganismFullName()
        self.reportList.append(report)
    
    def reportConsumption (self, killing, dying):
         report = killing.GetOrganismFullName() + " eate " + dying.GetOrganismFullName()
         self.reportList.append(report)
    
    def reportSpawn(self,org_):
        report = org_.GetOrganismFullName() + " has multiplied"
        self.reportList.append(report)
    
    def reportMoved(self,org_):
        position = org_.GetOrganismWantedPosition()
        report = org_.GetOrganismFullName() + " has moved to position [" + str(position['x'])+" , "+ str(position['y'])+"]"
        self.reportList.append(report)
    
    def reportAdding(self, org_):
        position = org_.GetOrganismPosition()
        report = org_.GetOrganismFullName() + " was added at position [" + str(position['x']) + " , " + str(position['y']) + "]"
        self.reportList.append(report)
    
    def AnimalOrPlant(self,killing, dying):
        if LETTER_RANGE_ANIMAL_Z > ord(dying.GetName()) > LETTER_RANGE_ANIMAL_A:
            self.reportKill(killing,dying)
        else: self.reportConsumption(killing, dying)
    
    def strengthIncrease(self, org_):
        report = "Strength of the " + org_.GetOrganismFullName()
        report+= " increased by 3 by Guarana"
        self.reportList.append(report)
    
    def attackReflected(self,org_):
        report = "Attacks of " + org_.GetOrganismFullName()
        report += " with strength less than 5 reflected by the Turtle"
        self.reportList.append(report)
    
    def humanGotAbility(self):
        report = "Special Ability - Human strength rises to 10"
        self.reportList.append(report)
    
    def roundOfAbility(self,org_):
        ability = org_.GetStrength() - 5
        report = "Special Ability: Rounds that left - " + str(ability) + ", current strength - " + str(org_.GetStrength())
        self.reportList.append(report)

    def cantUseAbility(self,roundsToGo):
        report = "Human can't turn on his special ability for - " + str(roundsToGo) + "rounds"
        self.reportList.append(report)
    
    def fileSaved(self, fileName):
        report = "File '"+fileName+"' - saved"
        self.reportList.append(report)
    
    def fileOpened(self, fileName):
        report = "File '" + fileName + "' - opened"
        self.reportList.append(report)

    def clearReports(self):
        self.reportList.clear()
        self.reportList.append("Reports: ")
    
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)