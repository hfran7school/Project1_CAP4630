"""
Detailed description of the module.

Author: Hailey Francis
Version: 1/31/22
Email: n01402670@unf.edu
"""

from State import State;

#create state list
def makeList():
    stateList = []
    file = open("States.csv", "r")
    for ln in file:
        stateVals = ln.split(",")
        currState = State(stateVals[0], stateVals[1], stateVals[2], stateVals[3], stateVals[4], stateVals[5], stateVals[6], stateVals[7], stateVals[9])
        stateList.append(currState)
    del stateList[0] #remove header
    print("\nThere were " + str(len(stateList)) + " state records read from States.csv")
    return stateList

#print state report
def printReport(stateList):
    print(f"{'State' : <20}{'Capitol' : <20}{'Reigon' : <20}{'House Seats' : <20}{'Covid Cases' : <20}{'Covid Deaths' : <20}{'Full Vax Rate' : <20}{'Med House Income' : <20}{'Violent Crime' : <20}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for st in stateList:
        print(st)

#print options menu    
def printMenu():
    print("\n1. Print a state report")
    print("2. Sort by name ")
    print("3. Sort by case fatality rate")
    print("4. Find and print a State for a given name")
    print("5. Print Spearman’s rho matrix")
    print("6. Quit)")

#the partition function
def quickPart(stateList, low, high):
    i = low - 1 #index of smaller element
    pivot = stateList[high] #pivot

    for j in range(low, high): 
        if pivot > stateList[j]: #if curr element <= pivot
            i = i + 1 #increment index of smaller element
            stateList[i], stateList[j] = stateList[j], stateList[i]
    
    stateList[i+1], stateList[high] = stateList[high], stateList[i+1]
    return (i+1)

#sort states by name using quick sort
def sortByName(stateList, low, high):
    if len(stateList) == 1:
        return stateList
    if low < high:
        pi = quickPart(stateList, low, high) #pi is partition index
        
        # Separately sort elements before and after partition
        sortByName(stateList, low, pi-1)
        sortByName(stateList, pi + 1, high)

#sort states by case fatality rate (using Merge sort, 
#case fatality rate is the rate of deaths over cases)

#find and print a state for a given name 
#using binary search if sorted by name
#sequential if not

#print Spearmans p correlation matrix


print("CAP4630 Project 1")
print("Author: Hailey Francis")
stateList = makeList()
op = -1

while op != "6":
    printMenu()
    op = input("Enter your choice: ")
    if(op == "1"):
        printReport(stateList)
    elif(op == "2"):
        print("\nState records now sorted alphabetically by state name.")
        sortByName(stateList, 0, len(stateList) - 1)
    elif(op == "3"):
        #sort by case fatality rate
        i = 0
    elif(op == "4"):
        #find and print a state for a given name
        i = 0
    elif(op == "5"):
        #print Spearman's rho matrix
        i = 0
    elif(op == "6"):
        print("Thank you! Goodbye!")













