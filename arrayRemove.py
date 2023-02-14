print("Enter the size of array:")
a=  int(input())
arr=[]
print("enter",a,"element")
for i in range(a):
    arr.append(int(input()))
print("\nEnter the value to delete:")
val = int(input())
if val in arr:
    arr.remove(val)
    print("\nThe new array is:")
    for i in range(a-1):
      print(arr[i],end =" ")
else:
    print("not done try again\n") 
   
    
