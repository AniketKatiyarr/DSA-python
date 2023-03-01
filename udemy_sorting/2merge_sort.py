def merge(left , right):
    combined = []
    i = 0
    j = 0
    while i <len(left) and j < len(right):
        if left[i] <right[j]:
            combined.append(left[i])
            i +=1
        else:
            combined.append(right[j])
            j += 1
    while i< len(left):
        combined.append(left[i])
        i +=1
    while j< len(right):
        combined.append(right[j])
        j +=1
    return combined



#second method we use here  sort the array in base level and then merge.
def merge_sort(list):
    if len(list) ==1:
        return list
    mid_index = int(len(list)/2)
    left = merge_sort(list[:mid_index])
    right = merge_sort(list[mid_index:])
    
    return merge(left,right)


original_list = [3,1,2,4]

sorted_list = merge_sort(original_list)

print("original list:",original_list)

print("\nsorted list",sorted_list)

