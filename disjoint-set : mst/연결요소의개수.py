import sys
input = sys.stdin.readline


n, m = map(int, input().split())

parent = [i for i in range(n+1)]
rank = [1] * (n + 1)

def find(x):
    if parent[x]!= x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if rank[x] < rank[y]:
        parent[x] = y
        rank[y] = rank[x] + 1
    elif rank[x] > rank[y]:
        parent[y] = x
        rank[x] = rank[y] + 1
    else:
        parent[y] = x
        rank[x] += 1


for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

temp = set()
for i in range(1, n+1):
    temp.add(find(i))
print(len(temp))


