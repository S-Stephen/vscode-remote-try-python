# Mergesort
import random


def merge(arrLeft,arrRight):
    """
    unshift lowest each time onto array
    shift <- unshift -> [] <- push -> pop
    """
    # return array if one is empty
    if len(arrRight) < 1:
        return arrLeft
    if len(arrLeft) < 1:
        return arrRight

    leftValue = arrLeft.pop()
    rightValue = arrRight.pop()

    if leftValue < rightValue:
        arrLeft.append(leftValue)
        value = rightValue
    else:
        arrRight.append(rightValue)
        value = leftValue

    return merge(arrLeft,arrRight)+[value]

def mergeSort(arr):
    """Merge sort
        if array size > 1 split array in half
    """

    if len(arr)<2:
         return arr

    arrLeft = arr[:int(len(arr)/2)]
    arrRight = arr[int(len(arr)/2):]

    return merge(mergeSort(arrLeft),mergeSort(arrRight))

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

    myArr = generateRandomPercentages(1000)

    myArr2=myArr
    print(mergeSort(myArr))
