#pragma once
#include "World.h"

class Game{
	bool beforeGame(World* world);
	void duringGame(World* world);
	void addToWorld(World* world, Organism* choiceOrganism);
	bool nameOfFile(char* txt);
	void intoFile(World* world, Organism* human);
	bool fromFile(World* world, Organism* human);
	void setFromFile(World* world, Organism* human);
	whoMoves who;
public:
	Game();
	World* world;
	Organism* human;
	void runGame();
	~Game();
};

