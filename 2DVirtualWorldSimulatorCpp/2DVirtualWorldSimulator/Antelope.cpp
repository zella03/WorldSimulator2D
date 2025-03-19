#include <iostream>
#include "Antelope.h"
#include "World.h"

Antelope::Antelope() {
	this->name = 'A';
	this->strength = 4;
	this->initiative = 4;
}

void Antelope::action(World* world) {
	//Has wider range of movement - 2 fields instead of 1.
	world->moveOrganism(this, TWO_STEPS);
}

bool Antelope::collision(World* world,Organism* organismToFight) {
	if (this->isAttacker == true) {
		this->defaultAttack(world, organismToFight);
		return true;
	}
	else {
		pos newPosition;
		int my_chances = rand() % 2;
		if (my_chances == 0) {
			newPosition = world->posFreeAround(this);
			if (newPosition.x != world->GetHorizSize() + 1) {
				world->setOrganismVectorData(nullptr, position.y, position.x);
				this->SetOrganismPosition(newPosition.x, newPosition.y);
				world->setOrganismVectorData(this, position.y, position.x);
				world->addCommentatorVector(MOVED, this, nullptr, NULL);
				return true;
			}
			else false;
		}
		else return false;
	}
}

char Antelope::GetName() const {
	return 'A';
}

string Antelope::GetOrganismFullName() const {
	return "Antelope";
}

Antelope::~Antelope() {
}