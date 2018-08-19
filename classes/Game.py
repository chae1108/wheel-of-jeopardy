from classes.Wheel import Wheel
from classes.Board import Board
from classes.Player import Player

class Game:

    # Added game over
    def __init__(self, categories):
        self.__turn = 0
        self.__round = 1
        self.__spins = 50
        self.__gameOver = False
        self.__players = self.__createPlayers()
        self.__round1Categories = categories[0:6]
        self.__round2Categories = categories[6:12]
        self.__wheel = self.__createWheel(self.__round1Categories)
        self.__board = self.__createBoard(self.__round)

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

    def __createBoard(self, round):
        if round == 1:
            board = Board(self.__round1Categories, round)
        else:
            board = Board(self.__round2Categories, round)

        return board

    def getTurn(self):
        return self.__turn

    def getRound(self):
        return self.__round

    def getSpins(self):
        return self.__spins

    def isGameOver(self):
        return self.__gameOver

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
        elif spin == 11:
            self.__doubleScore(player)

        self.useSpin()

    def __loseTurn(self, player):
        freeTurnsAvailable = player.freeTurnsAvailable()
        if freeTurnsAvailable:
            player.playFreeTurn()
        else:
            self.nextTurn()

    def __freeTurn(self, player):
        player.addFreeTurn()

    def __bankrupt(self, player):
        player.bankrupt()
        self.nextTurn()

    def __doubleScore(self, player):
        player.doubleScore()

    def playCategory(self, spin):
        boardID = int(spin / 2)
        categoryIsAvailable = self.__board.isCategoryAvailable(boardID)
        if categoryIsAvailable:
            catName = self.getBoard().getCategory(boardID).getName()
            square = self.__board.playCategory(boardID)
            question = square.getQuestion()
            answer = square.getAnswer()
            value = square.getValue()
            data = [catName, value, question, answer]
            return data
        else:
            data = ["", 0, "", ""]
            return data

    def playerAnswersCorrect(self, questionValue):
        self.__players[self.__turn].updateRoundScore(questionValue)
        self.useSpin()

    def playerAnswersIncorrect(self, questionValue):
        questionValue *= -1
        player = self.__players[self.__turn]
        player.updateRoundScore(questionValue)
        freeTurnsAvailable = player.freeTurnsAvailable()

        if freeTurnsAvailable:
            player.playFreeTurn()
        else:
            self.nextTurn()

        self.useSpin()

    def useSpin(self):
        self.__spins -= 1

    def nextTurn(self):
        self.__turn = (self.__turn + 1) % 3

    def nextRound(self):
        self._turn = self.__getLastPlacePlayer()
        self.__round += 1
        self.__spins = 50

        for player in self.__players:
            player.addRoundScoreToTotal()
            player.resetRoundScore()

        self.__wheel = self.__createWheel(self.__round2Categories)
        self.__board = self.__createBoard(self.__round)

    def __getLastPlacePlayer(self):
        lowestScore = self.__players[0].getTotalScore()
        lastPlace = 0
        for player in self.__players:
            score = player.getTotalScore()

            if score < lowestScore:
                lowestScore = score
                lastPlace = player.getID()

        return lastPlace

    def getWinner(self):
        highestScore = self.__players[0].getTotalScore()
        winner = 0
        for player in self.__players:
            score = player.getTotalScore()

            if score > highestScore:
                highestScore = score
                winner = player.getID()

        return winner

    def isGameOver(self):
        catAvail = 0

        for category in self.getBoard().getCategories():
            catAvail += 1

        if self.__round == 1:
            if self.__spins > 0 and catAvail > 0:
                self.__gameOver = False
            else:
                self.__gameOver = False
                self.nextRound()
        else:
            if self.__spins > 0 and catAvail > 0:
                self.__gameOver = False
            else:
                for player in self.__players:
                    player.addRoundScoreToTotal()
                    player.resetRoundScore()
                self.__gameOver = True

        return self.__gameOver

    def getAvailableSquares(self):
        available = []

        categories = self.__board.getCategories()
        for category in categories:
            squares = category.getSquares()

            for square in squares:
                if square.isAnswered():
                    available.append(False)
                else:
                    available.append(True)

        return available

    def printPlayers(self):
        for player in self.__players:
            player.printPlayer()
