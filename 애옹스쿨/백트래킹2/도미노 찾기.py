arr = list(list(input()) for _ in range(8))
for i in range(8):
     for j in range(7):
          arr[i][j] = int(arr[i][j])
domino = [[False for _ in range(7)] for _ in range(7)]

visited = [[False for _ in range(7)] for _ in range(8)]

ans = 0
def recur(x, y):
    global ans
    if y == 7:
        x += 1
        y = 0
    
    if x == 8:
        ans += 1
        return
    
    if visited[x][y]:
        recur(x, y + 1)
        return # 여기에 return을 안해주면 안나옴
    

    target = arr[x][y]
    # 가로 한번, 세로 한번 넣어주기
    # 오른쪽 끝이거나 왼쪽 끝이면 안하기

    # 가로로 넣어주기
    if y != 6:
        right_val = arr[x][y + 1]
        if not domino[target][right_val] and not visited[x][y+1]:
            visited[x][y] = True
            visited[x][y + 1] = True
            domino[target][right_val] = True
            domino[right_val][target] = True
            recur(x, y+1)
            visited[x][y] = False
            visited[x][y + 1] = False
            domino[target][right_val] = False
            domino[right_val][target] = False
    
    # 세로로 넣어주기
    if x != 7:
        down_val = arr[x+1][y]
        if not domino[target][down_val] and not visited[x+1][y]:
            visited[x][y] = True
            visited[x+1][y] = True
            domino[target][down_val] = True
            domino[down_val][target] = True
            recur(x, y+1)
            visited[x][y] = False
            visited[x+1][y] = False
            domino[target][down_val] = False
            domino[down_val][target] = False



                    


recur(0, 0)
print(ans)



        
        


    

