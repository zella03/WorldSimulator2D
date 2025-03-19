#pragma once
#include "Animal.h"

class Antelope : public Animal{
public:
	Antelope();
	void action(World* world) override;
	bool collision(World* world,Organism* organismToFight) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Antelope();
};

