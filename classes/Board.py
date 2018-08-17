from classes.Category import Category

class Board:

    def __init__(self, categories, round):
        self.__categories = self.__createCategories(categories, round)

    # Returns a list of category objects from the list provided by the game
    def __createCategories(self, categories, round):
        categoryObjects = []

        id = 0
        for cat in categories:
            category = Category(id, cat, round)
            categoryObjects.append(category)
            id += 1

        return categoryObjects

    # Returns if a category, based upon an ID, is available to play
    def isCategoryAvailable(self, id):
        category = self.__categories[id]
        if category.isAvailable():
            return True
        else:
            return False

    # Plays a category based upon an ID
    def playCategory(self, id):
        categorySelected = self.__categories[id]
        square = categorySelected.getAvailableSquare()
        return square

    # Prints the board
    def printBoard(self):
        for category in self.__categories:
            category.printCategory()
