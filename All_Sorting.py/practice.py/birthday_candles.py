#birthday candel problem
def candles(array):
    a = max(array)
    count =  0
    for i in range(len(array)):
        if array[i]== a:
            count += 1
    return count
    
    
    
arr = candles([3,4,4,1,2])    
# arrr = [3,4,5,6,6,1,2]
# arr.candles(arrr)