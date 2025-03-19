#include "Plant.h"
#include "World.h"
#include <iostream>
#include <stdlib.h>
#include "Organism.h"

Plant::Plant() {
	this->name = NULL;
	this->position.x = 0;
	this->position.y = 0;
	this->wantedPos.x = NULL;
	this->wantedPos.y = NULL;
	this->strength = 0;
	this->initiative = 0;
	this->isAlive = true;
}

void Plant::action(World* world) {
	defaultAction(world);
}

void Plant::defaultAction(World* world) {
	int my_chances;
	my_chances = rand() % 50;

	if (my_chances == 19) {
		if (world->addConcreteOrganism(this, this, NEW_ORGANISM)) {
			world->addCommentatorVector(SPAWN, this, nullptr, NULL);
		}
	}
	this->SetOrganismWantedPosition(position.x, position.y);
}

bool Plant::collision(World* world,Organism* organismToFight) {
	return false;
}

bool Plant::defaultAttack(World* world, Organism* organismToFight) {
	return false;
}

int Plant::GetFeatures()const {
	static int numFeature = 0;
	int out = NULL;
	if (numFeature == 0) out = this->name, numFeature++;
	else if (numFeature == 1) out = this->strength, numFeature++;
	else if (numFeature == 2) out = this->position.x, numFeature++;
	else if (numFeature == 3) out = this->position.y, numFeature++;
	else if (numFeature == 4) out = this->wantedPos.x, numFeature++;
	else if (numFeature == 5) out = this->wantedPos.y, numFeature++;
	else if (numFeature == 6) {
		numFeature = 0;
		if (this->isAlive) out = 1;
		else out = 0;
	}
	return out;
}

void Plant::SetFeatures(int feature_, World* world) {
	static int numFeature = 0;
	static pos positionTemp;

	if (numFeature == 0) this->SetOrganismStrength(feature_), numFeature++;
	else if (numFeature == 1) positionTemp.x = feature_, numFeature++;
	else if (numFeature == 2) positionTemp.y = feature_, numFeature++, this->SetOrganismPosition(positionTemp.x, positionTemp.y);
	else if (numFeature == 3) positionTemp.x = feature_, numFeature++;
	else if (numFeature == 4) positionTemp.y = feature_, numFeature++, this->SetOrganismWantedPosition(positionTemp.x, positionTemp.y);
	else if (numFeature == 5) {
		numFeature = 0;
		if (feature_ == 1) this->SetOrganismLifespan(true);
		else this->SetOrganismLifespan(false);
	}
}

Plant::~Plant() {

}