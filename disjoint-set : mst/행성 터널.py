import sys
input = sys.stdin.readline

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

n = int(input())
planet = []

edges = []

for i in range(n):
    x, y, z = map(int, input().split())
    planet.append((x,y,z,i))
for xyz in range(3):
    planet.sort(key=lambda x:x[xyz])
    for i in range(n-1):
        edges.append(((abs(planet[i][xyz] - planet[i+1][xyz])), planet[i][3], planet[i+1][3]))
        




parent = [i for i in range(n)]
rank = [1 for i in range(n)]

edges.sort(reverse=True)
ans = 0
while edges:
    dist, x, y = edges.pop()
    if find(x) != find(y):
        union(x,y)
        ans += dist

print(ans)




