from collections import deque
def solution(board):
    n = len(board)
    m = len(board[0])
    def move(x, y, dx, dy):
        while n > x+dx >= 0 and m > y+dy >= 0:
            if board[x+dx][y+dy] == "G":
                return (x + dx, y + dy, True)
            if board[x+dx][y+dy] != "D":
                x += dx
                y += dy
            else:
                return(x + dx, y + dy, False)
        
        return (x, y, False)
    
    
    visited = [[False for i in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                x = i
                y = j
                break
    
    
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 0
    
    while q:
        size = len(q)
        cnt += 1
        for i in range(size):  
            x, y = q.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny, isG = move(x, y, dx, dy)
                if isG:
                    return cnt
                elif visited[nx][ny]:
                    continue
                else:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                
    return -1


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))