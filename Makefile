SRC = lancement.py\

EXE3 = python3

EXE2 = python2

EXE = python

exe3:
	@($(EXE3) $(SRC))

exe2:
	@($(EXE2) $(SRC))

exe:
	@($(EXE) $(SRC))