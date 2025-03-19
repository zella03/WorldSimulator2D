#pragma once
#include "Animal.h"
#include <iostream>

class Sheep : public Animal {
public:
	Sheep();
	char GetName() const;
	string GetOrganismFullName() const;
	~Sheep();
};