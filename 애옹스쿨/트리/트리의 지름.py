import sys
sys.setrecursionlimit(10010)
input = sys.stdin.readline

n = int(input())

arr = [[] for i in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

max_val = 0
idx = -1

def recur(x, prv, d):
    global max_val, idx
    if d > max_val:
        idx = x
        max_val = d

    
    for i, v in arr[x]:
        if i == prv:
            continue

        recur(i, x, d + v)

recur(1, 0, 0)
max_val = 0
recur(idx, 0, 0)
print(max_val)