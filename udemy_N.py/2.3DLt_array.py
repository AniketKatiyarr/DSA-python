from array import *
 
arr1 = array = ['i',1,2,3,4,5,6,7,8,]

def dlt(arr1,val):
    for i in arr1:
        if i == val:
            arr1.remove(val)
            for i in range(len(arr1)):
                print(arr1[i],end=" ")
    else:
      return -1


dlt(arr1,6)
dlt(arr1,10)
