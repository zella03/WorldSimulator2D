#include <iostream>
#include "Sheep.h"

Sheep::Sheep() {
	this->name = 'S';
	this->strength = 4;
	this->initiative = 4;
}
char Sheep::GetName() const {
	return 'S';
}

string Sheep::GetOrganismFullName() const {
	return "Sheep";
}

Sheep::~Sheep() {

}