#Pairs sum of two value and return index of it
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def pairsSum(list,target):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] + list[j] == target:
                # return "It is there at"+str(i,j)+str(j),"position"
                print([i,j])
            
    return "None"

pairsSum(list,29)



#Check Value is present or not in an array

import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def FindNumber(array,n):
    for i in range(len(array)):
        if array[i] == n:
            print("value is presetna at:-",i)

FindNumber(array,10)
 
        