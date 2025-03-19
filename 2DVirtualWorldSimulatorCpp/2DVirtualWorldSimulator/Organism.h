#pragma once
#include "Defines.h"
#include <iostream>
#include <string>
using namespace std;

class World;

struct pos {
	int x;
	int y;
};

class Organism {
protected:
	int initiative;
	int strength;
	pos position;
	pos wantedPos;
	char name;
	World* world;
	bool isAlive;
	bool isAttacker;
protected:
	virtual bool defaultAttack(World* world, Organism* organismToFight) = 0;
public:
	Organism();
	virtual void action(World* world) = 0;
	virtual bool collision(World* world,Organism* organismToFight) = 0;
	virtual string GetOrganismFullName() const = 0;
	virtual int GetFeatures()const = 0;
	virtual void SetFeatures(int feature_, World* world) = 0;

	virtual char GetName() const;
	virtual int GetStrength() const;
	virtual int GetInitiative() const;
	
	virtual void SetOrganismStrength(int strength);
	virtual void SetOrganismPosition(int x, int y);
	virtual void SetOrganismLifespan(bool isAlive);
	virtual void SetOrganismWantedPosition(int x, int y);
	virtual void SetOrganismIsAttacker(bool isAttacker);

	virtual pos GetOrganismPosition() const;
	virtual pos GetOrganismWantedPosition() const;
	virtual bool GetOrganismLifespan() const;
	virtual bool GetOrganismIsAttacker() const;
	
	virtual ~Organism();
};