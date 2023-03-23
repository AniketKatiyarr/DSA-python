#find missing number in given set of integer from 1 to 1000
#Method 1 that is mine
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25]

total = 0
for i in range(1,26):
    total += i

sum = 0
for item in list:
    sum += item
print(sum)

value = total - sum 
if value == 0:
    print("integers are not missing from 1 to 25")
else:
    print("The integer is missing:",value)
    
    

# Method 2 that that is by Udemy:
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def findMissing(mylist,n):
    sum1 = (n*(n+1))/2
    sum2 = sum(mylist)
    print(sum1-sum2)

findMissing(mylist,30)


