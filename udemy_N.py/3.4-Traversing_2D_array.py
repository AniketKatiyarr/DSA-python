import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])

def TraverseTwoDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
#- Put here 0 means it give the value of all columns
          print(array[i][j],end=" ")

TraverseTwoDArray(array)



            
 