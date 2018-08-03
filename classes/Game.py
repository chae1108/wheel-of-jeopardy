from Wheel import Wheel
from Board import Board
from Player import Player

class Game:

    def __init__(self, categories):
        self.__turn = 0
        self.__round = 1
        self.__spins = 50
        self.__players = self.__createPlayers()
        self.__wheel = self.__createWheel(categories)
        self.__board = self.__createBoard(categories, self.__round)

    def __createPlayers(self):
        players = []
        playerCount = 3
        playerID = 0

        while playerCount > 0:
            player = Player(playerID)
            players.append(player)
            playerCount -= 1
            playerID += 1

        return players

    def __createWheel(self, categories):
        categoryNames = []
        for category in categories:
            name = category[0]
            categoryNames.append(name)

        wheel = Wheel(categoryNames)

        return wheel

    def __createBoard(self, categories, round):
        board = Board(categories, round)

        return board

    def getTurn(self):
        return self.__turn

    def getRound(self):
        return self.__round

    def getSpins(self):
        return self.__spins

    def getPlayer(self, id):
        return self.__players[id]

    def getPlayers(self):
        return self.__players

    def getWheel(self):
        return self.__wheel

    def getBoard(self):
        return self.__board

    def spinWheel(self):
        spin = self.__wheel.spin()
        return spin

    def playTurn(self, spin):
        player = self.__players[self.__turn]
        if spin == 1:
            self.__loseTurn(player)
        elif spin == 3:
            self.__freeTurn(player)
        elif spin == 5:
            self.__bankrupt(player)
        elif spin == 7 or spin == 9:
            spin = self.__categoryChoice(player)
            #spin *= 2
            #self.__playCategory(spin, player)
        elif spin == 11:
            self.__doubleScore(player)
        else:
            self.__playCategory(spin, player)

        self.useSpin()

    def __loseTurn(self, player):
        freeTurnsAvailable = player.freeTurnsAvailable()
        if freeTurnsAvailable:
            player.playFreeTurn()
            print("Free turns avaialable")
        else:
            self.nextTurn()
            print("Lose Turn")

    def __freeTurn(self, player):
        player.addFreeTurn()
        print("Gained free turn")

    def __bankrupt(self, player):
        player.bankrupt()
        self.nextTurn()
        print("Bankrupt")

    def __categoryChoice(self, player):
        print("Choice")
        ###################################### NEEDS TO GET CATEGORY ######################################

    def __doubleScore(self, player):
        player.doubleScore()
        print("Score doubled")

    def __playCategory(self, spin, player):
        boardID = int(spin / 2)
        categoryIsAvailable = self.__board.isCategoryAvailable(boardID)
        if categoryIsAvailable:
            square = self.__board.playCategory(boardID)
            question = square.getQuestion()
            print(question)
        else:
            print("Category is unavaible")

    def playerAnswersCorrect(self):
        return

    def playerAnswersIncorrect(self):
        return

    def useSpin(self):
        self.__spins -= 1

    def nextTurn(self):
        self.__turn = (self.__turn + 1) % 3

    def nextRound(self, categories):
        self._turn = self.__getLosingPlayer()
        self.__round += 1
        self.__spins = 50
        self.__wheel = self.__createWheel(categories)
        self.__board = self.__board(categories, self.__round)

    def __getLosingPlayer(self):
        lowestScore = self.__players[0].getTotalScore()
        losingPlayer = 0
        for player in self.__players:
            score = player.getTotalScore()

            if score < lowestScore:
                lowestScore = score
                losingPlayer = player.getID()

        return losingPlayer

    def printPlayers(self):
        for player in self.__players:
            player.printPlayer()