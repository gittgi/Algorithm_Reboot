arr = [list(map(int, input().split())) for _ in range(3)]
new_arr = [[0 for i in range(3)] for i in range(3)]
visited = [False for i in range(10)]
cost = 0
min_val = 10000000
def recur(x, y):
    global cost, min_val
    if y == 3:
        y = 0
        x += 1
     
    if x == 3:
        if check():
            min_val =  min(min_val, cost)
        return
    
    for i in range(1, 10):
        if visited[i]:
            continue
        visited[i] = True
        new_arr[x][y] = i
        cost += abs(arr[x][y] - i)
        recur(x, y + 1)
        cost -= abs(arr[x][y] - i)
        visited[i] = False


def check():
    for i in range(3):
        if sum(new_arr[i]) != 15:
            return False
    
   
    for j in range(3):
        temp = 0
        for i in range(3):
            temp += new_arr[i][j]
        if temp != 15:
            return False
    
    if new_arr[0][0] + new_arr[1][1] + new_arr[2][2] != 15 or new_arr[0][2] + new_arr[1][1] + new_arr[2][0] != 15:
        return False
    
    return True

recur(0, 0)

print(min_val)