import sys
from collections import deque

input = sys.stdin.readline

# def D(x):

#     return (x * 2) % 10000

# def S(x):
#     if x - 1 == 0:
#         return 9999
#     else:
#         return x - 1
    
# def L(x):
#     return (x%1000) * 10 + (x //1000)

# def R(x):
#     return (x%10)*1000 + (x // 10)

def bfs(x):
    q = deque()
    q.append(('', x))
    visited = [0] * 10001
    visited[x] = 1
    while q:
        seq, x = q.popleft()
        for i in ['D', 'S', 'L', 'R']:
            if i == 'D':
                new = (x * 2) % 10000
            elif i == 'S':
                if x == 0:
                    new = 9999
                else:
                    new = x - 1
            elif i == 'L':
                new = (x%1000) * 10 + (x //1000)
            else:
                new = (x%10)*1000 + (x // 10)
            new_seq = seq + i
            if new == target:
                return new_seq
            if visited[new] == 0:
                visited[new] = 1
                q.append((new_seq, new))



tc = int(input())

for _ in range(tc):
    origin, target = map(int, input().split())
   

    ans = bfs(origin)

    print(ans)
    
