#include <iostream>
#include "World.h"
#include "Fox.h"

Fox::Fox() {
	this->name = 'F';
	this->strength = 3;
	this->initiative = 7;
}

void Fox::action(World* world) {
	//wont go to stronger organizm
	int side_to_go = rand() % 4;

	switch (side_to_go) {
	case 0:
		if (position.x - 1 >= 0) {
			dueToStrength(world, position.x - 1, position.y);
		}
		else SetOrganismWantedPosition(position.x, position.y);
		break;
	case 1:
		if (position.x + 1 < world->GetHorizSize()) {
			dueToStrength(world, position.x + 1, position.y);
		}
		else SetOrganismWantedPosition(position.x, position.y);
		break;
	case 2:
		if (position.y - 1 >= 0) {
			dueToStrength(world, position.x, position.y - 1);
		}
		else SetOrganismWantedPosition(position.x, position.y);
		break;
	case 3:
		if (position.y + 1 < world->GetVerticSize()) {
			dueToStrength(world, position.x, position.y + 1);
		}
		else SetOrganismWantedPosition(position.x, position.y);
		break;
	default:
		break;
	}
}

void Fox::dueToStrength(World* world, int posX, int posY) {
	Organism* org = world->getOrganismVectorData(posY, posX);
	if ((org != nullptr && org->GetStrength() < this->GetStrength()) || org == nullptr) {
		SetOrganismWantedPosition(posX, posY);
	}
	else SetOrganismWantedPosition(position.x, position.y);
}

char Fox::GetName() const {
	return 'F';
}

string Fox::GetOrganismFullName() const {
	return "Fox";
}

Fox::~Fox() {

}
