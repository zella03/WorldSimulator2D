#pragma once
#include "Plant.h"
class Grass : public Plant{
public:
	Grass();
	char GetName() const;
	string GetOrganismFullName() const;
	~Grass();
};

