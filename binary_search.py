'''
binarysearch(arr,size)
 loop until beg is not equal to end
   midlindex = (beg+end)/2
     if(item ==arr[midlindex])
      return midlindex
    elif (item>arr[index])
    beg = midlindex+1
    
    else:
         elif (item<arr[index])
    beg = midlindex  - 1
    
'''
def binarysearch(array,search,beg,end):
    
    while beg <= end:
        
        mid = beg + (end-beg)//2
        
        if array[mid] == search:
           return mid
        elif array[mid]<search:
            beg = mid+1
        else:
            end = mid-1
    return -1

array = [1,2,3,4,45,6,7,8,9,7,55,33,24,78,43]
search = 3
result = binarysearch(array,search,0,len(array)-1)
if result != -1:
    print("element present at index:",result)
else:
    print("not found")
 
 
