def insertion_sort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key <array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
array = [5,3,5,4,2,6,1]
insertion_sort(array)
print(array)
 
def insert(array):
    for i in range(1,len(array)):
        temp = array[i]
        j = i-1
        while j<=0 and temp < array[j]:
            array[j+1]  = array[j]
            j = j-1
        array[j+1] = temp
array = [88,55,22,11,44,99,77,66,33]
insertion_sort(array)
print(array)       
         

        
        
        
            