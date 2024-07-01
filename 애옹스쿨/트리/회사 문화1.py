import sys
sys.setrecursionlimit(100010)
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))
comp = [0 for _ in range(n+1)] 
tree = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    comp[a] = b

for i in range(n+1):
    # arr[i] = i의 부모
    if arr[i] <= 0:
        continue
    tree[arr[i]].append(i)

def dfs(x, val):
    comp[x] += val
    for i in tree[x]:
        dfs(i, comp[x])

dfs(1, 0)
print(*comp[1:])