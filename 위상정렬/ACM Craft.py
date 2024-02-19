import sys
from collections import deque
input = sys.stdin.readline

def topology_sort(k):
    q = deque()
    dp = [0] *(n+1) # i번째 건물을 짓는 최소 시간

    for i in range(1, n+1):
        if jinip[i] == 0:
            q.append(i)
            dp[i] = build_delay[i]
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            jinip[i] -= 1
            dp[i] = max(dp[i], dp[x] + build_delay[i])
            if jinip[i] == 0:
                q.append(i)
    
    print(dp[k])

t = int(input())
for __ in range(t):
    n, k = map(int, input().split())

    build_delay = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]

    jinip = [0] * (n+1)

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        jinip[b] += 1

    topology_sort(int(input()))
