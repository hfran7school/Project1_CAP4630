"""
Detailed description of the module.

Author: Hailey Francis
Version: 1/31/22
Email: n01402670@unf.edu
"""

from State import State;


def makeList():
    stateList = []
    file = open("States.csv", "r")
    for ln in file:
        stateVals = ln.split(",")
        currState = State(stateVals[0], stateVals[1], stateVals[2], stateVals[3], stateVals[4], stateVals[5], stateVals[6], stateVals[7], stateVals[9])
        stateList.append(currState)
    del stateList[0] #remove header
    return stateList
#print state report
def printReport(stateList):
    print(f"{'State' : <15}{'Capitol' : <15}{'Reigon' : <15}{'House Seats' : <15}{'Covid Cases' : <15}{'Covid Deaths' : <15}{'Full Vax Rate' : <15}{'Median House Income' : <15}{'Violent Crime' : <15}")
    print(stateList[0])
    
    
#sort states by name using quick sort

#sort states by case fatality rate (using Merge sort, 
#case fatality rate is the rate of deaths over cases)

#find and print a state for a given name 
#using binary search if sorted by name
#sequential if not

#print Spearmans p correlation matrix


print("CAP4630 Project 1")
print("Author: Hailey Francis")
stateList = makeList()
printReport(stateList)











