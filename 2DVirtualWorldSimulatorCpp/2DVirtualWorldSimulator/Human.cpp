#include <iostream>
#include "Human.h"
#include "World.h"
#include <conio.h>

Human::Human() {
	this->name = 'H';
	this->strength = 5;
	this->initiative = 4;
	this->specialAbility = false;
	this->abilityRounds = 0;
	this->abilityStrength = 10;
	this->basicStrength = 5;
}

void Human::action(World* world) {
	static MovementSide side = NONE;
	char sign;
	bool getMove = true;

	do {
		sign = _getch();
		if (sign == 'p' && this->abilityRounds == 0) {
			world->addCommentatorVector(HUMAN_GOT_AB, nullptr, nullptr, NULL);
			this->specialAbility = true;
			this->abilityRounds = 10;
			this->abilityStrength = 10;
		}
		else if (sign == 'b') break;
		else {
			sign = _getch();
			if (sign == KEY_UP) {
				side = UP;
			}
			else if (sign == KEY_RIGHT) {
				side = RIGHT;
			}
			else if (sign == KEY_DOWN) {
				side = DOWN;
			}
			else if (sign == KEY_LEFT) {
				side = LEFT;
			}
			else {
				side = NONE;
			}
		}

		if (sign != 'b' && sign != 'p') {
			world->setMovementHumanSide(side);

			if (world->getMovementHumanSide() == LEFT && this->position.x - 1 >= 0) {
				this->SetOrganismWantedPosition(position.x - 1, position.y);
			}
			else if (world->getMovementHumanSide() == RIGHT && this->position.x + 1 < world->GetHorizSize()) {
				this->SetOrganismWantedPosition(position.x + 1, position.y);
			}
			else if (world->getMovementHumanSide() == UP && this->position.y - 1 >= 0) {
				this->SetOrganismWantedPosition(position.x, position.y - 1);
			}
			else if (world->getMovementHumanSide() == DOWN && this->position.y + 1 < world->GetVerticSize()) {
				this->SetOrganismWantedPosition(position.x, position.y + 1);
			}
			else {
				this->SetOrganismWantedPosition(position.x, position.y);
			}

			if (side != NONE) {
				world->OrganismActionCollision(this);
			}
		}
		else {
			this->SetOrganismWantedPosition(position.x, position.y);
		}

	} while (sign == 'p' && sign != 'b');

	if(sign == 'b') {
		this->SetOrganismWantedPosition(position.x, position.y);
	}
}

bool Human::abilityTurnOn() {
	this->SetOrganismStrength(this->abilityStrength);
	if (this->abilityStrength != this->basicStrength) {
		this->abilityStrength--;
		return true;
	}
	else if (this->abilityRounds >=0) {
		return false;
	}
}

bool Human::collision(World* world,Organism* organismToFight) {
	
	if (this->specialAbility) {
		if (abilityTurnOn()) world->addCommentatorVector(ROUND_OG_AB, this, nullptr, NULL);
		else world->addCommentatorVector(CANT_USE_AB, nullptr, nullptr, abilityRounds);
		this->abilityRounds--;
		if (abilityRounds == 0) {
			this->specialAbility = false;
		}
	}

	if (organismToFight != nullptr) {
		if (this->isAttacker == true) {
			this->defaultAttack(world, organismToFight);
			return true;
		}
		else {
			return false;
		}
	}
}

char Human::GetName() const {
	return 'H';
}

string Human::GetOrganismFullName() const {
	return "Human";
}

int Human::GetFeatures()const {
	static int numFeature = 0;
	int out = NULL;
	if (numFeature == 0) out=this->name, numFeature++;
	else if(numFeature==1) out=this->strength, numFeature++;
	else if (numFeature == 2) out=this->position.x, numFeature++;
	else if (numFeature == 3) out=this->position.y, numFeature++;
	else if (numFeature == 4) out=this->wantedPos.x, numFeature++;
	else if (numFeature == 5) out=this->wantedPos.y, numFeature++;
	else if (numFeature == 6) {
		numFeature++;
		if (isAlive) out=1;
		else out=0;
	}
	else if (numFeature == 7) out=this->abilityRounds, numFeature++;
	else if (numFeature == 8) out=this->abilityStrength, numFeature++;
	else if (numFeature == 9) {
		numFeature = 0;
		if (specialAbility) out=1;
		else out=0;
	}
	return out;
}

void Human::SetFeatures(int feature_, World* world) {
	static int numFeature = 0;
	if (numFeature == 0) this->name = feature_, numFeature++;
	else if (numFeature == 1) this->strength = feature_, numFeature++;
	else if (numFeature == 2) this->position.x = feature_, numFeature++;
	else if (numFeature == 3) this->position.y = feature_, numFeature++;
	else if (numFeature == 4) this->wantedPos.x = feature_, numFeature++;
	else if (numFeature == 5) this->wantedPos.y = feature_, numFeature++;
	else if (numFeature == 6) {
		numFeature++;
		if (feature_ == 1) this->isAlive = true;
		else this->isAlive = false;
	}
	else if (numFeature == 7) this->abilityRounds = feature_, numFeature++;
	else if (numFeature == 8) this->abilityStrength = feature_, numFeature++;
	else if (numFeature == 9) {
		numFeature = 0;
		if (feature_ == 1) this->specialAbility = true;
		else this->specialAbility = false;
	}
}

Human::~Human() {

}