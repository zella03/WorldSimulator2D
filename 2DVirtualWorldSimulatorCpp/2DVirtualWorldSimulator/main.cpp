#include <iostream>
#include "Defines.h"
#include "Game.h"
using namespace std;

int main() {
	srand((unsigned)time(NULL));
	Game game;
	game.runGame();

	return 0;
}