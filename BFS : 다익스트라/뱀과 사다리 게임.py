import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * 101

for _ in range(n + m):
    a, b = map(int, input().split())
    arr[a] = b

visited = [0] * 101

def bfs():
    q = deque()
    q.append(1)
   

    while q:
        x = q.popleft()
        if x == 100:
            return visited[x]
        for i in range(1, 7):
            if x + i <= 100:
                if visited[x + i] == 0:
                    visited[x + i] = visited[x] + 1
                    if arr[x + i]:
                        new_x = x+i
                        while arr[new_x] != 0 and visited[new_x] != 0:
                            if visited[arr[new_x]] == 0:
                                visited[arr[new_x]] = visited[x] + 1
                            new_x = arr[new_x]
                        q.append(new_x)
                    else:
                        q.append(x+i)

print(bfs())
