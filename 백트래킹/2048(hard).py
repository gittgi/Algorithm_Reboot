import sys
input = sys.stdin.readline

# from copy import deepcopy


from collections import deque

n = int(input())

origin = [[0] * (n+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n+2)]

def is_changed(arr1, arr2):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr1[i][j] != arr2[i][j]:
                return True
    
    return False


def up(arr):
    for j in range(1, n+1):
        target = []
        for i in range(1, n+1):
            if arr[i][j] != 0:
                target.append(arr[i][j])
                arr[i][j] = 0
        
    
        for x in range(len(target) - 1):
            if target[x] != 0 and target[x] == target[x+1]:
                target[x] <<= 1
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
                target[x] <<= 1
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
                target[x] <<= 1
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
                target[x] <<= 1
                target[x+1] = 0

        
        target = list(filter(lambda a: a != 0, target))
        for x in range(len(target)):
                arr[i][n - x] = target[x] 




def find_max(arr):
    return max(map(max, arr))

direction = [up, down, left,right]

max_val_dp = [0] * 11


def dfs(cnt, copied):
    temp_max = find_max(copied)
    
    if temp_max < max_val_dp[cnt]:
        return
    
    max_val_dp[cnt] = temp_max

    if cnt == 10:
        return

    for i in direction:
        send = [a[:] for a in copied]
        i(send)
        if is_changed(send, copied):
            dfs(cnt + 1, send)
        else:
            continue





dfs(0, origin)
print(max(max_val_dp))