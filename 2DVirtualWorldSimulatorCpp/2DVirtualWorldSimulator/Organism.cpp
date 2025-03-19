#include <iostream>
#include "Organism.h"
#include "Defines.h"
#include "World.h"

Organism::Organism() {
	this->name = NULL;
	this->strength = NULL;
	this->initiative = NULL;
	this->position.x = NULL;
	this->position.y = NULL;
	this->wantedPos.x = NULL;
	this->wantedPos.y = NULL;
	this->isAlive = true;
	this->isAttacker = false;
	this->world = nullptr;
}


pos Organism::GetOrganismPosition() const{
	return this->position;
}

pos Organism::GetOrganismWantedPosition() const {
	return this->wantedPos;
}

bool Organism::GetOrganismLifespan() const {
	return this->isAlive;
}

bool Organism::GetOrganismIsAttacker() const {
	return this->isAttacker;
}

void Organism::SetOrganismStrength(int strength) {
	this->strength = strength;
}

void Organism::SetOrganismPosition(int x, int y) {
	this->position.x = x;
	this->position.y = y;
}

void Organism::SetOrganismWantedPosition(int x, int y) {
	this->wantedPos.x = x;
	this->wantedPos.y = y;
}

void Organism::SetOrganismLifespan(bool isAlive) {
	this->isAlive = isAlive;
}

void Organism::SetOrganismIsAttacker(bool isAttacker) {
	this->isAttacker = isAttacker;
}

char Organism::GetName() const {
	return this->name;
}

int Organism::GetStrength() const {
	return this->strength;
}

int Organism::GetInitiative() const {
	return this->initiative;
}

Organism::~Organism() {

}