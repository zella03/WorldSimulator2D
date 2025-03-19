#include <iostream>
#include <cstdlib>
#include "Turtle.h"
#include "World.h"

Turtle::Turtle() {
	this->name = 'T';
	this->strength = 2;
	this->initiative = 1;
}

void Turtle::action(World* world) {
	//75% chance to stay in the same place.
	int side_to_go = rand() % 4;
	if (side_to_go == 0) {
		world->moveOrganism(this, 1);
	}
	else this->SetOrganismWantedPosition(this->position.x, this->position.y);
}

bool Turtle::collision(World* world,Organism* organismToFight) {
	//Reflects attacks of animal with strength less than 5. Attacker will return to the previous cell.
	
	if (this->isAttacker == true) {
		this->defaultAttack(world, organismToFight);
		return true;
	}
	else {
		if (organismToFight->GetStrength() < 5) {
			world->addCommentatorVector(ATTACK_REFLECTED, organismToFight, nullptr, NULL);
			return true;
		}
		else return false;
	}
}

char Turtle::GetName() const {
	return 'T';
}

string Turtle::GetOrganismFullName() const {
	return "Turtle";
}

Turtle::~Turtle() {

}