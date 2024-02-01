def get_gcd(a, b):
    if b > a:
        a, b = b, a
    while a % b != 0:
        a, b = b, a % b
    return b



        

arr = [0] * 1001

arr[1] = 3
arr[2] = 5

for i in range(3, 1001):
    cnt = 0
    for j in range(1, i+1):
        if get_gcd(i, j) == 1:
            cnt += 2
    arr[i] = arr[i-1] + cnt

c = int(input())

for _ in range(c):
    n = int(input())
    print(arr[n])