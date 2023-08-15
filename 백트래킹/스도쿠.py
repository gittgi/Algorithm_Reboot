

arr = [list(input().strip()) for _ in range(9)]
empty = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == '0':
          empty.append((i, j))  

def garo(row_index, num):
    for i in arr[row_index]:
        if i == num:
            return False
    return True

def sero(column_index, num):
    for i in range(9):
        if arr[i][column_index] == num:
            return False
    return True

def box(x, y, num):
    a = int((x // 3) * 3)
    b = int((y // 3) * 3)

    for i in range(3):
        for j in range(3):
            if arr[a + i][b + j] == num:
                return False
    return True

def check(x, y, num):
    if garo(x, num) and sero(y, num) and box(x, y, num):
        return True
    return False


def dfs(idx):
    if idx == len(empty):
        for i in arr:
            print("".join(i))
        quit()
    x, y = empty[idx]
    for num in range(1, 10):
        if check(x, y, str(num)):
            arr[x][y] = str(num)
            dfs(idx+1)
            arr[x][y] = '0'
            
dfs(0)