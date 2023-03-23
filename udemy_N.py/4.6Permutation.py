def permutation(list1,list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True

list1 = [1,2,3,4]
list2 = [3,4,2,1]    
list3 = [1,2,5,3,6]
print(permutation(list1,list2))
print(permutation(list1,list3))