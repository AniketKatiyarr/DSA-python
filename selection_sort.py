def selection_sort(array,size):
    for s in range(size):
        min = s
        
        for i in range(s+1,size):
            if array[i] <array[min]:
                min = i
        (array[s],array[min]) = (array[min],array[s])

array = [-34,-54,23,11,90]
size = len(array)
selection_sort(array,size) 
print(array)
               