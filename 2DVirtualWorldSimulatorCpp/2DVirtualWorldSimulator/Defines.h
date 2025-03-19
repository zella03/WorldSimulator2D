#pragma once

enum WorldState {
	FIRST_SET,
	START,
	END
};

enum MovementSide {
	NONE,
	LEFT,
	RIGHT,
	UP,
	DOWN
};

enum whoMoves {
	HUMAN_MOVE,
	WORLD_MOVE
};

enum reportType {
	KILL,
	CONSUMPTION,
	SPAWN,
	MOVED,
	STRENGTH_INC,
	ATTACK_REFLECTED,
	HUMAN_GOT_AB,
	ROUND_OG_AB,
	CANT_USE_AB,
	FILE_SAVED,
	FILE_OPENED,
	ANIMAL_OR_PLANT,
	PRINT,
	CLEAR
};

#define DEF_MATRIX_SIZE 10
#define ESCAPE 27
#define DOT '.'
#define KEY_ENTER 0x0d
#define ONE_STEP 1
#define TWO_STEPS 2
#define LETTER_RANGE_ANIMAL_A 64
#define LETTER_RANGE_ANIMAL_Z 91
#define KEY_UP 0x48
#define KEY_RIGHT 0x4d
#define KEY_DOWN 0x50
#define KEY_LEFT 0x4b

#define FIGHT_LIST 0
#define NEW_ORGANISM 1