def power(base,exp):
    assert int(exp) == exp , 'Enter the integer value only '
    if exp == 0:
        return 1
    elif exp <0:
        return 1/base * power(base,exp+1)
    return base * power(base,exp-1)
    
print(power(2,10))
print(power(2,3.5))