#pragma once
#include "Plant.h"
class Belladonna : public Plant{
public:
	Belladonna();
	bool collision(World* world,Organism* organismToFight) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Belladonna();
};

