import sys

input = sys.stdin.readline

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


n, m = map(int, input().split())


arr = [i for i in range(n+1)]
length = [1 for i in range(n+1)]

for _ in range(m):
    f, a, b = map(int, input().split())
    if f == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")