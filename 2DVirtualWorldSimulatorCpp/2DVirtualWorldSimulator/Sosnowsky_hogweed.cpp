#include <iostream>
#include "Sosnowsky_hogweed.h"
#include "World.h" 

Sosnowsky_hogweed::Sosnowsky_hogweed() {
	this->name = 'h';
	this->strength = 10;
}

void Sosnowsky_hogweed::action(World* world) {
	//Kills every animal in its immediate neighborhood except cyber - sheep.
	if (position.x - 1 >= 0 ) {
		killAnimalAround(world, position.x - 1, position.y);
	}
	if (position.x + 1 < world->GetHorizSize()) {
		killAnimalAround(world, position.x + 1, position.y);
	}
	if (position.y - 1 >= 0) {
		killAnimalAround(world, position.x, position.y - 1);
	}
	if (position.y + 1 < world->GetVerticSize()) {
		killAnimalAround(world, position.x, position.y + 1);
	}
	this->SetOrganismWantedPosition(position.x, position.y);
}

void Sosnowsky_hogweed::killAnimalAround(World* world, int posX, int posY) {
	if (world->getOrganismVectorData(posY, posX) != nullptr && (world->getOrganismVectorData(posY, posX)->GetName() > LETTER_RANGE_ANIMAL_A
		&& world->getOrganismVectorData(posY, posX)->GetName() < LETTER_RANGE_ANIMAL_Z)) {
		world->getOrganismVectorData(posY, posX)->SetOrganismLifespan(false);

		world->addCommentatorVector(KILL, this, world->getOrganismVectorData(posY, posX), NULL);
		world->setOrganismVectorData(nullptr, posY, posX);
	}
}

bool Sosnowsky_hogweed::collision(World* world,Organism* organismToFight) {
	//Kills any animal which eats it, apart from cyber - sheep.
	pos animalPos;
	if (this->isAttacker == true) {
		return true;
	}
	else {
		world->addCommentatorVector(CONSUMPTION, organismToFight, this, NULL);
		world->addCommentatorVector(KILL, this, organismToFight, NULL);
		organismToFight->SetOrganismLifespan(false);
		this->isAlive = false;
		animalPos = organismToFight->GetOrganismPosition();
		world->setOrganismVectorData(nullptr, animalPos.y, animalPos.x);
		world->setOrganismVectorData(nullptr, position.y, position.x);
	}
	return true;
}

char Sosnowsky_hogweed::GetName() const {
	return 'h';
}

string Sosnowsky_hogweed::GetOrganismFullName() const {
	return "Sosnowsky_hogweed";
}

Sosnowsky_hogweed::~Sosnowsky_hogweed() {

}