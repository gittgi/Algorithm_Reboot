arr = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append((i, j))


def virtical_check(j, num):
    for i in range(9):
        if arr[i][j] == num:
            return False
    return True

def horizontal_check(i, num):
    for j in range(9):
        if arr[i][j] == num:
            return False
    return True

def square_check(i,j,num):
    i = 3 * (i // 3)
    j = 3 * (j // 3)
    for di in range(i, i+3):
        for dj in range(j, j+3):
            if arr[di][dj] == num:
                return False
    return True

def recur(cur):

    if cur == len(blank):
        for i in arr:
            print(*i)
        quit()

    
    x, y = blank[cur]
    for i in range(1, 10):
        if horizontal_check(x, i) and virtical_check(y, i) and square_check(x, y, i):
            arr[blank[cur][0]][blank[cur][1]] = i
            recur(cur + 1)
            arr[blank[cur][0]][blank[cur][1]] = 0

recur(0)