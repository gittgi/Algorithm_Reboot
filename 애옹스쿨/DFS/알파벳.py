

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

visited_chr = [0 for _ in range(26)]

def dfs(x, y, cnt):
    max_val = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0<=ny <c :
            if visited_chr[ord(arr[nx][ny]) - ord("A")] == 0:
                visited_chr[ord(arr[nx][ny]) - ord("A")] += 1
                max_val = max(max_val, dfs(nx, ny, cnt+1))
                visited_chr[ord(arr[nx][ny]) - ord("A")] -= 1
    
    return max_val


visited_chr[ord(arr[0][0]) - ord("A")] = 1
print(dfs(0, 0, 1))
