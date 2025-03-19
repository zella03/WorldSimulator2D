#include <iostream>
#include "Guarana.h"
#include "World.h"

Guarana::Guarana() {
	this->name = 'u';
}

bool Guarana::collision(World* world,Organism* organismToFight) {
	int tempStrength;
	if (this->isAttacker == true) {
		return true;
	}
	else {
		//Strength of the animal which ate guarana is permanently increased by 3.
		if (organismToFight->GetName() > LETTER_RANGE_ANIMAL_A && organismToFight->GetName() < LETTER_RANGE_ANIMAL_Z) {
			tempStrength = (organismToFight->GetStrength()) * 3;
			organismToFight->SetOrganismStrength(tempStrength);
			world->addCommentatorVector(STRENGTH_INC, organismToFight, nullptr, NULL);
		}
	}
	return false;
}

char Guarana::GetName() const {
	return 'u';
}

string Guarana::GetOrganismFullName() const {
	return "Guarana";
}

Guarana::~Guarana() {

}