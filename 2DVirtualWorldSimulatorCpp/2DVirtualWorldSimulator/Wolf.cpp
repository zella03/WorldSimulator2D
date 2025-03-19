#include <iostream>
#include "Wolf.h"

Wolf::Wolf() {
	this->name = 'W';
	this->strength = 9;
	this->initiative = 5;
}

char Wolf::GetName() const{
	return 'W';
}

string Wolf::GetOrganismFullName() const {
	return "Wolf";
}

Wolf::~Wolf() {

}