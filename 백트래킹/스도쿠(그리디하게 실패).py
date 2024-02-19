import sys

input = sys.stdin.readline

class Node:
    def __init__(self):
        self.possible = [True] * 10
        self.possible[0] = False

    def __str__(self):
        return str(self.possible) 
    

    def discard(self, arr):
        for i in arr:
            self.possible[i] = False


def garo(row_index):
    temp = []
    for i in arr[row_index]:
        if type(i) == int:
            temp.append(i)
    return temp

def sero(column_index):
    temp = []
    for i in range(9):
        if type(arr[i][column_index]) == int:
            temp.append(arr[i][column_index])
            
    return temp

def box(x, y):
    temp = []
    for i in range(3):
        for j in range(3):
            if type(arr[x+i][y+j]) == int:
                temp.append(arr[x+i][y+j])
    return temp



arr = [list(input().strip()) for _ in range(9)]
empty_cnt = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] == '0':
            empty_cnt += 1
            arr[i][j] = Node()
        else:
            arr[i][j] = int(arr[i][j])



while empty_cnt > 0:
    for i in range(9):
        temp = garo(i)
        for j in range(9):
            if type(arr[i][j]) == Node:
                arr[i][j].discard(temp)

    for j in range(9):
        temp = sero(j)

        for i in range(9):
            if type(arr[i][j]) == Node:
                arr[i][j].discard(temp)

    for i in (0, 3, 6):
        for j in (0, 3, 6):
            temp = box(i, j)
            for x in range(3):
                for y in range(3):
                    if type(arr[i+x][j+y]) == Node:
                        arr[i+x][j+y].discard(temp)

                
    for i in range(9):
        for j in range(9):
            if type(arr[i][j]) == Node:
                if arr[i][j].possible.count(True) == 1:
                    empty_cnt -= 1
                    arr[i][j] = arr[i][j].possible.index(True)



for row in arr:
    print("".join(list(map(str, row))))


