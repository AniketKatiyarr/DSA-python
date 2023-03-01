def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

print(bubble_sort([4,2,6,5,1,3]))


def bubble(list):
    for i in range((len(list)-1,0,-1)):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

print(bubble_sort([55,33,22,88,77,11,99,44]))
                    
