#include <iostream>
#include "Grass.h"

Grass::Grass() {
	this->name = 'g';
}

char Grass::GetName() const {
	return 'g';
}

string Grass::GetOrganismFullName() const {
	return "Grass";
}

Grass::~Grass() {

}