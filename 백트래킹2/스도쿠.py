import sys
input = sys.stdin.readline
sudoku = list(list(map(int, input().split())) for _ in range(9))


zero_list = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_list.append((i, j))

def check_v(x, y, num):
  
    for i in range(9):
        if sudoku[i][y] == num:
            return False
    return True
            


def check_h(x, y, num):

    for j in range(9):
        if sudoku[x][j] == num:
            return False
    return True

def check_sq(x, y, num):
    if 3 > x >= 0:
        start_x = 0
        end_x = 3
    elif 6 > x >= 3:
        start_x = 3
        end_x = 6
    else:
        start_x = 6
        end_x = 9

    if 3 > y >= 0:
        start_y = 0
        end_y = 3
    elif 6 > y >= 3:
        start_y = 3
        end_y = 6
    else:
        start_y = 6
        end_y = 9

    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if sudoku[i][j] == num:
                return False
    return True
                

def solve(idx):
    if idx == len(zero_list):
        for l in sudoku:
            print(*l)
        quit()

    i, j = zero_list[idx]

    for k in range(1, 10):
        if check_h(i, j, k) and check_v(i, j, k) and check_sq(i, j, k):
            sudoku[i][j] = k
            solve(idx+1)
            sudoku[i][j] = 0


solve(0)