#by  iteration
def sumofDigit(n):
    sum = 0
    while (n >0):
        sum = sum + n%10 
        n = n//10
    return sum
print(sumofDigit(1234))        
     
     
#By Recursion Method
print("By recursion you get this:")
def sumofdigit(n):
    if n==0:
        return 0
    else:
        return n%10 + sumofDigit(n//10)
 
print(sumofDigit(12345))  