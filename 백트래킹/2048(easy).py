import sys
input = sys.stdin.readline

from copy import deepcopy


from collections import deque

n = int(input())

origin = [[0] * (n+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n+2)]




def up(arr):
    for j in range(1, n+1):
        target = []
        for i in range(1, n+1):
            if arr[i][j] != 0:
                target.append(arr[i][j])
                arr[i][j] = 0
        
    
        for x in range(len(target) - 1):
            if target[x] != 0 and target[x] == target[x+1]:
                target[x] = target[x] * 2
                target[x+1] = 0
         
        target = list(filter(lambda a: a != 0, target))
        for x in range(len(target)):
            arr[x + 1][j] = target[x] 
    


def down(arr):
    for j in range(1, n+1):
        target = []
        for i in range(n, 0, -1):
            if arr[i][j] != 0:
                target.append(arr[i][j])
                arr[i][j] = 0
        
        
        for x in range(len(target) - 1):
            if target[x] != 0 and target[x] == target[x+1]:
                target[x] = target[x] * 2
                target[x+1] = 0
  
        target = list(filter(lambda a: a != 0, target))
        for x in range(len(target)):
            arr[n - x][j] = target[x] 




def left(arr):
    for i in range(1, n+1):
        target = []
        for j in range(1, n+1):
            if arr[i][j] != 0:
                target.append(arr[i][j])
                arr[i][j] = 0
    
    
        for x in range(len(target) - 1):
            if target[x] != 0 and target[x] == target[x+1]:
                target[x] = target[x] * 2
                target[x+1] = 0

        target = list(filter(lambda a: a != 0, target))
        for x in range(len(target)):
            arr[i][x + 1] = target[x]



def right(arr):
    for i in range(1, n+1):
        target = []
        for j in range(n, 0, -1):
            if arr[i][j] != 0:
                target.append(arr[i][j])
                arr[i][j] = 0
    
  
        for x in range(len(target) - 1):
            if target[x] != 0 and target[x] == target[x+1]:
                target[x] = target[x] * 2
                target[x+1] = 0

        
        target = list(filter(lambda a: a != 0, target))
        for x in range(len(target)):
                arr[i][n - x] = target[x] 




def find_max(arr):
    return max(map(max, arr))

direction = [up, down, left,right]
max_val = 0

def dfs(cnt, copied):
    global max_val
    if cnt == 5:
        max_val = max(max_val, find_max(copied))
        return

    for i in direction:
        send = deepcopy(copied)
        i(send)
        dfs(cnt + 1, send)





dfs(0, origin)
print(max_val)