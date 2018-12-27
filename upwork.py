# Function which returns a list containing tuples of numbers whose sum is equal to sumRequired
# Assumes positive integers
# It uses a dictionary for storing the numbers. For every number in the array, num, it checks if sumRequired - num has been encountered before and if it is, we have a found a valid tuple.
# Completes in O(n) time where n is the size of input array (Auuming hasing in python dictionary takes O(1) time
def findPairsForSum(inputArray, sumRequired):
    numbersMap = {}
    outputList = []
    for num in inputArray:
        if num < sumRequired and (sumRequired-num) in numbersMap:
            outputList.append((num, sumRequired-num))
        else:
            numbersMap[num] = True

    return outputList

def convertToValue(outputSet, inputArray):
    output = []
    for subset in outputSet:
        output.append(set(map(lambda idx : inputArray[idx], subset)))
    return output

# Function which returns the minimum length subsets whose numbers sum up to the required value. Assumes positive integers.
# Uses a dp approach. Lets say f(s, l) denotes a list of subsets where each subset has sum s and length l and sum required is S, then
# to calculate f(s,l), find for each num in input array, f(S-num, l-1)) and then add num to each of those subsets.
def findMinLengthSubsetsForSum(inputArray, sumRequired):
    previousOutput = [set() for i in range(sumRequired+1)]
    lenInputArray = len(inputArray)
    for idx in range(0,lenInputArray):
        num = inputArray[idx]
        previousOutput[num] = {frozenset().union({idx})}
    for subsetLength in range(2, len(inputArray) + 1):
        currentOutput = [set() for i in range(sumRequired+1)]
        for idx in range(0,lenInputArray):
            num = inputArray[idx]
            for previousSum in range(1, sumRequired-num + 1):
                previousSubsets = previousOutput[previousSum]
                for subset in previousSubsets:
                    if not(idx in subset): 
                        currentOutput[num+previousSum].add(subset.union({idx}))
        if len(currentOutput[sumRequired]) > 0:
            return convertToValue(currentOutput[sumRequired], inputArray)
        previousOutput = currentOutput
    return set()
        
# Takes input from a file in the following format:
# First line: sumRequired (the number to sum to for elements in the input array)
# second line: input array where numbers are seperated by spaces
with open('input') as inputFile:
    sumLine = inputFile.readline()
    sumRequired = int(sumLine)
    inputArrayStr = inputFile.readline().split()
    inputArray = list(map(lambda numberStr: int(numberStr), inputArrayStr))
    print(findMinLengthSubsetsForSum(inputArray, sumRequired))
