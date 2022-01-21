# Quicksort
import random

def bubbleSort(arr):
    notSorted = True
    ops=0
    while notSorted:
        # pop top element from arr
        curr = arr.pop()
        notSorted = False

        for index in range(len(arr)):
            #print("help")
            ops+=1
            # pop next element and compare to current element
            next = arr.pop()
            #print(f'{next} > {curr}')
            if next > curr:
                arr = [next] + arr
                notSorted = True
            else:
                arr = [curr] + arr
                curr = next
        arr = [curr] + arr


    print(f'ops: {ops} vs {len(arr)*len(arr)}')
    return arr

# generate a list to sort
myArr = [] 
for loop in range(10):
    myArr.append(random.randint(1,100))

# print(bubbleSort(myArr2))

if __name__ == '__main__':

    print(myArr)
    myArr2=myArr
    #myArr.sort()
    print(myArr2)
    myArr1 = bubbleSort(myArr2)
    print("Sort again")
    print(bubbleSort(myArr1))