#pragma once
#include "Animal.h"

class Fox :public Animal{
	void dueToStrength(World* world, int posX, int posY);
public:
	Fox();
	void action(World* world) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Fox();
};

