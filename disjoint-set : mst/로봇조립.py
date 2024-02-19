import sys
input = sys.stdin.readline

n = int(input())

arr = [i for i in range(int(10e6) + 1)]
length = [1 for i in range(int(10e6) + 1)]



def find(x):
    if arr[x] != x:
        x = find(arr[x])
        arr[x] = x
    return x
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x!= y:
            if length[x] < length[y]:
                arr[x] = y
                length[y] += length[x]
            else:
                arr[y] = x
                length[x] += length[y]


for _ in range(n):
    str = input()
    if str[0] == "I":
         d, a, b = str.split()
         union(int(a), int(b))
    else:
         d, k = str.split()
         print(length[find(int(k))])