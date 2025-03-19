#pragma once
#include <vector>
#include <string>
#include "Organism.h"

class Reports{
public:
	vector<string> reportsList;
	
	Reports();
	void printReports();

	void reportKill(Organism*killing, Organism* dying);
	void reportConsumption(Organism* killing, Organism* dying);
	void reportSpawn(Organism* org_);
	void reportMoved(Organism* org_);
	void AnimalOrPlant(Organism* killing, Organism* dying);
	void strengthIncrease(Organism* org_);
	void attackReflected(Organism* org_);
	void humanGotAbility();
	void roundOfAbility(Organism* org_);
	void cantUseAbility(int roundsToGo);
	void fileSaved(string fileName);
	void fileOpened(string fileName);

	void clearReports();

	~Reports();
};

