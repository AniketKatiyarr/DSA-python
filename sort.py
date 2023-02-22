import array

arr = array.array('i',[1,2,3,1,2,5])
print("\nthe new created array:")
for i in range(0,6):
    print(arr[i],end=" ")
print("\nThe index of 2 occur:",arr.index(2))
print("\nthe index of 1st occurence:",arr.index(1))

