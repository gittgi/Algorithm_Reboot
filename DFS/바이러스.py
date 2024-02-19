from collections import deque

N = int(input())
arr = [[] for _ in range(N)]
l = int(input())

for _ in range(l):
    v, w = map(int, input().split())
    arr[v-1].append(w-1)
    arr[w-1].append(v-1)

visited = [0] * N

stack = deque()
stack.append(0)
while stack:
    now = stack.pop()
    visited[now] = 1
    for i in arr[now]:
        if visited[i] == 0:
            stack.append(i)

print(sum(visited) - 1)