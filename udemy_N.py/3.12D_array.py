#first method to make a matrix
import numpy as np

TwoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(TwoDArray)


#Second method to make a 2D matrix
row = int(input())
col = int(input())
m = []

for i in range(row):
    l = []
    for j in range(col):
        v = int(input())
        l.append(v)
    m.append(l)

print(m)


#Third method to make a matrix    

row = int(input())
column = int(input())

d = [[0 for col in range(column)]for roww in range(row)]

for roww in range(row):
    for col in range(column):
        d[roww][col] = roww*col 
print(d)