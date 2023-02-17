def hash(key,m):
    return key%m

m = 8
print(f'hash value for 4 is {hash(4,m)}')
print(f'hash value for 3 is {hash(3,m)}')
print(f'hash value for 10 is {hash(10,m)}')
print(f'hash value for 12 is {hash(12,m)}')
print(f'hash value for 8 is {hash(8,m)}')
