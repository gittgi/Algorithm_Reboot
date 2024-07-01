import sys
sys.setrecursionlimit(100010)

n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

sb = [0 for _ in range(n+1)]

def recur(x, prv):
    sb[x] = 1
    for i in tree[x]:
        if i == prv:
            continue

        recur(i, x)
        sb[x] += sb[i]

recur(r, 0)

print(sb)
for _ in range(q):
    print(sb[int(input())])