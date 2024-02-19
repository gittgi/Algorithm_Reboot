import sys
input = sys.stdin.readline



v, e = map(int, input().split())
parent = [i for i in range(v+1)]
rank = [1 for i in range(v+1)]


temp = [0] * e

for i in range(e):
    temp[i] = tuple(map(int, input().split()))

temp.sort(key=lambda x: x[2])


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if rank[x] < rank[y]:
        parent[x] = y
   
    elif rank[x] > rank[y]:
        parent[y] = x
 
    else:
        parent[y] = x
        rank[x] += 1

total = 0
for i in temp:
    a, b, d = i

    if find(a) != find(b):
        union(a, b)
        total += d

print(total)