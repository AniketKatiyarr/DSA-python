#ARRAY lIST pRACTICE


#1 
''' Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3] '''

def middle(lst):
    # TODO
    l = []
    for i in range(1,len(lst)-1):
        l.append(lst[i])
    return l



#2
'''
2D Lists
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
sumDiagonal(myList2D) # 15'''

def sumDiagonal(a):
    # TODO
    total= 0
    for i in range(len(a)):
        for j in range(len(a[0])):
                if i == j  :
                   total += a[i][j]
    return total


#3
''''''


def firstsecond(l):
    l.sort()
    print(l)
    # for i in  l:
    print(l[len(l)-1],l[(len(l))-2])
        
l = [6,4,9,7,2,5,0,1,8,100,99]
firstsecond(l)


# def f(l):
#     a = l
#     a.sort(reverse = True)
#     print(a)
    
#     first = a[0]
#     second =  None
    
#     for i in l:
#         if i != first:
#           second = i
#         return first,second
# l = [44,55,77,22,11,66,33,99,100]
# print(f(l))    


# l = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5]
# p = set(l)
# p.sort()
# print(p)


'''
Pairs
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

pairSum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']'''
def pairSum(myList, sum):
    # TODO
    result = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) +'+'+ str(myList[j]))
    return result

l = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]                
print(pairSum(l,7)) 