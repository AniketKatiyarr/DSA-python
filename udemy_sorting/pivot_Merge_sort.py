def swap(list,index1,index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    
def pivot(list,pivot_index,end_index):
    swap_index = pivot_index
    
    for i in range(pivot_index+1,end_index+1):
        if list[i] <list[pivot_index]:
            swap_index +=1
            swap(list,swap_index,i)
    swap(list,swap_index,pivot_index)
    return swap_index

list = [4,6,7,2,1,8,9,3]

print(pivot(list,0,6))
print(list)
