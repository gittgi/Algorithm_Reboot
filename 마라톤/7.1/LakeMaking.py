r, c, e, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]

sequence = []
for i in range(n):
    sequence.append(list(map(int, input().split())))

for x, y, d in sequence:
    x = x-1
    y = y-1
    max_val = 0
    for i in range(3):
        for j in range(3):
            max_val = max(max_val, arr[x+i][y+j])
    
    make_val = max(max_val - d, 0)
    for i in range(3):
        for j in range(3):
            arr[x+i][y+j] = min(make_val, arr[x+i][y+j])

answer = 0
for i in range(r):
    for j in range(c):
        answer += max(e - arr[i][j], 0)


print(answer * 72 * 72)