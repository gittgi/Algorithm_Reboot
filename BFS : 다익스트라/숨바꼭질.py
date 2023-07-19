from collections import deque

n, k = map(int, input().split())

visited = [0] * (200001)

def bfs(n):

    q = deque()
    q.append(n)


    while q:
        now = q.popleft()

        for i in [now + 1, now - 1, 2 * now]:

            if i == k:
                print(visited[now] + 1)
                quit()
            if i < 0 or i > 100000:
                continue
            if visited[i] == 0:
                visited[i] = visited[now] + 1
                q.append(i)

bfs(n)


