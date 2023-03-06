def first():
    second()
    print("hello first")

def second():
    third()
    print("hello Second")

def third():
    fourth()
    print("hello Third")

def fourth():
    print("hello fourth")
    
a = first()
print(a)

print()

def recursive(n):
    if n<1:
        print("value is less than 1")
    else:
        recursive(n-1)
        print(n)

a = recursive(4)

print()


def swap(n):
    li = []
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
                temp = n [i]
                n[i] = n[i+1]
                n[i+1] = temp
    return li

print(swap([1,4,6,8,4,21,20]))


