import sys
import heapq
input = sys.stdin.readline

def find(x):

    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if rank[a] > rank[b]:
            parent[b] = a
        elif rank[a] < rank[b]:
            parent[a] = b
        else:
            parent[a] = b
            rank[b] += 1
        return True
    
    return False



        
n, m = map(int, input().split())

edge = []
parent = [i for i in range(n+1)]
rank = [1] * (n+1)


for i in range(m):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort()

ans = 0

for cost, a, b in edge:
    if union(a, b):
        ans += cost
        last = cost
    
print(ans - last)