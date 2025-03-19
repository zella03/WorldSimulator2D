#include "Reports.h"
#include "Organism.h"
#include <iostream>
#include <string>
using namespace std;

Reports::Reports(): reportsList(1) {
	reportsList[0] = "Reports: ";
}

void Reports::printReports() {
	if (this->reportsList.size()!=NULL) {
		for (int i = 0; i < this->reportsList.size(); i++) {
			cout << this->reportsList[i] << endl;
		}
	}
}

void Reports::reportKill(Organism* killing, Organism* dying) {
	string report = killing->GetOrganismFullName()+" killed "+ dying->GetOrganismFullName();
	this->reportsList.push_back(report);
}

void Reports::reportConsumption(Organism* killing, Organism* dying) {
	string report = killing->GetOrganismFullName() + " eate " + dying->GetOrganismFullName();
	this->reportsList.push_back(report);
}

void Reports::reportSpawn(Organism* org_) {
	string report = org_->GetOrganismFullName() + " has multiplied";
	this->reportsList.push_back(report);
}

void Reports::reportMoved(Organism* org_) {
	pos position = org_->GetOrganismPosition();
	string report = org_->GetOrganismFullName() + " has moved to position [" + to_string(position.x)+" , "+ to_string(position.y)+"]";
	this->reportsList.push_back(report);
}
void Reports::clearReports() {
	this->reportsList.clear();
}

void Reports::AnimalOrPlant(Organism* killing, Organism* dying) {
	if (dying->GetName() > LETTER_RANGE_ANIMAL_A && dying->GetName() < LETTER_RANGE_ANIMAL_Z) {
		reportKill(killing, dying);
	}
	else reportConsumption(killing,dying);
}

void Reports::strengthIncrease(Organism* org_) {
	string report = "Strength of the " + org_->GetOrganismFullName();
	report+= " increased by 3 by Guarana";
	this->reportsList.push_back(report);
}

void Reports::attackReflected(Organism* org_) {
	string report = "Attacks of " + org_->GetOrganismFullName();
	report += " with strength less than 5 reflected by the Turtle";
	this->reportsList.push_back(report);
}

void Reports::humanGotAbility() {
	string report = "Special Ability - Human strength rises to 10";
	this->reportsList.push_back(report);
}

void Reports::roundOfAbility(Organism* org_) {
	int ability = org_->GetStrength() - 5;
	string report = "Special Ability: Rounds that left - " + to_string(ability) + ", current strength - " + to_string(org_->GetStrength());
	this->reportsList.push_back(report);
}

void Reports::cantUseAbility(int roundsToGo) {
	string report = "Human can't turn on his special ability for - " + to_string(roundsToGo) + "rounds";
	this->reportsList.push_back(report);
}

void Reports::fileSaved(string fileName) {
	string report = "File '"+fileName+"' - saved";
	this->reportsList.push_back(report);
}

void Reports::fileOpened(string fileName) {
	string report = "File '" + fileName + "' - opened";
	this->reportsList.push_back(report);
}

Reports::~Reports() {
}
