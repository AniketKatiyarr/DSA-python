row=  int(input(("enter number of rows:")))
column= int(input(("enter number of column:")))
d = [[0 for col in range(column)] for r in range(row)]

for r in range(row):
    for col in range(column):
        d[r][col] = r*col
print(d)
 
x=int(input('how many cars do you have')) 
a=[] 
for i in range(x): 
    car=int((input('enter your car name'))) 
    a.append(car)
print(a)
y=[] 
for i in range(len(a)-1,-1,-1): 
    y.append(a[i])
print(y)


    