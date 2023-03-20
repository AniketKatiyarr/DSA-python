from array import *
arr1 = array('i',[1,2,3,4,5,6,7,8])
print(arr1)

def search(arr1,search):
    for i in arr1:
        if i == search:
            return arr1.index(search)
            

    return "The element does not exist in this array"
    
print(search(arr1,6))



from array import *

arr2 = array('i',[21,32,34,56,87,56,43])


def search(arr2,search):
    for i in arr2:
        if i==search:
            return arr2.index(search)

    return "none"
print(search(arr2,34))