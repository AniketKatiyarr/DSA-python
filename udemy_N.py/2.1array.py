from array import *

arr1= array('i',[1,2,3,4,5,6,7,8])
arr2= array('d',[1.1,2.1,3.3,4.2,5.7,6.2,7.1,8.9])
print(arr1)
print(arr2)

arr1.insert(8,10)
print(arr1)
arr1.insert(0,0)
print(arr1)


print("array in traversal method:-")
def traversal(arr1):
    for i in arr1:
        print(i,end=" ")

traversal(arr1)


print("accessing index by:-")

def acess(array,index):
    if index> len(array):
        return -1
    else:
        print(array[index])
        
acess(arr1,8)
