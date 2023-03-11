def dtb(a):
    if a ==0:
        return 0
    return a%2 + 10 *dtb(int(a/2)) 

print(dtb(10))
print(dtb(22))