import sys
sys.setrecursionlimit(111111)
t = int(input())

def dfs(x):
    global teamed


    visited[x] = 1
    temp.append(x)
    next = arr[x]
    if visited[next] == 1:
        if next in temp:
            teamed += temp[temp.index(next):]
        return
    else:
        dfs(next)

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n+1) # 
    teamed = []
    for i in range(1, n+1):
        if not visited[i]:
            temp = []
            dfs(i)

    print(n - len(teamed))

