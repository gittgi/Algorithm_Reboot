import sys
sys.setrecursionlimit(100010)

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

par = [0 for _ in range(n+1)]

def find_parent(x, prv):

    for i in arr[x]:
        if i == prv:
            continue

        par[i] = x
        find_parent(i, x)


find_parent(1, 0)

for i in range(2, n+1):
    print(par[i])
