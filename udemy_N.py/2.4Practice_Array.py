# arr = [1,2,3,4,5]
# for i in range(len(arr)):
#     print(arr[i],end=" ")

from array import *
arr1 = array('i',[1,2,3,4,5,6,7,8,9])

def traverse(arr1):
    for i in range(len(arr1)):
        print(arr1[i],end=" ")
        
traverse(arr1)
print()

#acess element thorugh index of array
print("elemnt")
print(arr1[3])


#apend any value to the array using append

arr1.append(11)
print(arr1)

#insert an element through given things
arr1.insert(10,12)
print(arr1)

# reverse array
arr1.reverse()
print(arr1)

#extend the given array
arr2 = array('i',[11,22,33])
arr1.extend(arr2)
print(arr1)

#from list append the list value in given array
temp  = [44,55,66]
arr1.fromlist(temp)
print(arr1)

#value using index
print("step11")
print(arr1.index(3)) 


#get array buffer information through buffer_info method()
print(arr1.buffer_info())

#count the array integer
print(arr1.count(11))

#tostring()method convert array into string
#change from tostring() method to tobytes method() 
print(arr1.tobytes())
# print(arr1.frombytes())


#slice our array
print(arr1[1:5])
