class Square:

    def __init__(self, id, value, round, question, answer):
        self.__id = id
        self.__value = value * round
        self.__question = question
        self.__answer = answer
        self.__answered = False

    # Returns the square ID
    def getID(self):
        return self.__id

    # Returns the square value
    def getValue(self):
        return self.__value

    # Returns the square question
    def getQuestion(self):
        return self.__question

    # Returns the square answer
    def getAnswer(self):
        return self.__answer

    # Sets the square as answered
    def setAnswered(self):
        self.__answered = True

    # Returns if the square has been answered
    def isAnswered(self):
        return self.__answered

    # Prints the square
    def printSquare(self):
        print(str(self.__id) + ": " + str(self.__value) + " (" + str(self.__answered) + ")")
        print(self.__question)
        print(self.__answer)