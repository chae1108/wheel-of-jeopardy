class Player:

    def __init__(self, id):
        self.__id = id
        self.__totalScore = 0
        self.__roundScore = 0
        self.__freeTurns = 0

    # Returns the player ID
    def getID(self):
        return self.__id

    # Returns the player's round score
    def getRoundScore(self):
        return self.__roundScore

    # Returns the player's total score
    def getTotalScore(self):
        return self.__totalScore

    # Updates the player's round score
    def updateRoundScore(self, update):
        self.__roundScore += update

    # Resets the player's round score
    def resetRoundScore(self):
        self.__roundScore = 0

    # Doubles the player's round score
    def doubleScore(self):
        self.__roundScore *= 2

    # Bankrupts the player
    def bankrupt(self):
        self.__roundScore = 0

    # Adds the round score to the total score
    def addRoundScoreToTotal(self):
        self.__totalScore += self.__roundScore

    # Returns the player free turns
    def getFreeTurns(self):
        return self.__freeTurns

    # Adds a free turn
    def addFreeTurn(self):
        self.__freeTurns += 1

    # Removes a free turn
    def playFreeTurn(self):
        self.__freeTurns -= 1

    # Returns if a player has any free turns available to play
    def freeTurnsAvailable(self):
        if(self.__freeTurns > 0):
            return True
        else:
            return False

    # Prints the player
    def printPlayer(self):
        print("Player" + str(self.__id) + ": " + str(self.__roundScore) + "/" + str(self.__totalScore) + " (" + str(self.__freeTurns) + ")")
