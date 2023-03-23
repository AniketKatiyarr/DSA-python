import numpy as np

TwoDArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

def search(array,search):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == search:
                print("yes it is present at: " +str(i)+""+str(j))
                print("Row:",i,"Col",j)
    return "None"

search(TwoDArray,4)
search(TwoDArray,8)



def total(a):
    total = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == a[0][0] or a[1][1] or a[2][2]:
                total += a[i][j]
                
    return total

l = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(total(l))

