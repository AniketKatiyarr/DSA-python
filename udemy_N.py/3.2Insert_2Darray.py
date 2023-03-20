import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])


#inserting time colplexity::-- O(MN)

NewArray =  np.insert(array,0,[[11,22,33]],axis=1)
#NewArray =  np.insert(name of aarray,position to insert(which row ,col),value to print,which axis 1 for col 0 for row)
 #for column its 1 and for row its 0

print(NewArray)


#for rows inseetion
import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]])


#inserting time colplexity::-- O(MN)

NewArray =  np.insert(array,0,[[44,55,66]],axis=0)
#NewArray =  np.insert(name of aarray,position to insert(which row ,col),value to print,which axis 1 for col 0 for row)
 #for column its 1 and for row its 0

print(NewArray)


#append is also used to append the row or column at the end of the matrix
 
 
 