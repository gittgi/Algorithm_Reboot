from collections import deque

n, k = map(int, input().split())

visited = [float("inf")] * (200001)

def bfs(n):

    q = deque()
    q.append(n)
    visited[n] = 0


    while q:
        now = q.popleft()
        # 가중치가 다르다(1칸 움직일 때는 1, 두배로 순간이동 할 때는 0 -> 가중치가 다를 땐 다익스트라)
        if now * 2 < 0 or now * 2 > 100000:
            pass
        elif visited[now*2] > visited[now]:
            visited[now*2] = visited[now]
            q.append(now * 2)

        for i in [now + 1, now - 1]:

            if i < 0 or i > 100000:
                continue
            if visited[i] > visited[now] + 1:
                visited[i] = visited[now] + 1
                q.append(i)

        

if n == k:
    print(0)
else:
    bfs(n)
    print(visited[k])


