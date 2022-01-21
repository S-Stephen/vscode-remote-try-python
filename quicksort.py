# Quicksort
import random


def quickSort(arr):
    """Quick sort:
        selects a pivot then
        scanindex starts at the begining of the array and compares its value with the pivots value
        if val > pivot value leave in place
        if val < pivot value 
            increment endlower (index) 
            swap val with end lower

        Note: maximum recursion depth may be reached for large lists (100,000)

        To query and set recursion depth (which will vary depemding on the pivots found)
        
        import sys
        print(sys.getrecursionlimit())
        sys.setrecursionlimit(1500)
        """
    if len(arr)<2:
        # length could be 0,1
        return arr

    # it would be better to randomly select our pivot - but scanning is complicated
    # pivotIndex = random.randint(0,len(arr)-1)

    pivotIndex=len(arr)-1
    endlower=0
    scanindex=0
    while scanindex < len(arr)-1:
        val = arr[scanindex]
        if arr[scanindex] < arr[pivotIndex]:
            arr[scanindex]=arr[endlower]
            arr[endlower]=val
            endlower+=1
        scanindex+=1

    return quickSort(arr[:endlower])+[arr[pivotIndex]]+quickSort(arr[endlower:-1])

def generateRandomPercentages(length):
    """
    Produce a list of Integer percentages
    """
    # generate a list to sort
    myArr = [] 
    for loop in range(length):
        myArr.append(random.randint(1,100))

    return myArr

if __name__ == '__main__':

    myArr = generateRandomPercentages(100000)
    #print(myArr)
    myArr2=myArr
    #print(quickSort(myArr))