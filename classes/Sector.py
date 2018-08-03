class Sector:

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    # Returns the sector ID
    def getID(self):
        return self.__id

    # Returns the sector name
    def getName(self):
        return self.__name

    # Prints the sector
    def printSector(self):
        print(str(self.__id) + ": " + self.__name)