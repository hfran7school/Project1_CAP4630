"""
Detailed description of the module.

Author: Hailey Francis
Version: 1/31/22
Email: n01402670@unf.edu
"""

class State:
    # INITIALIZER #
    def __init__(state, name, capitol, reigon, houseSeats, covidCases, covidDeaths, fullVaxRates, medHouseIncome, violentCrime):
        state.name = name
        state.capitol = capitol
        state.reigon = reigon
        state.houseSeats = houseSeats
        state.covidCases = covidCases
        state.covidDeaths = covidDeaths
        state.fullVaxRates = fullVaxRates
        state.medHouseIncome = medHouseIncome
        state.violentCrime = violentCrime
    
    # GETTER METHODS #
    def getName(state):
        return state.name
    
    def getCapitol(state):
        return state.capitol
    
    def getReigon(state):
        return state.reigon

    def getHouseSeats(state):
        return state.houseSeats

    def getCovidCases(state):
        return state.covidCases

    def getCovidDeaths(state):
        return state.covidDeaths

    def getFullVaxRates(state):
        return state.fullVaxRates

    def getMedHouseIncome(state):
        return state.medHouseIncome

    def getViolentCrime(state):
        return state.violentCrime
    # END OF GETTER METHODS #

    # SETTER METHODS #
    def setName(state, newName):
        state.name = newName

    def setCapitol(state, newCapitol):
        state.capitol = newCapitol

    def setReigon(state, newReigon):
        state.reigon = newReigon

    def setHouseSeats(state, newHouseSeats):
        state.houseSeats = newHouseSeats

    def setCovidCases(state, newCovidCases):
        state.covidCases = newCovidCases

    def setCovidDeaths(state, newCovidDeaths):
        state.covidDeaths = newCovidDeaths

    def setFullVaxRates(state, newFullVaxRates):
        state.fullVaxRates = newFullVaxRates

    def setMedHouseIncome(state, newMedHouseIncome):
        state.medHouseIncome = newMedHouseIncome

    def setViolentCrime(state, newViolentCrime):
        state.violentCrime = newViolentCrime
    # END OF SETTER METHODS #


    #__gt__ and __str__
    def __str__(state):
        return f"{state.getName() : <20}{state.getCapitol() : <20}{state.getReigon() : <20}{state.getHouseSeats() : <20}{state.getCovidCases() : <20}{state.getCovidDeaths() : <20}{state.getFullVaxRates() : <20}{state.getMedHouseIncome() : <20}{state.getViolentCrime() : <20}" 

    def __gt__(state, other):
        return state.name > other.name