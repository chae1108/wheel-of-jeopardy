from classes.Sector import Sector
from random import Random

class Wheel:

    def __init__(self, categoryNames):
        sectorNames = self.__getSectorNames(categoryNames)
        self.__sectors = self.__createSectors(sectorNames)

    # Returns a list of all the sector names. Sectors alternate between a category and other sector types
    def __getSectorNames(self, categoryNames):
        sectorNames = ["Lose Turn", "Free Turn", "Bankrupt", "Player's Choice", "Opponents' Choice", "Double Score"]

        #alternates the category names with the other sector types
        index = 0
        for name in categoryNames:
            sectorNames.insert(index, name)
            index += 2

        return sectorNames

    # Returns a list of the sectors of the wheel
    def __createSectors(self, sectorNames):
        sectors = []
        index = 0
        for name in sectorNames:
            sector = Sector(index, name)
            sectors.append(sector)
            index += 1

        return sectors

    # Returns the sector type once the wheel spins
    def spin(self):
        index = Random()
        index = index.randrange(0, 12)
        sector = self.__sectors[index]
        sectorID = sector.getID()
        return sectorID

    # Prints the wheel
    def printWheel(self):
        for sector in self.__sectors:
            sector.printSector()
