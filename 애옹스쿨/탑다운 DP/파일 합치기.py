t = int(input())

def recur(cur, cost):
    if cur == len(arr):
        return cost
    
    for i in range(0, len(arr)):
        if visited[cur]:continue
        
        recur(cur + 1, cost + )



for _ in range(t):
    k = int(input())
    arr = list(map(int, input().split()))
    visited = [False for _ in range(k)]