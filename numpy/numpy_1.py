import numpy as np
import operator as op

# program 1
array = np.array(eval(input("Enter 10 numbers separated by commas:")))
arrayPositive = np.array(list(filter(lambda x: x >0 , array)))
print(array, arrayPositive)

# program 3
array =np.zeros((4,4))
print(array)



# program 4
array = np.arange(12)
index =  eval(input("Enter the index position of the list"))
array = np.delete(array , index)
print(array)

# program 6
array = np.reshape(np.arange(8) ,(4,2))
attributeList = [array.shape , array.ndim, array.itemsize , array.size, array.dtype]
print(attributeList , array)

# program 7
array = np.reshape(np.arange(20) ,(5,4))
dimensions = list(array.shape)
oddRows= list(filter( lambda x : x %2 ==1 ,np.arange(dimensions[0])))
oddColumn = list(filter( lambda x : x %2 ==0 ,np.arange(dimensions[1])))
arrayNewR = list(map(lambda x : array[x,:] , oddRows))
arrayNewC = list(map(lambda x : array[:,x] , oddColumn))
print(arrayNewR, arrayNewC)

# program 10
array = np.reshape(np.linspace(10,30,10) , (5,2))


# program 12
array= np.reshape(np.arange(9) ,(3,3))
print(array[:1,:3])
# [[0 1 2]]
print(array[::-1 , ::-1])
# [[8 7 6]
#  [5 4 3]
#  [2 1 0]]
print(array[:3 , ::2])
# [[0 2]
#  [3 5]
#  [6 8]]


# program 13
# Ans : <class "numpy.ndarray">

# program 14
operatorDictionary = {"sum": op.add , "sub" : op.sub , "mul" : op.mul ,"div" : op.truediv } 
array1 = np.array(eval(input("Enter a array with four elements: ")))
array2 = np.array(eval(input("Enter a array with four elements: ")))
bleh = input("Enter the operation: ")
print(operatorDictionary[bleh](array1, array2))