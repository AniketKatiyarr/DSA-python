#a= 6.8
#a= int(a)
#print(type(a))
#print(a+4)
#
#print(int (6.8))


def reverseArray(a):
    # Write your code here


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()