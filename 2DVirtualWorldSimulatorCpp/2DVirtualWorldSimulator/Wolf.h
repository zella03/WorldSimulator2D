#pragma once
#include "Animal.h"
#include <iostream>

class Wolf : public Animal {
public:
	Wolf();
	char GetName() const;
	string GetOrganismFullName() const;
	~Wolf();
};