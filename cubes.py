from http.client import REQUESTED_RANGE_NOT_SATISFIABLE


cubes = []
for i in range(1,11):
    cubes.append(i**3)
    
print(cubes)
    
    
#2 even list comprehension

even =[]
for  num in range(1,100):
    if num%2==0:
        even.append(num)
        print(even) 