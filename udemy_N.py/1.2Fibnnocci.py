def fibonnocci(n):
    if n == 0 or n==1:
        return n
    else:   
        return fibonnocci(n-1) + fibonnocci(n-2)

print(fibonnocci(10))
