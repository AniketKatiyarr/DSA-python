#---List operation and function -------!!!!

total = 0
count = 0 
while (True):
    inp = input("Enter number:")
    if inp == 'done': 
        break
    else:
        val = float(inp)
        total += val
        count += 1
average = (total/count)
print("Average:" + str(average))


#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def search(mylist,val):
    for i in mylist:
        if val == i:
            return mylist.index(val)
    return "Not Found"

print(search(myList,40))



