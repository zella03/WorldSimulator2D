#pragma once
#include "Organism.h"
#include <iostream>

class Animal : public Organism {
public:
	Animal();
	void action(World* world) override;
	bool collision(World* world,Organism* organismToFight) override;
	int GetFeatures()const override;
	void SetFeatures(int feature_, World* world) override;
	bool defaultAttack(World* world, Organism* organismToFight);
	~Animal();
};
