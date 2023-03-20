def bubble_sort(array,n):
    swap = False
    for i in range(n-1,0,-1):
        for indx in range(i):
            if array[indx] > array[indx+1]:
                temp = array[indx]
                array[indx] = array[indx+1]
                array[indx+1] = temp
        if swap == False:
           break
    

arr = [1,22,345,75,4,332,12,313]
n = len(arr)
result = bubble_sort(arr,n)
print(result)   

#simple as f

def bubble(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] >array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array
l = [23,45,768,9989,5343,23,45]
print(bubble(l))

            
     