#pragma once
#include "Animal.h"

class Turtle : public Animal{
public:
	Turtle();
	void action(World* world) override;
	bool collision(World* world,Organism* organismToFight) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Turtle();
};

