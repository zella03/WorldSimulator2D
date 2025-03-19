#include <iostream>
#include "Sow_thistle.h"

Sow_thistle::Sow_thistle() {
	this->name = 's';
}

void Sow_thistle::action(World* world) {
	for (int i = 0; i < 3; i++) {
		this->defaultAction(world);
	}
}

char Sow_thistle::GetName() const {
	return 's';
}

string Sow_thistle::GetOrganismFullName() const {
	return "Sow_thistle";
}

Sow_thistle::~Sow_thistle() {

}