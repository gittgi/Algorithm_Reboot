import sys
input = sys.stdin.readline

n = int(input())

arr = list(list(map(int, input().split())) for _ in range(n))


max_prev = [0, 0, 0]
max_now = [0, 0, 0]
min_prev = [0, 0, 0]
min_now = [0,0,0]


for i in range(3):
    max_prev[i] = arr[0][i]
    min_prev[i] = arr[0][i]

for i in range(1, n):
    max_now[0] = arr[i][0] + max(max_prev[0], max_prev[1])
    max_now[1] = arr[i][1] + max(max_prev[0], max_prev[1], max_prev[2])
    max_now[2] = arr[i][2] + max(max_prev[1], max_prev[2])

    min_now[0] = arr[i][0] + min(min_prev[0], min_prev[1])
    min_now[1] = arr[i][1] + min(min_prev[0], min_prev[1], min_prev[2])
    min_now[2] = arr[i][2] + min(min_prev[1], min_prev[2])

    for j in range(3):
        max_prev[j] = max_now[j]
        min_prev[j] = min_now[j]


    

print (max(max_prev), min(min_prev))