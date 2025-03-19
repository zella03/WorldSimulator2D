#include "Game.h"
#include "World.h"
#include "Human.h"
#include "Defines.h"
#include <stdlib.h>
#include <conio.h>
#include <fstream>
#include <string>

Game::Game() {
	this->world = new World;
	this->human = new Human();
	this->who = HUMAN_MOVE;
}

bool Game::beforeGame(World *world) {
	int start, horiz, vertic;
	system("cls");
	cout << "If you want to load world - press 2" << endl;
	cout << "If you want to choose size of the world - press 1"<<endl;
	cout << "If you want to choose default world size (which is 10x10) - press 0"<<endl;
	cin >> start;
	if (start == 0) {
		return false;
	}
	else if (start == 1) {
		system("cls");
		cout << "Enter Horizontal size of the world" << endl;
		cin >> horiz;
		world->SetHorizSize(horiz);

		system("cls");
		cout << "Enter Vertical size of the world" << endl;
		cin >> vertic;
		world->SetVerticSize(vertic);

		world->userWorld();
		return true;
	}
	else {
		if (fromFile(world, human)) {
			return false;
		}
		else beforeGame(world);
	}
	return false;
}

void Game::duringGame(World* world) {
	cout << "Monika Mazella nr.193334"<<endl;
	cout << "press arrows - to move human (one key at time)" << endl;
	cout << "press p - if you want to add special ability (only before moving)" << endl;
	cout << "press s - to save world (after human move)" << endl;
	cout << "press l - to load world (after human move)" << endl;
	cout << "press b - to skip human move" << endl;
	cout << "press n - to start next round" << endl;
	cout << "press q - to end symulation" << endl;
	if(who==HUMAN_MOVE) cout << endl << "HUMAN ROUND" << endl << endl;
	else if (who == WORLD_MOVE) cout << endl << "WORLD ROUND" << endl << endl;
	world->drawWorld();
}

void Game::addToWorld(World* world, Organism* choiceOrganism) {
	pos position = world->randPosition();
	world->addOrganism(position, choiceOrganism, FIGHT_LIST,false);
}

void Game::runGame() {
	
	static WorldState state = FIRST_SET;
	static MovementSide side = NONE;
	char sign = NULL;

	while (state != END) {
		if (state == FIRST_SET) {
			beforeGame(world);
			addToWorld(world, human);
			state = START;
		}
		else if (state == START) {
			system("cls");
			duringGame(world);

			if (human->GetOrganismLifespan() != false) {
				human->action(world);
				this->who = WORLD_MOVE;
				system("cls");
				duringGame(world);
			}
			else this->who = WORLD_MOVE;

			sign = _getch();
			if (sign == 'q') {
				state = END;
			}
			else if (sign == 's') {
				intoFile(world, human);
			}
			else if (sign == 'l') {
				fromFile(world, human);
			}
			else if (sign == 'n') {
				if (human->GetOrganismLifespan() != false) {
					side = NONE;
					world->setMovementHumanSide(side);
					pos stayPos = human->GetOrganismPosition();
					human->SetOrganismWantedPosition(stayPos.x, stayPos.y);
				}
				world->makeTurn();
			}
			if (human->GetOrganismLifespan() != false) this->who = HUMAN_MOVE;
		}
	}
}

bool Game::nameOfFile(char* txt) {
	int zn2 = NULL;
	int size = 0;

	cout << "Input File name: ";

	while (true) {
		zn2 = _getch();
		if (zn2 == KEY_ENTER)break;
		else if (((zn2 >= 'A') && (zn2 <= 'Z')) || ((zn2 >= 'a') && (zn2 <= 'z')) || ((zn2 >= '1') && (zn2 <= '9'))) {
			txt[size] = zn2;
			size++;
			_putch(zn2);
		}
	}
	txt[size] = '\0';

	if (size != 0) return true;
	else return false;
}



void Game::intoFile(World* world, Organism* human) {
	char txt[32];
	int temp;
	errno_t err;

	if (nameOfFile(txt) != false) {
		sprintf_s(txt, "%s.bin", txt);

		FILE* plik;
		err = fopen_s(&plik, txt, "ab");

		if (err==0) {
			temp = world->GetVerticSize();
			fwrite((void*)&temp, sizeof(int), 1, plik);
			temp = world->GetHorizSize();
			fwrite((void*)&temp, sizeof(int), 1, plik);
			temp = world->getFightVectorSize();
			fwrite((void*)&temp, sizeof(int), 1, plik);

			for (int i = 0; i < 10; i++) {
				temp = human->GetFeatures();
				fwrite((void*)&temp, sizeof(int), 1, plik);
			}
		
			for (int i = 0; i < world->getFightVectorSize(); i++)
			{
				for (int j = 0; j < 7; j++) {
					temp = world->getFightVectorData(i)->GetFeatures();
					fwrite((void*)&temp, sizeof(int), 1, plik);
				}
			}
			fclose(plik);
			world->CommentatorSaveOpen(FILE_SAVED, txt);
		}
	}
}


bool Game::fromFile(World* world, Organism* human) {
	char txt[32];
	system("cls");
	Organism* org_ = nullptr;
	int sizeFightList;
	int input;
	errno_t err;
	world->clearFightVect();
	world->clearNewOrgVect();

	if (nameOfFile(txt) == false) return false;
	sprintf_s(txt, "%s.bin", txt);

	FILE* plik;
	err = fopen_s(&plik, txt, "rb");

	if (err==0) {

		fread(&input, sizeof(int), 1, plik);
		world->SetVerticSize(input);
		fread(&input, sizeof(int), 1, plik);
		world->SetHorizSize(input);
		fread(&input, sizeof(int), 1, plik);
		sizeFightList = input;

		for (int i = 0; i < 10; i++) {
			fread(&input, sizeof(int), 1, plik);
			human->SetFeatures(input, world);
		}
		
		for (int i = 0; i < sizeFightList; i++) {
			fread(&input, sizeof(int), 1, plik);
			org_ = world->addByName(input);
			for (int j = 0; j < 6; j++) {
				fread(&input, sizeof(int), 1, plik);
				org_->SetFeatures(input, world);
			}
			world->addFightVectorData(org_);
		}
		setFromFile(world, human);
		fclose(plik);
		world->CommentatorSaveOpen(FILE_OPENED, txt);
	}
	else {
		int zn = NULL;
		zn = _getch();
		return false;
	}
	return true;
}

void Game::setFromFile(World* world, Organism* human) {
	pos positionOrg_;
	world->clearOrganismVect();
	world->organismsVectorResize();

	positionOrg_ = human->GetOrganismPosition();
	world->setOrganismVectorData(human, positionOrg_.y, positionOrg_.x);

	for (int i = 0; i < world->getFightVectorSize(); i++) {
		positionOrg_ = world->getFightVectorData(i)->GetOrganismPosition();

		world->setOrganismVectorData(world->getFightVectorData(i), positionOrg_.y, positionOrg_.x);
	}
}

Game::~Game() {
	
}