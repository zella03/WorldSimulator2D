#include <iostream>
#include <stdlib.h>
#include <vector>
#include<algorithm>
#include "World.h"
#include "Defines.h"

#include "Antelope.h"
#include "Belladonna.h"
#include "Fox.h"
#include "Grass.h"
#include "Guarana.h"
#include "Human.h"
#include "Sheep.h"
#include "Sosnowsky_hogweed.h"
#include "Sow_thistle.h"
#include "Turtle.h"
#include "Wolf.h"
using namespace std;

World::World(): organisms(DEF_MATRIX_SIZE, vector<Organism*>(DEF_MATRIX_SIZE,nullptr)) {
	this->horizSize = DEF_MATRIX_SIZE;
	this->verticSize = DEF_MATRIX_SIZE;
	this->commentator = new Reports();

	int randO;
	for (int i = 0; i < 10; i++) {
		randO = (rand() % 2) + 1;
		for (int j = 0; j < randO; j++) {
			addRandomOrganism(i,FIGHT_LIST);
		}
	}
}

void World::userWorld() {
	organisms.clear();
	fightList.clear();
	this->organisms.resize(GetVerticSize(), vector <Organism*>(GetHorizSize(),nullptr));

	int randO;
	for (int i = 0; i < 10; i++) {
		randO = (rand() % 2) + 1;
		for (int j = 0; j < randO; j++) {
			addRandomOrganism(i,FIGHT_LIST);
		}
	}
}

void World::makeTurn() {
	sort(fightList.begin(), fightList.end(), more_initiative());

	for (int i = 0; i < fightList.size(); i++) {
		if (fightList[i]->GetOrganismLifespan() == true) {
			fightList[i]->action(this);
			OrganismActionCollision(fightList[i]);
		}
	}
	killOrg();

	for (int i = 0; i < newOrgList.size(); i++) {
		fightList.push_back(newOrgList[i]);
	}
	newOrgList.clear();
}

void World::OrganismActionCollision(Organism* org_) {

	pos posCheck = org_->GetOrganismWantedPosition();
	pos posNow = org_->GetOrganismPosition();

	if ((posCheck.x != posNow.x || posCheck.y != posNow.y) && (organisms[posCheck.y][posCheck.x] != nullptr)) {
		org_->SetOrganismIsAttacker(true);
		organisms[posCheck.y][posCheck.x]->SetOrganismIsAttacker(false);
		org_->collision(this, organisms[posCheck.y][posCheck.x]);
	}
	else {
		if (org_->GetName() == 'H') {
			org_->collision(this, nullptr);
		}
		org_->SetOrganismPosition(posCheck.x, posCheck.y);
		org_->SetOrganismWantedPosition(NULL, NULL);
		organisms[posCheck.y][posCheck.x] = org_;
		if (posCheck.x != posNow.x || posCheck.y != posNow.y) {
			organisms[posNow.y][posNow.x] = nullptr;
			commentator->reportMoved(org_);
		}
	}
}

void World::addOrganism(pos position, Organism* organism, int whichVect, bool addToList) {
	organism->SetOrganismPosition(position.x,position.y);
	organisms[position.y][position.x] = organism;
	if (addToList) {
		if (whichVect == FIGHT_LIST) fightList.push_back(organism);
		else if (whichVect == NEW_ORGANISM) newOrgList.push_back(organism);
	}
}

void World::addRandomOrganism(int numO, int whichVect) {
	Organism* organism;
	organism = nullptr;
	switch (numO){
	case 0:
		organism = new Wolf();
		break;
	case 1:
		organism = new Sheep();
		break;
	case 2:
		organism = new Fox();
		break;
	case 3:
		organism = new Turtle();
		break;
	case 4: 
		organism = new Antelope();
		break;
	case 5:
		organism = new Grass();
		break;
	case 6:
		organism = new Sow_thistle();
		break;
	case 7:
		organism = new Guarana();
		break;
	case 8:
		organism = new Belladonna();
		break;
	case 9:
		organism = new Sosnowsky_hogweed();
		break;
	}

	pos position = randPosition();
	addOrganism(position, organism, whichVect, true);
}


bool World::addConcreteOrganism(Organism* first, Organism* second, int whichVect) {
	char name = first->GetName();
	Organism* temp = addByName(name);

	pos position = posFreeAround(first);
	if (position.x == GetHorizSize() + 1) {
		position = posFreeAround(second);
	}
	if (position.x!= GetHorizSize() + 1) {
		addOrganism(position, temp, whichVect, true);
		return true;
	}
	return false; // nie by³o wolnego miejsca, nie dodano organizmu
}

Organism* World::addByName(char name) {
	Organism* temp = nullptr;
	if (name == 'W') {
		temp = new Wolf();
	}
	else if (name == 'S') {
		temp = new Sheep();
	}
	else if (name == 'F') {
		temp = new Fox();
	}
	else if (name == 'T') {
		temp = new Turtle();
	}
	else if (name == 'A') {
		temp = new Antelope();
	}
	else if (name == 'g') {
		temp = new Grass();
	}
	else if (name == 'u') {
		temp = new Guarana();
	}
	else if (name == 'b') {
		temp = new Belladonna();
	}
	else if (name == 's') {
		temp = new Sow_thistle();
	}
	else if (name == 'h') {
		temp = new Sosnowsky_hogweed();
	}
	return temp;
}

void World::killOrg() {
	for (int i = 0; i < fightList.size(); i++) {
		if (fightList[i]->GetOrganismLifespan() == false) {
			delete[] fightList[i];
			fightList.erase(fightList.begin() + i);
		}
	}
}

pos World::randPosition() {
	int y, x;
	pos tempPoint;
	do {
		y = rand() % GetVerticSize();
		x = rand() % GetHorizSize();
	} while (organisms[y][x] != nullptr);
	tempPoint.x = x;
	tempPoint.y = y;
	return tempPoint;
}

pos World::posFreeAround(Organism* org) {
	pos position = org->GetOrganismPosition();
	pos tempPoint;
	if (position.x - 1 >= 0 && organisms[position.y][position.x - 1] == nullptr) {
		tempPoint.x = position.x - 1;
		tempPoint.y = position.y;
	}
	else if (position.x + 1 < GetHorizSize() && organisms[position.y][position.x + 1] == nullptr) {
		tempPoint.x = position.x + 1;
		tempPoint.y = position.y;
	}
	else if (position.y - 1 >= 0 && organisms[position.y - 1][position.x] == nullptr) {
		tempPoint.x = position.x;
		tempPoint.y = position.y - 1;
	}
	else if (position.y + 1 < GetVerticSize() && organisms[position.y + 1][position.x] == nullptr) {
		tempPoint.x = position.x;
		tempPoint.y = position.y + 1;
	}
	else {
		tempPoint.x = GetHorizSize() + 1;
		tempPoint.y = GetVerticSize() + 1;
	}
	return tempPoint;
}

void World::moveOrganism(Organism* organism, int numFields) {
	int side_to_go = rand() % 4;
	pos position = organism->GetOrganismPosition();

	switch (side_to_go) {
	case 0:
		if (position.x - numFields >= 0) {
			organism->SetOrganismWantedPosition(position.x - numFields, position.y);
		}
		else organism->SetOrganismWantedPosition(position.x, position.y);
		break;
	case 1:
		if (position.x + numFields < GetHorizSize()) {
			organism->SetOrganismWantedPosition(position.x + numFields, position.y);
		}
		else organism->SetOrganismWantedPosition(position.x, position.y);
		break;
	case 2:
		if (position.y - numFields >= 0) {
			organism->SetOrganismWantedPosition(position.x, position.y - numFields);
		}
		else organism->SetOrganismWantedPosition(position.x, position.y);
		break;
	case 3:
		if (position.y + numFields < GetVerticSize()) {
			organism->SetOrganismWantedPosition(position.x, position.y + numFields);
		}
		else organism->SetOrganismWantedPosition(position.x, position.y);
		break;
	}
}


void World::drawWorld() {
	for (int i = 0; i < GetVerticSize(); i++) {
		for (int j = 0; j < GetHorizSize(); j++) {
			if (organisms[i][j] == nullptr) {
				cout << DOT;
			}
			else cout << organisms[i][j]->GetName();
		}
		cout << endl;
	}
	cout << endl;
	commentator->printReports();
	commentator->clearReports();
}

void World::SetHorizSize(int horizSize) {
	this->horizSize = horizSize;
}

void World::SetVerticSize(int verticSize) {
	this->verticSize = verticSize;
}

int World::GetHorizSize() const{
	return this->horizSize;
}

int World::GetVerticSize() const {
	return this->verticSize;
}

void World::setOrganismVectorData(Organism* org_, int i, int j) {
	this->organisms[i][j] = org_;
}

Organism* World::getOrganismVectorData(int i, int j) {
	return this->organisms[i][j];
}

void World::addFightVectorData(Organism* org_) {
	this->fightList.push_back(org_);
}

Organism* World::getFightVectorData(int i) {
	return this->fightList[i];
}

int World::getFightVectorSize() {
	return this->fightList.size();
}

void World::addNewOrgVectorData(Organism* org_) {
	this->newOrgList.push_back(org_);
}
Organism* World::getNewOrgVectorData(int i) {
	return this->newOrgList[i];
}

void World::setMovementHumanSide(MovementSide side) {
	this->movementHuman = side;
}

MovementSide World::getMovementHumanSide() {
	return this->movementHuman;
}

void World::addCommentatorVector(int whichComment, Organism* killing, Organism* dying, int roundsAd) {
	if (whichComment == KILL) this->commentator->reportKill(killing, dying);
	else if (whichComment == CONSUMPTION) this->commentator->reportConsumption(killing, dying);
	else if (whichComment == SPAWN) this->commentator->reportSpawn(killing);
	else if (whichComment == MOVED) this->commentator->reportMoved(killing);
	else if (whichComment == STRENGTH_INC) this->commentator->strengthIncrease(killing);
	else if (whichComment == ATTACK_REFLECTED) this->commentator->attackReflected(killing);
	else if (whichComment == HUMAN_GOT_AB) this->commentator->humanGotAbility();
	else if (whichComment == ROUND_OG_AB) this->commentator->roundOfAbility(killing);
	else if (whichComment == CANT_USE_AB) this->commentator->cantUseAbility(roundsAd);
	else if (whichComment == ANIMAL_OR_PLANT) this->commentator->AnimalOrPlant(killing, dying);
}

void World::CommentatorSaveOpen(int whichComment,string fileName) {
	if (whichComment == FILE_SAVED) this->commentator->fileSaved(fileName);
	else if (whichComment == FILE_OPENED) this->commentator->fileOpened(fileName);
}

void World::CommentatorPrintOrClear(int whichAct) {
	if (whichAct == PRINT) this->commentator->printReports();
	else if (whichAct == CLEAR) this->commentator->clearReports();
}

void World::clearFightVect() {
	this->fightList.clear();
}

void World::clearNewOrgVect() {
	this->newOrgList.clear();
}

void World::clearOrganismVect() {
	this->organisms.clear();
}

void World::organismsVectorResize() {
	this->organisms.resize(this->GetVerticSize(), vector <Organism*>(this->GetHorizSize(), nullptr));
}

World::~World() {
	organisms.clear();
	fightList.clear();
}