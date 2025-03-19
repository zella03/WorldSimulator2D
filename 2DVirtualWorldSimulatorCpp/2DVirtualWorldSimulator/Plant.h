#pragma once
#include "Organism.h"

class Plant : public Organism{
public:
	Plant();
	void action(World* world) override;
	void defaultAction(World* world);
	bool collision(World* world,Organism* organismToFight) override;
	int GetFeatures()const override;
	void SetFeatures(int feature_, World* world) override;
	bool defaultAttack(World* world, Organism* organismToFight);
	~Plant();
};

