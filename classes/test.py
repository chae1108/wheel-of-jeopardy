from Game import Game

if __name__ == "__main__":
    cat0 = ["cat0", "c0q0", "c0a0", "c0q1", "c0a1", "c0q2", "c0a2", "c0q3", "c0a3", "c0q4", "c0a5"]
    cat1 = ["cat1", "c1q0", "c1a0", "c1q1", "c1a1", "c1q2", "c1a2", "c1q3", "c1a3", "c1q4", "c1a4"]
    cat2 = ["cat2", "c2q0", "c2a0", "c2q1", "c2a1", "c2q2", "c2a2", "c2q3", "c2a3", "c2q4", "c2a4"]
    cat3 = ["cat3", "c3q0", "c3a0", "c3q1", "c3a1", "c3q2", "c3a2", "c3q3", "c3a3", "c3q4", "c3a4"]
    cat4 = ["cat4", "c4q0", "c4a0", "c4q1", "c4a1", "c4q2", "c4a2", "c4q3", "c4a3", "c4q4", "c4a4"]
    cat5 = ["cat5", "c5q0", "c5a0", "c5q1", "c5a1", "c5q2", "c5a2", "c5q3", "c5a3", "c5q4", "c5a4"]
    cat6 = ["cat6", "c6q0", "c6a0", "c6q1", "c6a1", "c6q2", "c6a2", "c6q3", "c6a3", "c6q4", "c6a4"]
    cat7 = ["cat7", "c7q0", "c7a0", "c7q1", "c7a1", "c7q2", "c7a2", "c7q3", "c7a3", "c7q4", "c7a4"]
    cat8 = ["cat8", "c8q0", "c8a0", "c8q1", "c8a1", "c8q2", "c8a2", "c8q3", "c8a3", "c8q4", "c8a4"]
    cat9 = ["cat9", "c9q0", "c9a0", "c9q1", "c9a1", "c9q2", "c9a2", "c9q3", "c9a3", "c9q4", "c9a4"]
    cat10 = ["cat10", "c10q0", "c10a0", "c10q1", "c10a1", "c10q2", "c10a2", "c10q3", "c10a3", "c10q4", "c10a4"]
    cat11 = ["cat11", "c11q0", "c11a0", "c11q1", "c11a1", "c11q2", "c11a2", "c11q3", "c11a3", "c11q4", "c11a4"]
    categories1 = [cat0, cat1, cat2, cat3, cat4, cat5]
    categories2 = [cat6, cat7, cat8, cat9, cat10, cat11]

    r1 = 1;
    r2 = 2;

    game = Game(categories1)
    #game.printPlayers()
    #game.getWheel().printWheel()
    #game.getBoard().printBoard()
    spin = game.spinWheel()
    game.playTurn(spin)