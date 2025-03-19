#pragma once
#include <iostream>
#include <vector>
#include <string>
#include "Organism.h"
#include "Reports.h"
#include "Defines.h"
using namespace std;

struct more_initiative
{
	inline bool operator() (const Organism* struct1, const Organism* struct2) {
		return ((*struct1).GetInitiative() > (*struct2).GetInitiative());
	}
};

class World {
	int horizSize;
	int verticSize;

	vector<vector<Organism*>> organisms;
	vector<Organism*> fightList;
	vector<Organism*>newOrgList;
	Reports* commentator;

	MovementSide movementHuman;

	void addRandomOrganism(int numO, int whichVect);
	void killOrg();
public:
	World();
	pos posFreeAround(Organism* org);
	void moveOrganism(Organism* organism, int numFields);
	void userWorld();
	void makeTurn();
	void drawWorld();
	pos randPosition();
	void addOrganism(pos position, Organism* organism, int whichVect, bool addToList);
	bool addConcreteOrganism(Organism* first, Organism* second, int whichVect);
	void OrganismActionCollision(Organism* org_);
	Organism* addByName(char name);

	void SetHorizSize(int horizSize);
	void SetVerticSize(int verticSize);
	int GetHorizSize() const;
	int GetVerticSize() const;

	void setMovementHumanSide(MovementSide side);
	MovementSide getMovementHumanSide();

	void addCommentatorVector(int whichComment, Organism* killing, Organism* dying,int roundsAd);
	void CommentatorSaveOpen(int whichComment,string fileName);
	void CommentatorPrintOrClear(int whichAct);

	void setOrganismVectorData(Organism* org_, int i, int j);
	Organism* getOrganismVectorData(int i, int j);
	void addFightVectorData(Organism* org_);
	Organism* getFightVectorData(int i);
	int getFightVectorSize();
	void addNewOrgVectorData(Organism* org_);
	Organism* getNewOrgVectorData(int i);

	void clearFightVect();
	void clearNewOrgVect();
	void clearOrganismVect();
	void organismsVectorResize();

	~World();
};