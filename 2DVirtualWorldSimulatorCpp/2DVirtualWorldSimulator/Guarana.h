#pragma once
#include "Plant.h"
class Guarana : public Plant{
public:
	Guarana();
	bool collision(World* world,Organism* organismToFight) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Guarana();
};

