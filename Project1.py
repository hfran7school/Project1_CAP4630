"""
This program will take States.csv
and create a list of State objects that
contain information about each state in
the file.
The user will be able to select from 5
different option: printing a report, 
sorting the States by either name or
case fatality rate, searching for a 
specific state's information, and
giving a Spearman's rho matrix based
on the data.

Author: Hailey Francis
Version: 2/3/22
Email: n01402670@unf.edu
"""
from State import State;

def printMenu():
    """
    This function prints the menu options for the user to select
    from.

    :param N/A
    :return N/A
    """
    print("\n1. Print a state report")
    print("2. Sort by name ")
    print("3. Sort by case fatality rate")
    print("4. Find and print a State for a given name")
    print("5. Print Spearman’s rho matrix")
    print("6. (Quit)")

def makeList():
    """
    Opens States.csv and reads it, creates a State object from
    each line and appends it to a list, then returns the list.

    :param N/A
    :return list of State objects from the States.csv file
    """
    stateList = []
    file = open("States.csv", "r")
    for ln in file:
        stateVals = ln.split(",")
        currState = State(stateVals[0], stateVals[1], stateVals[2], stateVals[3], stateVals[4], stateVals[5], stateVals[6], stateVals[7], stateVals[8], stateVals[9])
        stateList.append(currState)
    del stateList[0] #remove header
    return stateList

def printReport(stateList):
    """
    Prints the States report for the user,
    includes name, median house income, violent
    crime rate, Case Rate, Death Rate, and full
    vaccination rate.

    :param list of State objects
    :return N/A
    """
    print(f"{'Name' : <20}{'MHI' : <20}{'VCR' : <20}{'CFR' : <20}{'Case Rate' : <20}{'Death Rate' : <20}{'FVR' : <20}")
    print("------------------------------------------------------------------------------------------------------------------------------")
    for st in stateList:
        print(st)

def printStateInfo(state):
    """
    Prints the information of a specific State
    for the user, includes name, median house income,
    violent crime rate, Case Rate, Death Rate, and full
    vaccination rate.

    :param State object
    :return N/A
    """
    print("\nName: " + state.getName())
    print("MHI: " + state.getMedHouseIncome())
    print("VCR: " + format(state.getViolentCrimeRate(), '.1f'))
    print("CFR: " + format(state.getMortalityRate(), '.6f'))
    print("Case Rate: " + format(state.getCaseRate(), '.2f'))
    print("Death Rate: " + format(state.getDeathRate(), '.2f'))
    print("FV Rate: " + format(state.getFullVaxRate(), '.3f'))

def quickPart(stateList, low, high):
    """
    This is the partition function that is used by
    the sortByName function, which is an implementation
    of Quick Sort.

    :param list of State objects, low index, high index
    :return the next partition index
    """
    i = low - 1 #index of smaller element
    pivot = stateList[high] #pivot

    for j in range(low, high): 
        if pivot > stateList[j]: #if pivot larger than curr element
            i = i + 1 #increment index of smaller element
            stateList[i], stateList[j] = stateList[j], stateList[i]
    
    stateList[i+1], stateList[high] = stateList[high], stateList[i+1]
    return (i+1) #next partition index

def sortByName(stateList, low, high):
    """
    This is the implementation of quick sort
    that will sort the the States in the given
    list in alphabetical order.

    :param list of State objects, low index, high index
    :return the sorted State list
    """
    if len(stateList) == 1:
        return stateList
    if low < high:
        pi = quickPart(stateList, low, high) #pi is partition index
        
        # Separately sort elements before and after partition
        sortByName(stateList, low, pi-1)
        sortByName(stateList, pi + 1, high)

def mergeSort(stateList, sortBy):
    """
    This is the implementation of merge sort.
    Based on the given parameter, it will sort
    the data by its CFR, MHI, VCR, FVR, Case
    Rate, or Death Rate. Sorting by CFR is used
    when the user wants to sort the states report
    by fatality rate, and the rest are used for 
    finding Spearman Rho.

    :param list of State objects
    :return N/A (the list will be sorted)
    """
    if len(stateList) > 1:
        mid = len(stateList) // 2 #middle
        LEF = stateList[:mid] #left subarray
        RIG = stateList[mid:] #right subarray

        mergeSort(LEF, sortBy)
        mergeSort(RIG, sortBy)

        i = j = k = stateLeft = stateRight = 0

        while i < len(LEF) and j < len(RIG):
            if sortBy == "CFR":
                stateLeft = LEF[i].getMortalityRate()
                stateRight = RIG[j].getMortalityRate()
            elif sortBy == "MHI": #med house income
                stateLeft = LEF[i].getMedHouseIncome()
                stateRight = RIG[j].getMedHouseIncome()
            elif sortBy == "VCR": #violent crime rate, saved as a string so coverting to float
                stateLeft = LEF[i].getViolentCrimeRate()
                stateLeft = float(stateLeft)
                stateRight = RIG[j].getViolentCrimeRate()
                stateRight = float(stateRight)
            elif sortBy == "FVR": #full vax rate
                stateLeft = LEF[i].getFullVaxRate()
                stateRight = RIG[j].getFullVaxRate()
            elif sortBy == "Case Rate": #case rate
                stateLeft = LEF[i].getCaseRate()
                stateRight = RIG[j].getCaseRate()
            elif sortBy == "Death Rate": #death rate
                stateLeft = LEF[i].getDeathRate()
                stateRight = RIG[j].getDeathRate()

            if stateLeft == stateRight:
                stateLeft = LEF[i]
                stateRight = RIG[j]

            if stateRight > stateLeft:
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
        return stateList

def binarySearch(stateList, stateName):
    """
    This is an implementation of a binary
    search that will find the State by its
    name.

    :param list of State objects, name of State to be searched
    :return State if found, -1 if not found
    """
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
    
def sequentialSearch(stateList, stateName, rho):
    """
    This is the implementation of sequential search,
    and will either return the state object itself, or
    it will return the index of the object in the list if
    we are working with Spearman Rho.

   :param list of State objects, name of State to be searched, rho boolean
    :return State or index if found, -1 if not found
    """
    size = len(stateList)
    i = 0
    while i < size:
        if stateList[i].getName() == stateName:
            if rho == False:
                return stateList[i]
            else:
                return i
        else:
            i += 1
    return -1

def findState(stateList, sortedByName):
    """
    This function runs either binary or
    sequential sort based on whether the
    boolean sortedByName is True or False.
    It takes the result of the search and either
    calls the printStateInfo function if the State
    was found, or tells the user that the state wasn't
    found otherwise.

    :param list of State objects, sortedByName boolean
    :return N/A
    """
    found = -1
    stateName = input("\nEnter the State name: ")
    if sortedByName == True:
        print("Binary Search")
        found = binarySearch(stateList, stateName)
    else:
        print("Sequential Search")
        found = sequentialSearch(stateList, stateName, False)
    if found != -1:
        printStateInfo(found)
    else:
        print("\nState not found.")

def SpearmansMatrix(stateList):
    """
    This function computes and prints the
    Spearman Rho matrix of the states in the
    stateList. It copies the stateList into new
    arrays, and then those arrays are sorted with
    merge sort. 

    The 6 Spearmans rho values are then calculated
    and formatted, then printed to a table on the
    terminal.

    :param list of State objects
    :return N/A
    """
    CaseRate = stateList.copy()
    DeathRate = stateList.copy()
    MHI = stateList.copy()
    VCR = stateList.copy()
    FVR = stateList.copy()

    mergeSort(CaseRate, "Case Rate")
    mergeSort(DeathRate, "Death Rate")
    mergeSort(MHI, "MHI")
    mergeSort(VCR, "VCR")
    mergeSort(FVR, "FVR")

    x1 = format(SpearmansRho(CaseRate, MHI), '.4f')
    x2 = format(SpearmansRho(CaseRate, VCR), '.4f')
    x3 = format(SpearmansRho(CaseRate, FVR), '.4f')
    x4 = format(SpearmansRho(DeathRate, MHI), '.4f')
    x5 = format(SpearmansRho(DeathRate, VCR), '.4f')
    x6 = format(SpearmansRho(DeathRate, FVR), '.4f')

    print("--------------------------------------------------------------------")
    print("|             |     MHI         |     VCR         |     FVR        |")
    print("--------------------------------------------------------------------")
    print("|  Case Rate  |     "+str(x1)+"     |     "+str(x2)+"     |     "+str(x3)+"     |")
    print("--------------------------------------------------------------------")
    print("|  Death Rate |     "+str(x4)+"     |     "+str(x5)+"     |     "+str(x6)+"     |")
    print("--------------------------------------------------------------------")
   
def SpearmansRho(stateListR1, stateListR2):
    """
    This function calculates the Spearmans Rho
    value for two different attributes of the stateList.
    This is done by using two lists in the parameter, each
    sorted by the attributes we want to compare, so that
    we are able to use sequential search to get the index
    (rank), for each state's attribute.

    :param 2 list of the same State objects sorted by different attributes
    :return Spearman's Rho value
    """
    size = len(stateListR1) #R1 and R2 should be the same length
    sum_di_p2 = 0
    i = 0
    while i < size:
        name = stateListR1[i].getName()
        r1_index = sequentialSearch(stateListR1, name, True)
        r2_index = sequentialSearch(stateListR2, name, True)
        di_p2 = (r1_index - r2_index)**2
        sum_di_p2 += di_p2
        i += 1
    
    rho = float(1 - ((6 * sum_di_p2) / (size * (size**2 - 1))))
    return rho

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
        stateList = mergeSort(stateList, "CFR")
        sortedByName = False
        print("\nState records now sorted by fatality rate (ascending).")
    elif(op == "4"):
        findState(stateList, sortedByName)
    elif(op == "5"):
        SpearmansMatrix(stateList)
        i = 0
    elif(op == "6"):
        print("\nThank you! Goodbye!\n")
    else:
        print("\nInvalid Option. Please try again!")













