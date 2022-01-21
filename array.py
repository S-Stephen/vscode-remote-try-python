import numpy as np

# array produced from numpy
# https://www.askpython.com/python-modules/numpy/python-numpy-arrays

myArray = np.random.randint(1,101,10000)

# Search is O(n)

findValue=23;
occurances=0
for value in range(len(myArray)):
    if myArray[value] == 23:
        occurances+=1
        
plural='' if occurances == 1 else 's'

print(f'value {findValue} found {occurances} time{plural}')


# Insert is O(n) - though this is cheating also

indexToInsert=10
valueToInsert = 1001
insertedArray = np.array((), dtype=np.int8)

for index in range(len(myArray[0:20])):
    if index == indexToInsert:
        insertedArray = np.append(insertedArray,np.array([valueToInsert]))

    insertedArray = np.append(insertedArray,np.array([myArray[index]]))
    
print(f'inserted Array {insertedArray}')

# cheat

arrayStart = np.concatenate((myArray[0:20][0:indexToInsert],np.array([valueToInsert])))

print(f'inserted Array2 {np.concatenate((arrayStart,myArray[0:20][indexToInsert:]))}')

# delete is O(n)

deletedArray=np.array(())
removeIndex=10
for value in range(len(insertedArray)):
    if value != removeIndex:
        deletedArray = np.append(deletedArray,np.array([insertedArray[value]]))

print(f'deleted Array: {deletedArray}')

# cheat numpy.delete():

print(f'{np.delete(insertedArray,10)}')