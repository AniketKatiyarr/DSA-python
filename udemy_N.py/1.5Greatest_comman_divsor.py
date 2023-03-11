def GCD(a,b):
    if a <0:
        a = -1 *a
    if b<0:
        b = -1*b
    if b ==0:
        return a 
    else:
        return GCD(b,a%b)

print(GCD(48,18))
print(GCD(36,12))
print(GCD(42,-21))
print(GCD(-110,55))


