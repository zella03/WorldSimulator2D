#pragma once
#include "Animal.h"
#include "Defines.h"
#include <iostream>

class Human : public Animal {
	bool specialAbility;
	int abilityRounds;
	int abilityStrength;
	int basicStrength;

	bool abilityTurnOn();
public:
	Human();
	void action(World* world) override;
	bool collision(World* world,Organism* organismToFight) override;
	int GetFeatures()const override;
	void SetFeatures(int feature_, World* world) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Human();
};