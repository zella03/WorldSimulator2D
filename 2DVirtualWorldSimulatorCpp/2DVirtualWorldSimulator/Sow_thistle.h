#pragma once
#include "Plant.h"
class Sow_thistle : public Plant{
public:
	Sow_thistle();
	void action(World* world) override;
	char GetName() const;
	string GetOrganismFullName() const;
	~Sow_thistle();
};

