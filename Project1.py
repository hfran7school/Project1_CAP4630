"""
Detailed description of the module.

Author: Hailey Francis
Version: 2/2/22
Email: n01402670@unf.edu
"""

from State import State;

#print options menu    
def printMenu():
    print("\n1. Print a state report")
    print("2. Sort by name ")
    print("3. Sort by case fatality rate")
    print("4. Find and print a State for a given name")
    print("5. Print Spearman’s rho matrix")
    print("6. (Quit)")

#create state list
def makeList():
    stateList = []
    file = open("States.csv", "r")
    for ln in file:
        stateVals = ln.split(",")
        currState = State(stateVals[0], stateVals[1], stateVals[2], stateVals[3], stateVals[4], stateVals[5], stateVals[6], stateVals[7], stateVals[8], stateVals[9])
        stateList.append(currState)
    del stateList[0] #remove header
    return stateList

#print state report
def printReport(stateList):
    print(f"{'Name' : <20}{'MHI' : <20}{'VCR' : <20}{'CFR' : <20}{'Case Rate' : <20}{'Death Rate' : <20}{'FVR' : <20}")
    print("----------------------------------------------------------------------------------------------------------------------------")
    for st in stateList:
        print(st)

#print stateInfo
def printStateInfo(state):
    print("\nName: " + state.getName())
    print("MHI: " + state.getMedHouseIncome())
    print("VCR: " + state.getViolentCrimeRate())
    print("CFR: " + str(state.getMortalityRate()))
    print("Case Rate: " + str(state.getCaseRate()))
    print("Death Rate: " + str(state.getDeathRate()))
    print("FV Rate: " + str(state.getFullVaxRate()))

#the partition function
def quickPart(stateList, low, high):
    i = low - 1 #index of smaller element
    pivot = stateList[high] #pivot

    for j in range(low, high): 
        if pivot > stateList[j]: #if pivot larger than curr element
            i = i + 1 #increment index of smaller element
            stateList[i], stateList[j] = stateList[j], stateList[i]
    
    stateList[i+1], stateList[high] = stateList[high], stateList[i+1]
    return (i+1)

#merge sort fatality rate
def sortByFatalityRate(stateList):
    if len(stateList) > 1:
        mid = len(stateList) // 2 #middle
        LEF = stateList[:mid] #left subarray
        RIG = stateList[mid:] #right subarray

        sortByFatalityRate(LEF)
        sortByFatalityRate(RIG)

        i = j = k = 0

        while i < len(LEF) and j < len(RIG):
            stateLeft = LEF[i].getMortalityRate()
            stateRight = RIG[j].getMortalityRate()

            if stateLeft < stateRight:
                stateList[k] = LEF[i]
                i += 1
            else:
                stateList[k] = RIG[j]
                j += 1
            k += 1
        
        while i < len(LEF):
            stateList[k] = LEF[i]
            i += 1
            k += 1
        
        while j < len(RIG):
            stateList[k] = RIG[j]
            j += 1
            k += 1
            
#sort states by name using quick sort
def sortByName(stateList, low, high):
    if len(stateList) == 1:
        return stateList
    if low < high:
        pi = quickPart(stateList, low, high) #pi is partition index
        
        # Separately sort elements before and after partition
        sortByName(stateList, low, pi-1)
        sortByName(stateList, pi + 1, high)

#binary sort
def binarySearch(stateList, stateName):
    lef = 0
    rig = len(stateList) - 1

    while lef <= rig:
        mid = lef + ((rig - lef) // 2)
        if stateList[mid].getName() == stateName:
            return stateList[mid]
        elif stateName > stateList[mid].getName():
            lef = mid + 1
        else:
            rig = mid - 1
    return -1

#sequential sort    
def sequentialSearch(stateList, stateName):
    size = len(stateList)
    i = 0
    while i < size:
        if stateList[i].getName() == stateName:
            return stateList[i]
        else:
            i += 1
    return -1

#find and print a state for a given name 
#using binary search if sorted by name
#sequential if not
def findState(stateList, sortedByName):
    found = -1
    stateName = input("\nEnter the State name: ")
    if sortedByName == True:
        print("Binary Search")
        found = binarySearch(stateList, stateName)
    else:
        print("Sequential Search")
        found = sequentialSearch(stateList, stateName)
    if found != -1:
        printStateInfo(found)
    else:
        print("\nState not found.")

#print Spearmans p correlation matrix


# MAIN #
print("CAP4630 Project 1 -- Python Basics")
print("Author: Hailey Francis (n01402670@unf.edu")
stateList = makeList()
reportLength = len(stateList)
print("\nThere were " + str(reportLength) + " state records read from States.csv")
sortedByName = False

op = -1

while op != "6":
    printMenu()
    op = input("Enter your choice: ")
    if(op == "1"):
        printReport(stateList)
    elif(op == "2"):
        sortByName(stateList, 0, reportLength - 1)
        sortedByName = True
        print("\nState records now sorted alphabetically by state name.")
    elif(op == "3"):
        sortByFatalityRate(stateList)
        sortedByName = False
        print("\nState records now sorted by fatality rate (ascending).")
    elif(op == "4"):
        findState(stateList, sortedByName)
    elif(op == "5"):
        #print Spearman's rho matrix
        i = 0
    elif(op == "6"):
        print("\nThank you! Goodbye!\n")
    else:
        print("\nInvalid Option. Please try again!")













