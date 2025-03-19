#pragma once
#include "Plant.h"
class Sosnowsky_hogweed : public Plant{
	void killAnimalAround(World* world, int posX, int posY);
public:
	Sosnowsky_hogweed();
	void action(World* world) override;
	bool collision(World* world,Organism* organismToFight) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Sosnowsky_hogweed();
};

