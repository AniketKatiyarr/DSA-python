'''
linearsearch (arr,item)
for each item in array:
  if item==element
    return its index
return -1
'''
def linearSearch(array,startingn,searchx ):
    for i in range(0,startingn):
        if (array[i] == searchx):
          return i
    return -1

array = [2,3,4,5,6,7,8,9,7,65,34,23]
searchx =34
startingn = len(array)

result = linearSearch(array,startingn,searchx)
if(result==-1):
    print("enter not found")
else:
     print("element found at index:->",result) 
     
     
def linear(array,search):
      for i in range(0,len(array)):
            if array[i] == search:
                  return i
      return -1

array = [1,2,3,4,5,6,7,8,9,54,32,667,89,65,33,22]
search = 89


result = linear(array,search)
print(result)


            
           