from Square import Square

class Category:

    def __init__(self, id, category, round):
        self.__id = id
        self.__name = category.pop(0)
        self.__available = True
        self.__squares = self.__createSquares(category, round)

    # Returns a list of squares created from the category provided by the board
    def __createSquares(self, category, round):
            squares = []

            # Removes the first entry in the category and alternates between the question and answer
            id = 0
            value = 200;
            while len(category) > 0:
                question = category.pop(0)
                answer = category.pop(0)
                square = Square(id, value, round, question, answer)
                squares.append(square)
                id += 1
                value += 200

            return squares

    # Returns the category ID
    def getID(self):
        return self.__id

    # Returns the category name
    def getName(self):
        return self.__name

    # Returns the next available square in the category.  If the square is the final entry, it sets the category as unavailable.
    def getAvailableSquare(self):
        for square in self.__squares:
            if square.isAnswered() == False:
                if square.getID() == (len(self.__squares) - 1):
                    self.__setUnavailable()
                return square

    # Returns a square with the specific ID
    def getSquare(self, id):
        return self.__squares[id]

    # Sets the category as unavailable
    def __setUnavailable(self):
        self.__available = False

    # Returns if the category is available
    def isAvailable(self):
        return self.__available

    # Prints the category
    def printCategory(self):
        print(str(self.__id) + ": " + self.__name + " (" + str(self.__available) + ")")
        for square in self.__squares:
            square.printSquare()