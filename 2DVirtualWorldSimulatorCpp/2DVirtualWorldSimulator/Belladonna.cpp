#include <iostream>
#include "Belladonna.h"
#include "World.h"

Belladonna::Belladonna() {
	this->name = 'b';
	this->strength = 99;
}

bool Belladonna::collision(World* world,Organism* organismToFight) {
	//Kills any animal which eats it.
	pos animalPos;
	if (this->isAttacker == true) {
		return true;
	}
	else {
		if (organismToFight->GetName() > LETTER_RANGE_ANIMAL_A && organismToFight->GetName() < LETTER_RANGE_ANIMAL_Z) {
			organismToFight->SetOrganismLifespan(false);
			this->isAlive = false;
			animalPos = organismToFight->GetOrganismPosition();
			world->setOrganismVectorData(nullptr, animalPos.y, animalPos.x);
			world->setOrganismVectorData(nullptr, position.y, position.x);

			world->addCommentatorVector(CONSUMPTION, organismToFight, this, NULL);
			world->addCommentatorVector(KILL, this, organismToFight, NULL);
		}
	}
	return true;
}

char Belladonna::GetName() const {
	return 'b';
}

string Belladonna::GetOrganismFullName() const {
	return "Belladonna";
}

Belladonna::~Belladonna() {

}