n = int(input("How many days' temprature?"))
total = 0
list = []
for i in range(1,n+1):
    print("Day",i,"'s high temp:",end=" ")
    val =  int(input())
    total += val
    list.append(val)
average = (total / n) 
print("average",average)

count = 0
for i in range(len(list)):
    if list[i] > average:
        count += 1
    else: 
        pass
    
print(count,"day(s) above average")



#Second method--------------------!!!!!!!!!11

n = int(input("How many days' temprature?"))
total = 0
list = []
for i in range(1,n+1):
    val = int(input("Days"+str(i)+ "'s high temp:"))
    total += val
    list.append(val)
average = (total / n) 
print("average",average)

count = 0
for i in list:
    if i > average:
        count += 1
    else: 
        pass
    
print(count,"day(s) above average")