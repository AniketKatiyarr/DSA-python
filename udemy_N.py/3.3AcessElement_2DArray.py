import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array)

def access_element(array,rowindex,colindex):
    if rowindex >= len(array) or colindex >= len(array):
        print("Incorrect index out of range")
    else:
        print(array[rowindex][colindex])

print("The value acees by index is:-")
access_element(array,1,1)
access_element(array,1,1)
access_element(array,1,2)


