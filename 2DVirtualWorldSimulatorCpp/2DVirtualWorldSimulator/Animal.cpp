#include <iostream>
#include <cstdlib>
#include "Organism.h"
#include "Animal.h"
#include "World.h"
#include "Defines.h"

Animal::Animal() {
	this->name = NULL;
	this->strength = 0;
	this->initiative = 0;
	this->position.x = 0;
	this->position.y = 0;
	this->wantedPos.x = NULL;
	this->wantedPos.y = NULL;
	this->isAlive = true;
}

void Animal::action(World* world) {
	world->moveOrganism(this, ONE_STEP);
}

bool Animal::collision(World* world,Organism* organismToFight) {
	if (this->isAttacker == true) {
		defaultAttack(world, organismToFight);
		return true;
	}
	return false;
}

bool Animal::defaultAttack(World* world, Organism* organismToFight) {
	if (organismToFight->GetOrganismLifespan() == true) {
		
		if (this->name == organismToFight->GetName()) {
			if (world->addConcreteOrganism(this, organismToFight, NEW_ORGANISM)) {
				world->addCommentatorVector(SPAWN, this, nullptr, NULL);
			}
			this->SetOrganismWantedPosition(NULL, NULL);
		}
		else if (!organismToFight->collision(world, this)) {
			if ((this->strength == organismToFight->GetStrength()) || (this->strength > organismToFight->GetStrength())) {
				organismToFight->SetOrganismLifespan(false);

				world->setOrganismVectorData(nullptr, position.y, position.x);
				this->SetOrganismPosition(wantedPos.x, wantedPos.y);
				this->SetOrganismWantedPosition(NULL, NULL);

				world->setOrganismVectorData(this, position.y, position.x);
				world->addCommentatorVector(ANIMAL_OR_PLANT, this, organismToFight, NULL);
			}
			else {
				this->isAlive = false;
				this->SetOrganismWantedPosition(NULL, NULL);
				world->setOrganismVectorData(nullptr, position.y, position.x);
				world->addCommentatorVector(ANIMAL_OR_PLANT, organismToFight, this, NULL);
			}
		}
	}
	else {
		world->setOrganismVectorData(nullptr, position.y, position.x);
		this->SetOrganismPosition(wantedPos.x, wantedPos.y);
		this->SetOrganismWantedPosition(NULL, NULL);
		world->setOrganismVectorData(this, position.y, position.x);

		world->addCommentatorVector(MOVED, this, nullptr, NULL);
	}
	return true;
}

int Animal::GetFeatures()const {
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

void Animal::SetFeatures(int feature_, World* world) {
	static int numFeature = 0;
	static pos positionTemp;

	if (numFeature == 0) this->SetOrganismStrength(feature_) , numFeature++;
	else if(numFeature == 1) positionTemp.x = feature_, numFeature++;
	else if (numFeature == 2) positionTemp.y = feature_, numFeature++, this->SetOrganismPosition(positionTemp.x, positionTemp.y);
	else if (numFeature == 3) positionTemp.x = feature_, numFeature++;
	else if (numFeature == 4) positionTemp.y = feature_, numFeature++, this->SetOrganismWantedPosition(positionTemp.x, positionTemp.y);
	else if (numFeature == 5) {
		numFeature = 0;
		if (feature_ == 1) this->SetOrganismLifespan(true);
		else this->SetOrganismLifespan(false);
	}
}

Animal::~Animal() {

}