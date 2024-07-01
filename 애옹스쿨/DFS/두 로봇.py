import sys
sys.setrecursionlimit(10**6)

n, a, b = map(int, input().split())
arr = list([] for _ in range(n+1))
for i in range(n-1):
    s, e, v = map(int, input().split())
    arr[s].append((e, v))
    arr[e].append((s, v))


# 둘다 움직이려고 하지말고, 하나만 움직이자
# 해당 길로 가는 방법은 하나이기 때문에, 쭉 가다가 가장 큰값만 빼주면 됨
visited = [False for _ in range(n+1)]

def recur(cur, total, max_val):
    visited[cur] = True

    if cur == b:
        return total - max_val
    
    min_val = 1 << 60
    for i, d in arr[cur]:
        if visited[i]:
            continue
        
        min_val = min(min_val, recur(i, total + d, max(max_val, d)))
    
    return min_val
    

print(recur(a, 0, 0))
        
